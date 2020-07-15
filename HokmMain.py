import random


def player_cards():
    card_suit = ['♠', '♥', '♦', '♣']
    p0_cards = []
    p1_cards = []
    p2_cards = []
    p3_cards = []
    rand051 = [*range(52)]
    random.shuffle(rand051)
    for n, I in enumerate(rand051):
        if n < 13:
            p0_cards.append(cards[I])
        elif 13 <= n < 26:
            p1_cards.append(cards[I])
        elif 26 <= n < 39:
            p2_cards.append(cards[I])
        elif 39 <= n < 52:
            p3_cards.append(cards[I])
        p0_cards = sorted(p0_cards, key=lambda item: (card_suit.index(item[1]), item[0]))
        p1_cards = sorted(p1_cards, key=lambda item: (card_suit.index(item[1]), item[0]))
        p2_cards = sorted(p2_cards, key=lambda item: (card_suit.index(item[1]), item[0]))
        p3_cards = sorted(p3_cards, key=lambda item: (card_suit.index(item[1]), item[0]))
    return p0_cards, p1_cards, p2_cards, p3_cards


def player_turns(winners, turns):
    while turns[-1] != winners:
        turns.insert(0, turns[-1])
        turns.pop()
    return turns
    #     2
    # 3       1
    #     0
    # be soorate saat gard micharkhad.
    # lis az enteha khande mishavad.
    # [1, 2, 3, 0] yani aval 0 bazi mikonad bad 3 bad 2 dar akhar 1


def what_is_hokm(hokm):
    suit_values = ['♣', '♦', '♥', '♠']
    suit_values.remove(hokm)
    suit_values.append(hokm)
    return suit_values


player_names = ['Sadjad', 'Ali', 'Haniye', 'Amir']

# initializing cards
cards = []
playing_card_suit = ['♣', '♦', '♥', '♠']
for j in playing_card_suit:
    for i in range(2, 15):
        cards.append([i, j])

a = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠'}
no_of_wins = [0, 0, 0, 0]
winner = 0
turn = [1, 2, 3, 0]
zamin = []
cart_haye_bazi_shode = []
hate_error = 0

cards_to_play = player_cards()
print('your cards = ', random.sample(cards_to_play[0], 5))
while hate_error == 0:
    try:
        Hokm = a[input('''hokm chie?
S: spades (♠), H: hearts (♥), D: diamonds (♦), C: clubs (♣)
(type: s, h, d or c)
>>> ''').upper()]
        break
    except KeyError:
        print('what did you say? 😕')

suit_value = what_is_hokm(Hokm)
values_list = sorted(cards, key=lambda item: (suit_value.index(item[1]), item[0]))

while (no_of_wins[0] + no_of_wins[2] < 7) and (no_of_wins[1] + no_of_wins[3] < 7):
    # let's play:
    for i in range(1, 5):
        #   nafare i'om:
        print('------------')
        print('nobate', player_names[turn[-i]])
        print(Hokm, 'Hokm', Hokm)
        print('zamin:', zamin)
        lst = list(enumerate(cards_to_play[turn[-i]]))
        spades = [item for item in lst if item[1][1] == playing_card_suit[3]]
        hearts = [item for item in lst if item[1][1] == playing_card_suit[2]]
        diamonds = [item for item in lst if item[1][1] == playing_card_suit[1]]
        clubs = [item for item in lst if item[1][1] == playing_card_suit[0]]
        print(spades)
        print(hearts)
        print(diamonds)
        print(clubs)
        #       kodoom kart ro bazi mikone:
        while hate_error == 0:
            try:
                played_card_index = int(input('''adade samte chape karti ke mikhay bazi koni ro vared kon\n>>> '''))
                print(cards_to_play[turn[-i]][played_card_index])
                break
            except (IndexError, ValueError):
                print('what did you say? 😕')
        if i == 1:
            khal = cards_to_play[turn[-i]][played_card_index][1]
            if khal != Hokm:
                suit_value.remove(khal)
                suit_value.insert(2, khal)
            values_list = sorted(values_list, key=lambda item: (suit_value.index(item[1]), item[0]))
        #           kart ro bezar zamin va az dastesh hazf kon:
        zamin.append(cards_to_play[turn[-i]][played_card_index])
        cards_to_play[turn[-i]].pop(played_card_index)

    # yaftane barande:
    most_value = 0
    for card in zamin:
        if values_list.index(card) > most_value:
            most_value = values_list.index(card)
            winner = turn[-(zamin.index(card) + 1)]
    turn = player_turns(winner, turn)
    print('zamin:', zamin)
    # amade beshim baraye daste bad:
    values_list = ([x for x in values_list if x not in zamin])
    cart_haye_bazi_shode += zamin
    zamin = []
    spades_bazishode = [item for item in cart_haye_bazi_shode if item[1] == playing_card_suit[3]]
    hearts_bazishode = [item for item in cart_haye_bazi_shode if item[1] == playing_card_suit[2]]
    diamonds_bazishode = [item for item in cart_haye_bazi_shode if item[1] == playing_card_suit[1]]
    clubs_bazishode = [item for item in cart_haye_bazi_shode if item[1] == playing_card_suit[0]]
    no_of_wins[winner] += 1
    # neveshtane etefaq haye in dast
    print('------------')
    print('barandeye in dast:', player_names[winner])
    print(player_names[0], '&', player_names[2], '=', no_of_wins[0] + no_of_wins[2])
    print(player_names[1], '&', player_names[3], '=', no_of_wins[1] + no_of_wins[3])
    print('♠ played:', sorted(spades_bazishode))
    print('♥ played: ', sorted(hearts_bazishode))
    print('♦ played:', sorted(diamonds_bazishode))
    print('♣ played:', sorted(clubs_bazishode))

# payane bazi taiine barande:
print('******')
if no_of_wins[0] + no_of_wins[2] > no_of_wins[1] + no_of_wins[3]:
    print(player_names[0], '&', player_names[2], 'won the game!')
else:
    print(player_names[1], '&', player_names[3], 'won the game!')
print('******')
