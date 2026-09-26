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

# --- Show numbered list and let only the player pick a favorite ---
name_key = list(all_cards[0].keys())[0]
print("--- NBA PLAYERS LIST ---")
for idx, card in enumerate(all_cards, start=1):
    print(f"{idx}. {card[name_key]}")

fav_num = int(input("\nPick your favorite player by number: "))
user_fav = all_cards[fav_num - 1][name_key]
print(f"Your favorite player: {user_fav}\n")

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

# Initialize scores
player_score = 0
computer_score = 0

# Ask user for game mode
game_mode = input("Do you want to play based on 'points' or till cards are 'over'? ").strip().lower()
target_points = 0
if game_mode == 'points':
    target_points = int(input("How many points do you want to play for? "))

while not game_over:
    if not player_cards or not computer_cards:
        print("\nGame Over! Out of cards.")
        print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
        break

    player = player_cards.pop(0)
    computer = computer_cards.pop(0)

    table_cards.append(player)
    table_cards.append(computer)

    # --- Check if your favorite card is drawn by anyone ---
    if player[name_key] == user_fav:
        print("\nYour card is ...")
        display_card(player)
        print(f"\n✨ Your favorite player ({user_fav}) appeared! YOU WIN! CONGRATULATIONS! ✨")
        break
    elif computer[name_key] == user_fav:
        print(f"\n✨ The computer drew your favorite player ({user_fav})! Computer wins! ✨")
        break
    

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

    winner = determine_winner(value_player, value_computer, order=1)
    
    # Update scores
    if winner == 'player':
        player_score += 1
    elif winner == 'computer':
        computer_score += 1

    print('Key of interest is :', key_requested)
    print('Player', key_requested, 'is :', value_player)
    print('Computer', key_requested, 'is :', value_computer)
    print('Winner of this round:', winner)
    
    print(f"----------------------------------------")
    print(f"Current Score -> You: {player_score} | Computer: {computer_score}")
    print(f"----------------------------------------")

    # Check if target points are reached
    if game_mode == 'points' and (player_score >= target_points or computer_score >= target_points):
        print("\n========================================")
        print("Target points reached! Game Over!")
        print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
        if player_score > computer_score:
            print("Congratulations, you won the match!")
        elif computer_score > player_score:
            print("Computer won the match!")
        else:
            print("It's a draw!")
        print("========================================")
        break

    input('\nPress Enter to continue to the next round...')