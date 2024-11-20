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

# Import modules:
import random

# Global variables:
suites = ['D', 'H', 'C', 'S']
cards = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
HIDDEN_CARD = ('X', 'X')

# Define functions here:
def prompt(message):
    """Adds and arrow --> to signify game prompts"""
    print(f'--> {message}')

def display_hands(players):
    """Keeps dealer hand hidden except for one face-up card"""
    prompt(f"Dealer: {players['Dealer'][0]} {HIDDEN_CARD * (len(players['Dealer']) - 1)}")
    for player in players:
        if player != 'Dealer':
            prompt(f'{player} Total Value: {total_value(players[player])}')
            prompt(f'{player}: {players[player]}')

def display_full_hands(players):
    """Used after determining winner, to show all hands"""
    for player in players:
        prompt(f'{player} Total Value: {total_value(players[player])}')
        prompt(f'{player}: {players[player]}')

def deal(players, deck):
    """Only used for the initial deal"""
    for player in players:
        while len(players[player]) < 2:
            hit(players, player, deck)

def hit(players, current_player, deck):
    """Used for both player and computer turns"""
    card = random.choice(deck)
    players[current_player].append(card)
    deck.remove(card)

def bust(hand):
    """Returns True if value over 21"""
    return total_value(hand) > 21

def twenty_one(hand):
    """Returns True if value is 21"""
    return total_value(hand) == 21

def total_value(hand):
    """Calculates total value of a hand, taking into account aces"""
    values = [card[1] for card in hand]
    total = 0
    for value in values:
        if value in ['J', 'Q', 'K']:
            total += 10
        elif value == 'A':
            total += 11
        else:
            total += int(value)
    
    aces = values.count('A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    
    return total

def determine_winner(players):
    """
    Used after all moves have been made.
    First calculates best score <= 21, then finds players matching that score. 
    Prints a messages and displays all hands. 
    """
    best_score = 0
    for player in players:
        score = total_value(players[player])
        if best_score < score <= 21:
            best_score = score

    winner = []
    for player in players:
        if total_value(players[player]) == best_score:
            winner.append(player)
    
    display_full_hands(players)

    if len(winner) > 1:
        prompt(f'Tie: {", ".join(winner)}')
    elif len(winner) == 0:
        prompt('Dealer Wins')
    else:
        prompt(f'{winner[0]} Wins')

def player_turn(players, deck):
    """
    For player game loop:
    1. Ask player to hit or stay
    2. If stay stop asking
    3. If hit, show total value of cards, your hand, and check:
        a. Did I bust?
        b. Did I get 21?
        c. If neither, repeat at step 1
    """
    hand = players['Player']
    while True:
        display_hands(players)
        
        if not twenty_one(hand):
            prompt('Hit or Stay?')
            decision = input().lower()
        
            if decision == 'hit':
                hit(players, 'Player', deck)
            elif decision == 'stay':
                break
        
        if bust(hand):
            prompt("You've busted!")
            break
        if twenty_one(hand):
            prompt("You got 21!")
            break

def computer_turn(players, deck):
    """
    For computer game loop:
    1. Always hit if total value is less than 17
    2. Hit until value between 17-21 or bust
    """
    if bust(players['Player']):
        return
    
    hand = players['Dealer']
    while total_value(hand) < 17:
        hit(players, 'Dealer', deck)
        
        if bust(hand):
            prompt("Dealer busted!")
            break
        if twenty_one(hand):
            prompt("Dealer got 21!")
            break

def play_game():
    """
    Initiates the deck contained in a list. Cards are tuples.
    Initiates players (player and dealer) in a dictionary. Values are hands.
    Currently only supports single player. Can expand to multi-player. 
    """
    while True:
        deck = []
        for suite in suites:
            for card in cards:
                deck.append(tuple((suite, card)))
        
        players = {
            'Dealer': [],
            'Player': []
        }
        
        deal(players, deck)
        player_turn(players, deck)
        computer_turn(players, deck)
        determine_winner(players)
        
        prompt('Play again? Yes or No?')
        again = input()
        if again[0].lower() == 'n':
            break

play_game()
