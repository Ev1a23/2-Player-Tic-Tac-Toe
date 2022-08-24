from IPython.display import clear_output
def display_board(board):
    '''
    Function to display a board of tic tac toe
    '''
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    '''
    Function that assigns user1 and user2 marks as a tuple(user1,user2)
    '''
    user1_choice = " "
    options = ['X', 'O']
    while user1_choice not in options:
        user1_choice = input("Player 1, you want to be X or O? \n").upper()
        if (user1_choice) not in options:
            print("Incorrect input")

    if (user1_choice == 'X'):
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    '''
    Function that set user marker on a specifice position in the board
    '''
    board[position] = marker

def win_check(board, mark):
    '''
    Function to check if A mark of a user won the game on board
    '''
    return((board[1]==board[2]==board[3]==mark) or
           (board[4]==board[5]==board[6]==mark) or
           (board[7]==board[8]==board[9]==mark) or
           (board[1]==board[4]==board[7]==mark) or
           (board[2]==board[5]==board[8]==mark) or
           (board[3]==board[6]==board[9]==mark) or
           (board[1]==board[5]==board[9]==mark) or
           (board[3]==board[5]==board[7]==mark))

import random

def choose_first():
    '''
    Function to choose randomly who starts the game, Player 1 Or Player 2
    '''
    choice = random.randint(0,1)
    if(choice == 0 ):
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    '''
    Function to check if on the board, a position has a value yet
    '''
    return (board[position] == " ")


def full_board_check(board):
    '''
    Function to check if the board is full, to know if the game should ended as a drae
    '''
    return (" " not in board)


def player_choice(board):
    '''
    Function to take from the player a position he wants to mark on board, if it's free
    '''
    user1_choice = 0
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while user1_choice not in options or not space_check(board, user1_choice):
        user1_choice = int(input("Choose a position, between 1 and 9, 1 is Lower Left, 9 is Upper Right\n"))
    return user1_choice


def replay():
    '''
    Function to check if the player wants to play another game
    '''
    return input('Do you want to play again? Enter Yes or No: \n').lower() == "y"


#The Game Itself
print('Welcome to Tic Tac Toe!')
while True:
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]
    player1, player2 = player_input()
    turn = choose_first()
    print(f'{turn} Will go First')
    play_game = input("Are you ready to play? Enter Y or N\n")
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1, position)
            if (win_check(board, player1)):
                display_board(board)
                print("Player 1 Won!\n")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw\n")
                    break
                else:
                    turn = "Player 2"
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2, position)
            if (win_check(board, player2)):
                display_board(board)
                print("Player 2 Won!\n")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is draw\n")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        print("Thanks for playing!")
        break

