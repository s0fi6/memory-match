#Create board 
from board import new_board



#Shuffle cards
from actions import shuffle_cards

#Reveal cards
from actions import reveal_cards

#Print current board
from board import print_board

#Flipp cards
from actions import flipp_cards



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
    user_input = print(input("Enter 'start' to begin the game or 'exit' to quit: "))
    if user_input == 'start':
        print("Starting the game...")
        break
    elif user_input == 'exit':
        print("Exiting the game...")
        
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

#Display cards
from actions import display_cards 
#Pick cards
print("Choose 2 cards: ")
from actions import pick_card 
