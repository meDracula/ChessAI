import torch
import torch.optim as optim
import torch.nn.functional as F
import torch.nn as nn
import time
from random import randint
from os import path
from pokerai.card_compute import card_compute
from poker import Poker
from pokerai.n_network import NeuralNetwork

EPSILON_CONSTANT = 40  # Used to control randomness
REWARD_CONSTANT = 0.1 # Used to control reward

def clear_output(output):
    return 1 if output > 0.5 else 0

def penalty(expected_outcome, outcome_all):
    print(expected_outcome, outcome_all)
    clear_outcome_all = [clear_output(outcome) for outcome in outcome_all]
    idx = next((i for i in range(4) if clear_outcome_all[i] != expected_outcome[i]), 4)
    return REWARD_CONSTANT*(4 - idx)


def train(net, epochs):
    poker = Poker()
    poker.new_game('human', 'bot')
    winners = []

    optimizer = optim.Adam(net.parameters(), lr=0.001)

    loss = nn.BCELoss()

    for epoch in range(epochs):
        print('=' * 5, f'Epoch {epoch + 1}', '=' * 5)
        net.zero_grad()
        players = poker.new_match()
        print(f'Human: {players["human"]}', f'Bot: {players["bot"]}')
        outcome_all = []

        X = torch.tensor([card_compute(players['bot'][0]), card_compute(players['bot'][1]),
                          0, 0, 0, 0, 0], dtype=torch.float)
        expt_outcome = poker.exepected_outcome('bot')
        y = torch.tensor(expt_outcome, dtype=torch.float)

        print(f'Expected outcome: {expt_outcome}')
        outcome = net(X)

        action = clear_output(outcome)
        outcome_all.append(outcome)

        if action == 1:
            for turn in poker:
                community_cards = turn
                community_cards = community_cards['community cards']
                if len(community_cards) == 3:
                    X = torch.tensor([card_compute(players['bot'][0]),
                                  card_compute(players['bot'][1]),
                                  card_compute(community_cards[0]),
                                  card_compute(community_cards[1]),
                                  card_compute(community_cards[2]), 0, 0], dtype=torch.float)

                elif len(community_cards) == 4:
                    X = torch.tensor([card_compute(players['bot'][0]),
                                  card_compute(players['bot'][1]),
                                  card_compute(community_cards[0]),
                                  card_compute(community_cards[1]),
                                  card_compute(community_cards[2]),
                                  card_compute(community_cards[3]), 0], dtype=torch.float)

                else:
                    X = torch.tensor([card_compute(players['bot'][0]),
                                  card_compute(players['bot'][1]),
                                  card_compute(community_cards[0]),
                                  card_compute(community_cards[1]),
                                  card_compute(community_cards[2]),
                                  card_compute(community_cards[3]),
                                  card_compute(community_cards[4])], dtype=torch.float)

                print(f'Community cards: {community_cards}')
                outcome = net(X)

                epsilon = EPSILON_CONSTANT - epoch # Control the randomness
                if randint(0, 100) < epsilon:
                    print(f"RANDOM ROUND: {len(community_cards) - 1}")
                    action = 0 if randint(0,1) == 0 else 1
                else:
                    action = clear_output(outcome)
                outcome_all.append(outcome)

                if action == 0:
                    poker.folds("bot")
                    break



        if action == 0:
            print(f'Folded round: {len(outcome_all)}')
            for _ in range(4-len(outcome_all)):
                outcome_all.append(torch.tensor([0.], dtype=torch.float, requires_grad=True))
        else:
            winner = poker.winner()["winner"]
            print(f'Winner: {winner[0]}')
            winners.append(winner[0])

        # Convert outcome_all to tensor
        outcome_all = torch.cat(outcome_all)
        print("OUTCOME ALL:", outcome_all)

        output = loss(outcome_all, y)

        # Introduce penalty and reward
        print(f'Loss: {output}')
        output += penalty(y, outcome_all)

        print(f'Loss: {output}')
        output.backward()
        optimizer.step()

    print(f"bot wins:{winners.count('bot')}")
    print(f"human wins:{winners.count('human')}")


def main():

    net = NeuralNetwork()

    print("="*10, "Training", "="*10)

    start = time.time()
    train(net, 5000)
    end = time.time()
    print("--- %s seconds ---" % (end - start))

    save = input("Save model[y/n]: ")
    if save.lower() == "y":
        filename = input("File name: ") + ".ph"
        current_dir = path.join(path.dirname(path.realpath(__file__)), "data")
        torch.save(net.state_dict(), path.join(current_dir, filename))

if __name__ == '__main__':
    main()
