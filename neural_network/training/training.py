import os
import time
import torch
import torch.optim as optim
import torch.nn.functional as F
from neural_network.card_compute import card_compute
from poker import Poker
from neural_network.n_network import NeuralNetwork

net = NeuralNetwork(11, 64)
omptimizer = optim.Adam(net.parameters(), lr=0.001)

EPOCHS = 1000
poker = Poker()
start = time.time()
def clear_output(output):
    _, index = torch.max(torch.abs(output), dim=0)
    return [1, 0] if index == 0 else [0, 1]

poker.new_game('human', 'bot')
for epoch in range(EPOCHS):
    print('=' * 5, f'Epoch {epoch + 1}', '=' * 5)
    net.zero_grad()
    players = poker.new_match()
    print(f'Human: {players["human"]}', f'Bot: {players["bot"]}')
    outcome_all = []
    # preflop round
    X = torch.tensor([card_compute(players['bot'][0]),
                      card_compute(players['bot'][1]),
                      0, 0, 0, 0, 0, 1, 0, 0, 0], dtype=torch.float)

    expt_outcome = poker.exepected_outcome('bot')
    y = torch.tensor(expt_outcome, dtype=torch.float)
    y = y.type(torch.LongTensor)
    print(f'Expected outcome: {expt_outcome}')
    outcome = net(X)
    outcome_all.append(outcome)

    for turn in poker:

        community_cards = turn
        community_cards = community_cards['community cards']
        if len(community_cards) == 3:
            X = torch.tensor([card_compute(players['bot'][0]),
                          card_compute(players['bot'][1]),
                          card_compute(community_cards[0]),
                          card_compute(community_cards[1]),
                          card_compute(community_cards[2]),
                          0, 0, 0, 1, 0, 0], dtype=torch.float)

        elif len(community_cards) == 4:
            X = torch.tensor([card_compute(players['bot'][0]),
                          card_compute(players['bot'][1]),
                          card_compute(community_cards[0]),
                          card_compute(community_cards[1]),
                          card_compute(community_cards[2]),
                          card_compute(community_cards[3]),
                          0, 0, 0, 1, 0], dtype=torch.float)

        else:
            X = torch.tensor([card_compute(players['bot'][0]),
                          card_compute(players['bot'][1]),
                          card_compute(community_cards[0]),
                          card_compute(community_cards[1]),
                          card_compute(community_cards[2]),
                          card_compute(community_cards[3]),
                          card_compute(community_cards[4]),
                          0, 0, 0, 1], dtype=torch.float)

        print(f'Community cards: {community_cards}')
        outcome = net(X)
        outcome_all.append(outcome)
        if clear_output(outcome)[1] == 1:
            poker.folds("bot")
            break

    if len(outcome_all) != 4:
        print(f'Folded round: {len(outcome_all)}')
    else:
        print(f'Winner: {poker.winner()["winner"][0]}')

    for i in range(len(outcome_all)):
        loss = F.nll_loss(outcome_all[i], y[i])

        print(f'Loss: {loss}')
        loss.backward()
    omptimizer.step()

path = 'C:\\Code\\ChessAI\\neural_network\\training\\dummy.ph'
#path = "/home/hyde/Documents/PokerAI/neural_network/training/dummy.ph"
torch.save(net.state_dict(), path)
end = time.time()

print("--- %s seconds ---" % (end - start))
