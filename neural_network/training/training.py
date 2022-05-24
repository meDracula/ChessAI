import torch

from neural_network.card_compute import card_compute
from poker import Poker
from neural_network.n_network import NeuralNetwork
import torch.optim as optim
import torch.nn.functional as F

net = NeuralNetwork(11, 64)
omptimizer = optim.Adam(net.parameters(), lr=0.001)

EPOCHS = 1
poker = Poker()

poker.new_game('human', 'bot')
for epoch in range(EPOCHS):
    net.zero_grad()
    players = poker.new_match()
    print(players)
    hand = card_compute(players['human'][0])
    print(hand)
    outcome_all = []
    # preflop round
    X = torch.tensor([card_compute(players['bot'][0]),
                      card_compute(players['bot'][1]),
                      0, 0, 0, 0, 0, 1, 0, 0, 0], dtype=torch.float)

    y = torch.tensor(poker.exepected_outcome('bot'))
    print(X, y)
    for turn in poker:

        #flop round
        community_cards = turn
        community_cards = community_cards['community cards']
        if len(community_cards) == 3:
            X[2] = card_compute(community_cards[0])
            X[3] = card_compute(community_cards[1])
            X[4] = card_compute(community_cards[2])
            X[-4] = 0
            X[-3] = 1
        elif len(community_cards) == 4:
            X[5] = card_compute(community_cards[3])
            X[-3] = 0
            X[-2] = 1
        else:
            X[6] = card_compute(community_cards[4])
            X[-2] = 0
            X[-1] = 1

        outcome = net(X)
        outcome_all.append(outcome)
        print(outcome, outcome_all)
        if outcome[1] == 1:
            poker.folds('bot')
            break

    winner = poker.winner()
    print(winner)
    print(outcome_all)

    outcome_all = torch.tensor(outcome_all)
    loss = F.nll_loss(outcome_all, y)
    loss.backward()
    omptimizer.step()

        # X = torch.tensor([card_compute(players['bot'][0]),
        #                   card_compute(players['bot'][1]),
        #                   card_compute(community_cards[0]),
        #                   card_compute(community_cards[1]),
        #                   card_compute(community_cards[2]),
        #                   0, 0, 0, 1, 0, 0], dtype=torch.float)

        #turn round
        # community_cards = turn
        # X = torch.tensor([card_compute(players['bot'][0]),
        #                   card_compute(players['bot'][1]),
        #                   card_compute(community_cards[0]),
        #                   card_compute(community_cards[1]),
        #                   card_compute(community_cards[2]),
        #                   card_compute(community_cards[3]),
        #                   0, 0, 0, 0, 1, 0], dtype=torch.float)
        #
        # #river round
        # community_cards = turn
        # X = torch.tensor([card_compute(players['bot'][0]),
        #                   card_compute(players['bot'][1]),
        #                   card_compute(community_cards[0]),
        #                   card_compute(community_cards[1]),
        #                   card_compute(community_cards[2]),
        #                   card_compute(community_cards[3]),
        #                   card_compute(community_cards[4]),
        #                   0, 0, 0, 0, 0, 1], dtype=torch.float)

    #y = torch.tensor(poker.exepected_outcome())
    #output = net(X)
        # loss = F.nll_loss(output, y)
        # loss.backward()
        # omptimizer.step()




# correct = 0
# total = 0

# with torch.no_grad():
#     for data in :
#         X, y = data
#         output =
#         for idx, i in enumerate(output):
#             if torch.argmax(i) == y[idx]:
#                 correct += 1
#             total += 1
