import csv
import os
import random

def display_card(card):
    max_chars = 0
    for keys in card:
        if len(keys) > max_chars:
            max_chars = len(keys)

    for keys in card:
        print(keys, (max_chars - len(keys)) * ' ', ':', card[keys])

def determine_winner(m1, m2, order = 1):
    dct = {'player': m1, 'computer': m2}
    v = list(dct.values())
    k = list(dct.keys())
    if m1 == m2:
        return 'draw'
    else:
        if order == 1:
            return k[v.index(max(v))]
        else:
            return k[v.index(min(v))]

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, '..', 'nba_top_trumps_players.csv')
csv_path = os.path.abspath(csv_path)

with open(csv_path, mode='r', newline='', encoding='utf-8-sig') as file:
    csvFile = csv.DictReader(file)
    all_cards = list(csvFile)

relevant_keys = list(all_cards[0].keys())[2:]

random.shuffle(all_cards)

computer_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []


mapping_dict = {}
for key in relevant_keys:
    k_lower = key.lower()
    if 'basket' in k_lower:
        mapping_dict['B'] = key
    elif 'height' in k_lower:
        mapping_dict['H'] = key
    elif 'experience' in k_lower or 'year' in k_lower:
        mapping_dict['Y'] = key
    elif 'troph' in k_lower:
        mapping_dict['T'] = key

chance = 'player'
game_over = False

while not game_over:
    if not player_cards or not computer_cards:
        print("Game Over! Out of cards.")
        break

    player = player_cards.pop(0)
    computer = computer_cards.pop(0)

    table_cards.append(player)
    table_cards.append(computer)

    print()
    print('Your card is ...')
    display_card(player)
    
    if chance == 'player':
        chosen_key = input('Choose a key to compare with computer (B, H, Y, T): ').strip().upper()
        while chosen_key not in mapping_dict:
            chosen_key = input('Invalid choice. Choose a valid key shortcut (B, H, Y, T): ').strip().upper()
        chance = 'computer'
    else:
        chosen_key = random.choice(list(mapping_dict.keys()))
        print(f"Computer chose key shortcut: {chosen_key}")
        chance = 'player'

    key_requested = mapping_dict[chosen_key]
    
    try:
        value_player = float(player[key_requested])
        value_computer = float(computer[key_requested])
    except ValueError:
        value_player = player[key_requested]
        value_computer = computer[key_requested]

    # All criteria (B, H, Y, T) use order = 1 (higher value wins)
    winner = determine_winner(value_player, value_computer, order=1)
    
    print('Key of interest is :', key_requested)
    print('Player', key_requested, 'is :', value_player)
    print('Computer', key_requested, 'is :', value_computer)
    print('Winner of this round:', winner)
    input('\nPress Enter to continue to the next round...')