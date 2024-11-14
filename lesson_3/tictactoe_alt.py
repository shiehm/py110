"""
Proceedure for Tic-Tac-Toe Game:

1. Display the initial empty 3x3 board.
2. Ask the user to mark a square.
3. Computer marks a square.
4. Display the updated board state.
5. If it's a winning board, display the winner.
6. If the board is full, display tie.
7. If neither player won and the board is not full, go to #2
8. Play again?
9. If yes, go to #1

"""

import os
import random

INITIAL_MARK = ' '
HUMAN_MARK = 'X'
CPU_MARK = 'O'
WINS_REQUIRED = 5

WINNING_COMBOS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

"""
Necessary functions
"""

def initialize_board():
    return {num: INITIAL_MARK for num in range(1, 10)}

def display_board(board):
    os.system('clear')
    
    prompt(f'You are {HUMAN_MARK}. Computer is {CPU_MARK}.')
    print('')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('---+---+---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('---+---+---')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('')

def prompt(message):
    print(f'--> {message}')

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARK]

def identify_risk(line, board):
    marks = [board[square] for square in line]
    if marks.count(HUMAN_MARK) == 2:
        for square in line:
            if board[square] == INITIAL_MARK:
                return square
    return None

def identify_win(line, board):
    marks = [board[square] for square in line]
    if marks.count(CPU_MARK) == 2:
        for square in line:
            if board[square] == INITIAL_MARK:
                return square
    return None

def user_choice(board):
    valid_moves = empty_squares(board)
    
    while True:
        prompt(f'Choose a square from: {join_or([str(key) for key in valid_moves])}')
        user_move = input()
        if user_move in [str(square) for square in valid_moves]:
            break
        prompt('Not a valid choice.')
    
    board[int(user_move)] = HUMAN_MARK

def computer_choice(board):
    if len(empty_squares(board)) == 0:
        return None
    
    # Need separate loops otherwise it will take a defense if available
    square = None
    for line in WINNING_COMBOS:
        square = identify_win(line, board)
        if square:
            break
        
    if not square:
        for line in WINNING_COMBOS:
            square = identify_risk(line, board)
            if square:
                break
    
    if not square:
        if board[5] == INITIAL_MARK:
            square = 5
        else:
            square = random.choice(empty_squares(board))
    
    board[square] = CPU_MARK

def determine_winner(board):
    for line in WINNING_COMBOS:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARK and board[sq2] == HUMAN_MARK and board[sq3] == HUMAN_MARK):
            return 'Player'
        elif (board[sq1] == CPU_MARK and board[sq2] == CPU_MARK and board[sq3] == CPU_MARK):
            return 'Computer'
    
    return None

def board_full(board):
    return len(empty_squares(board)) == 0

"""
Additional Features
"""

def join_or(lst, sep=', ', last='or'):
    string = ''
    for i in range(len(lst)):
        string += str(lst[i])
        if i == len(lst) - 2:
            string += sep + last + ' '
        elif i != len(lst) - 1:
            string += sep
    return string

def choose_square(board, current_player):
    while True:
        display_board(board)
    
        if current_player == 'Player':
            user_choice(board)
            display_board(board)
            if board_full(board) or determine_winner(board):
                break
            
            computer_choice(board)
            display_board(board)
            if board_full(board) or determine_winner(board):
                break
        
        elif current_player == 'Computer':
            computer_choice(board)
            display_board(board)
            if board_full(board) or determine_winner(board):
                break
            
            user_choice(board)
            display_board(board)
            if board_full(board) or determine_winner(board):
                break

def alternate_player(current_player):
    if current_player == 'Player':
        return 'Computer'
    elif current_player == 'Computer':
        return 'Player'

"""
Main game function
"""

def play_game():
    
    score = {
        'Player': 0,
        'Computer': 0
    }
    
    while True:
        board = initialize_board()
        
        prompt('Who plays first? (H = Human, C = Computer, R = Random): ')
        first = input()
        
        while first == '' or first[0].lower() not in ['h', 'c', 'r']:
            prompt('Please select H for human, C for computer, or R for random.')
            first = input()
        
        if first[0].lower() == 'h':
            current_player = 'Player'
        elif first[0].lower() == 'c':
            current_player = 'Computer'
        elif first[0].lower() == 'r':
            current_player = random.choice(['Player', 'Computer'])
        
        while True:
            choose_square(board, current_player)
            current_player = alternate_player(current_player)
            if determine_winner(board) or board_full(board):
                break
        
        if determine_winner(board):
            prompt(f'{determine_winner(board)} has won!')
            score[determine_winner(board)] += 1
        else:
            prompt('It\'s a tie!')
        
        prompt(score)
        if score['Player'] == WINS_REQUIRED:
            prompt(f'Player has won {score["Player"]}/{WINS_REQUIRED} games!')
            break
        elif score['Computer'] == WINS_REQUIRED:
            prompt(f'Computer has won {score["Computer"]}/{WINS_REQUIRED} games!')
            break
        
        prompt('Play again? (y or n)')
        answer = input()
        
        while answer == '' or answer[0].lower() not in ['y', 'n']:
            prompt('Please type Y for y or N for no')
            answer = input()
        
        if answer[0].lower() == 'n':
            break
    
    prompt('Thanks for playing!')

play_game()