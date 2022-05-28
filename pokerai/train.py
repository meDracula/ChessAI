import time
import torch
import torch.optim as optim
import torch.nn.functional as F
from pokerai.card_compute import card_compute
from poker import Poker
from pokerai.n_network import NeuralNetwork

EPOCHS = int(input('How many epochs would you want to run the program?'))
NEURONS = int(input('How many neurons would you like to use?'))
net = NeuralNetwork(7, NEURONS)
optimizer = optim.Adam(net.parameters(), lr=0.001)
poker = Poker()
start = time.time()
poker.new_game('human', 'bot')


def clear_output(output):
    _, index = torch.max(torch.abs(output), dim=0)
    return [1, 0] if index == 0 else [0, 1]


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
        outcome_all.append(outcome)
        if clear_output(outcome)[1] == 1:
            poker.folds("bot")
            break

    if len(outcome_all) != 4:
        print(f'Folded round: {len(outcome_all)}')
    else:
        print(f'Winner: {poker.winner()["winner"][0]}')

    for i in range(len(outcome_all)):
        if clear_output(outcome_all[i]) != clear_output(y[i]):
            loss = F.nll_loss(outcome_all[i], y[i])
            print(f'Loss: {loss}')
            loss.backward()
    optimizer.step()

# path = 'C:\\Code\\ChessAI\\neural_network\\training\\dummy.ph'
# path = "/home/hyde/Documents/PokerAI/pokerai/data/dummy.ph"
# torch.save(net.state_dict(), path)
end = time.time()
print("--- %s seconds ---" % (end - start))
