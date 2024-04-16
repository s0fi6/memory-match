#Create board 
from board import new_board

#Display cards
from actions import display_cards

#Shuffle cards
from actions import shuffle_cards

#Reveal cards
from actions import reveal_cards

#Print current board
from board import print_board

#Flipp cards
from actions import flipp_cards

#Pick cards
from actions import pick_card 

#Check matching cards
from actions import pick_card

#All cards ready
from board import all_cards

#Winner
from board import game_winner

#Game over
from board import game_over

#Instructions 



#Game Loop
while True:
    user_input = input("Enter 'start' to begin the game or 'exit' to quit: ")
    if user_input == 'start':
        print("Starting the game...")
        break
    elif user_input == 'exit':
        print("Exiting the game...")
        exit()
    else:
        print("Invalid input. Please enter 'start' or 'exit'.")

#Empty board onscreen
from board import new_board, print_board

def main():
    rows = 4  # Example board size
    cols = 4  # Example board size
    board = new_board(rows, cols)

    print("Welcome to the Memory Match Game!")
    print_board(board)

 
with open('README.md', 'r') as f:
    print(f.read())

while True:
    command = input("Enter a command: ")
    if command == "Create board":
        new_board(rows, columns)
    elif command == "Display cards":
        display_cards(board, cards)
    elif command == "Shuffle cards":
        shuffle_cards(board, cards, row, column)
    elif command == "Reveal cards":
        board = None
        row = None
        cards = None
        column = None
        reveal_cards(board, row, column)
    elif command == "Print current board":
        print_board(board)
    elif command == "Flipp cards":
        flipp_cards(board, row, column)
    elif command == "Pick cards":
        pick_card(board, reveal_cards)
    elif command == "Check matcing cards":
        pick_card(board, row1, column1, row2, column2, row3, column3)
    elif command == "All cards ready":
        all_cards(rows, columns)
    elif command == "Winner":
        game_winner(board, winner)
    elif command == "Game over":
        game_over(board, loser)
    else:
        print("I did not understand this command.")