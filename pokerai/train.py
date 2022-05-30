import time
import torch
import torch.optim as optim
import torch.nn.functional as F
import torch.nn as nn
from random import randint
from pokerai.card_compute import card_compute
from poker import Poker
from pokerai.n_network import NeuralNetwork

print("="*10, "Training", "="*10)

filename = "dummy2.ph"
PATH = "/home/hyde/Documents/PokerAI/pokerai/data/" + filename

EPOCHS = 40

net = NeuralNetwork()
optimizer = optim.Adam(net.parameters(), lr=0.001)
poker = Poker()
start = time.time()
poker.new_game('human', 'bot')

loss = nn.BCELoss()

EPSILON_CONSTANT = 80  # Used to control randomness
epsilon = 0    # Control the randomness

def clear_output(output):
    return 1 if output > 0.5 else 0
    #return 1 if torch.argmax(output) == 0 else 0


for epoch in range(EPOCHS):
    print('=' * 5, f'Epoch {epoch + 1}', '=' * 5)
    net.zero_grad()
    players = poker.new_match()
    print(f'Human: {players["human"]}', f'Bot: {players["bot"]}')
    outcome_all = []

    X = torch.tensor([card_compute(players['bot'][0]), card_compute(players['bot'][1]),
                      0, 0, 0, 0, 0], dtype=torch.float)
    expt_outcome = poker.exepected_outcome('bot')
    y = torch.tensor(expt_outcome, dtype=torch.float)
    #y = y.type(torch.LongTensor)

    print(f'Expected outcome: {expt_outcome}')
    outcome = net(X)
    print(outcome)

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

            epsilon = EPSILON_CONSTANT - epoch
            if randint(0, 100) < epsilon:
                print("RANDOM")
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
        print(f'Winner: {poker.winner()["winner"][0]}')

    # Convert outcome_all to tensor
    outcome_all = torch.cat(outcome_all)
    print("OUTCOME ALL:", outcome_all)

    output = loss(outcome_all, y)
    print(f'Loss: {output}')
    output.backward()
    optimizer.step()

end = time.time()
print("--- %s seconds ---" % (end - start))

save = input("Save model[y/n]: ")
if save.lower() == "y":
    torch.save(net.state_dict(), PATH)
