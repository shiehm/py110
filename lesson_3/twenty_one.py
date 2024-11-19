"""
Problem: Create the game of Twenty-One:
- Rules are like Blackjack 
- Except no splitting or doubling down 
- No betting in first iteration 

Pseudocode: 
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
    - Ask player to hit or stay.
    - If stay, stop asking.
    - Repeat until bust or stay.
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - Repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.

Notes:
- 

Data Structure: 
- We could use a dictionary, a list of lists or tuples, or a list 
- I like the idea of a list of lists or tuples, since we can use 0 or 1 index 
- Tuples make more sense since the cards can't be changed 
- We also need a dictionary for values too, 

"""

"""
Import needed modules
Initialize the deck and global variables
"""

import random

# Initialize the deck here:
suites = ['D', 'H', 'C', 'S']
cards = [num for num in range(2, 11)] + ['J', 'Q', 'K', 'A']

deck = list()
for suite in suites:
    for card in cards:
        deck.append(tuple((suite, card)))

HIDDEN_CARD = ('X', 'X')

# Initialize hands here 
# Can turn players into objects later that way we can initialize multiple 
players = {
    'dealer': [],
    'player': []
}

current_player = 'player'

"""
Define functions here
"""

# Define functions here:
# Note: Will upgrade to multiple players later (max of 6 players 1 dealer)
def prompt(message):
    print(f'--> {message}')

def display_hands(players):
    for player in players:
        if player == 'dealer':
            prompt(f'Dealer: {players[player][0]} {HIDDEN_CARD * (len(players[player]) - 1)}')
        else:
            prompt(f'{player}: {players[player]}')

def display_full_hands(players):
    for player in players:
        prompt(f'{player}: {players[player]}')

def alternate_player(current_player):
    if current_player == 'player':
        return 'dealer'
    elif current_player == 'dealer':
        return 'player'

def deal(players, deck):
    for player in players:
        while len(players[player]) < 2:
            hit(player, deck)

def hit(current_player, deck):
    card = random.choice(deck)
    players[current_player].append(card)
    deck.remove(card)

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
    
    aces = cards.count('A')
    while total_value > 21 and aces:
        total_value -= 10
        aces -= 1
    
    return total_value

def bust(cards):
    return total_value(cards) > 21

def twenty_one(cards):
    return total_value(cards) == 21

def determine_winner(players):
    best_score = 0
    for player in players:
        score = total_value(players[player])
        if score > best_score and score <= 21:
            best_score = score

    winner = []
    for player in players:
        if players[player] == score:
            winner.append(player)

    if len(winner) > 1:
        return f'Tie: {", ".join(winner)}'
    elif len(winner) == 0:
        return f'Dealer Wins'
    else:
        return winner[0]

"""
Define game loops here
"""

def player_turn():
    
    cards = players["player"]
    
    while True:
        display_hands(players)
        prompt('Hit or Stay?')
        decision = input().lower()
        
        if decision == 'stay':
            break
        elif decision == 'hit':
            hit('player', deck)
            
        prompt(f'Total Value Player: {total_value(cards)}')
        
        if bust(cards):
            
            break
        elif twenty_one(cards):
            break