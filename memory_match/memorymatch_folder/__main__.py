from board import new_board, print_board, all_cards, game_winner, game_over
from actions import display_cards, shuffle_cards, reveal_cards, flipp_cards, pick_card, match  

def main():
    rows = 4  # Example board size
    cols = 4  # Example board size
    board = new_board(rows, cols)

    print("Welcome to the Memory Match Game!")
    print_board(board)

 
with open('README.md', 'r') as f:
    print(f.read())

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

while True:
    command = input("Enter a command: ")
    if command == "Create board":
        rows = None
        columns=None
        board = new_board(rows, columns)
    elif command == "Display cards":
        board =None
        cards=None
        display_cards(board, cards)
    elif command == "Shuffle cards":
        board=None
        cards=None
        rows = None
        column=None
        shuffle_cards(board, cards, row, column)
    elif command == "Reveal cards":
        board = None
        row = None
        cards = None
        column = None
        reveal_cards(board, row, column)
    elif command == "Print current board":
        board = new_board()
        print_board(board)
    elif command == "Flipp cards":
        flipp_cards(board, row, column)
        board = None 
        row = None
        column = None
    elif command == "Pick cards":
        pick_card(board, reveal_cards)
        board = None
    elif command == "Check matcing cards":
        pick_card(board, row1, column1, row2, column2, row3, column3)
        board = None
        row1 = None
        column1 = None
        row2 = None
        column2 = None
        row3 = None
        column3 = None
    elif command == "All cards ready":
        all_cards(rows, columns)
        rows = None
        columns = None
    elif command == "Winner":
        game_winner(board, winner)
        winner = None
    elif command == "Game over":
        game_over(board, loser)
        loser = None
    else:
        print("I did not understand this command.")