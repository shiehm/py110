"""
Problem: Create the game of Twenty-One:
- Rules are like Blackjack 
- Except no splitting or doubling down 
- No betting in first iteration 
- Make the game single player for now, but optional to expand

Pseudocode: 
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
    - Ask player to hit or stay.
    - If stay, stop asking.
    - Repeat until bust, 21, or stay.
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - Repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.

Data Structure: 
- We could use a dictionary, a list of lists or tuples, or a list 
- I like the idea of a list of lists or tuples, since we can use 0 or 1 index 
- Tuples make more sense since the cards can't be changed 
"""

"""
Import needed modules
Initialize the deck and global variables
"""

# Import modules:
import random
import pdb

"""
Define functions here
"""

# Define functions here:
# Note: Will upgrade to multiple players later (max of 6 players 1 dealer)
def prompt(message):
    print(f'--> {message}')

def display_hands(players):
    prompt(f"Dealer: {players['Dealer'][0]} {HIDDEN_CARD * (len(players['Dealer']) - 1)}")
    
    for player in players:
        if player != 'Dealer':
            prompt(f'{player} Total Value: {total_value(players[player])}')
            prompt(f'{player}: {players[player]}')

def display_full_hands(players):
    for player in players:
        prompt(f'{player} Total Value: {total_value(players[player])}')
        prompt(f'{player}: {players[player]}')

# def alternate_player(current_player):
#     if current_player == 'Player':
#         return 'Dealer'
#     elif current_player == 'Dealer':
#         return 'Player'

def deal(players, deck):
    for player in players:
        while len(players[player]) < 2:
            hit(player, deck)

def hit(current_player, deck):
    card = random.choice(deck)
    players[current_player].append(card)
    deck.remove(card)

def bust(cards):
    return total_value(cards) > 21

def twenty_one(cards):
    return total_value(cards) == 21

def total_value(cards):
    values = [card[1] for card in cards]
    total_value = 0
    
    for value in values:
        if value in ['J', 'Q', 'K']:
            total_value += 10
        elif value == 'A':
            total_value += 11
        else:
            total_value += int(value)
    
    aces = values.count('A')
    while total_value > 21 and aces:
        total_value -= 10
        aces -= 1
    
    return total_value

def determine_winner(players):
    best_score = 0
    for player in players:
        score = total_value(players[player])
        if score > best_score and score <= 21:
            best_score = score

    winner = []
    for player in players:
        if total_value(players[player]) == best_score:
            winner.append(player)
    
    display_full_hands(players)

    if len(winner) > 1:
        prompt(f'Tie: {", ".join(winner)}')
    elif len(winner) == 0:
        prompt(f'Dealer Wins')
    else:
        prompt(f'{winner[0]} Wins')

"""
Define game loops here

For player:
1. Ask player to hit or stay
2. If stay stop asking
3. If hit, show total value of cards, your hand, and check:
    a. Did I bust?
    b. Did I get 21?
    c. If neither, repeat at step 1

For computer:
1. Always hit if total value is less than 17
2. Hit until value between 17-21 or bust
"""

def player_turn(players):
    
    cards = players['Player']
    
    while True:
        display_hands(players)
        
        if not twenty_one(cards):
            prompt('Hit or Stay?')
            decision = input().lower()
            
            if decision == 'stay':
                break
            elif decision == 'hit':
                hit('Player', deck)
            
        if bust(cards):
            prompt("You've busted!")
            break
        elif twenty_one(cards):
            prompt("You got 21!")
            break

def computer_turn(players):
    
    # Change this to take into account multiple players later
    if bust(players['Player']):
        return
        
    cards = players['Dealer']

    while total_value(cards) < 17:
        hit('Dealer', deck)

        if bust(cards):
            prompt("Dealer busted!")
            break
        elif twenty_one(cards):
            prompt("Dealer got 21!")
            break

def play_game():
    deal(players, deck)
    player_turn(players)
    computer_turn(players)
    determine_winner(players)

# Initialize the deck here:
suites = ['D', 'H', 'C', 'S']
cards = [num for num in range(2, 11)] + ['J', 'Q', 'K', 'A']
HIDDEN_CARD = ('X', 'X')

deck = list()
for suite in suites:
    for card in cards:
        deck.append(tuple((suite, card)))

# Initialize hands here: 
# Can turn players into objects later that way we can initialize multiple 
players = {
    'Dealer': [],
    'Player': []
}

# current_player = 'Player'

play_game()