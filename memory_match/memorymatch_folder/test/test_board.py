import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from board import new_board, print_board, all_cards, game_winner, game_over

def test_new_board():
    print("Testing new_board function...")
    board = new_board()
    assert len(board) == 4
    assert len(board[0]) == 4
    print("New board created successfully.")
    print()

def test_print_board():
    print("Testing print_board function...")
    board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
             ["DOG", "CAT", "GIRAFFE", "RACOON"],
             ["BEE", "PANDA", "FISH", "MONKEY"],
             ["BEE", "PANDA", "FISH", "MONKEY"]]
    print("Printing the board:")
    print_board(board)
    print("Printed the board successfully.")
    print()

def test_all_cards():
    print("Preparing cards:".format(rows, columns))
    total_pairs = (rows*columns)//2
    print("Total pairs of cards to prepare:", total_pairs)
   
rows = 4
columns = 4
print("Starting a new memory match game...")

all_cards(rows, columns)

def test_winner():

    def all_cards_matched(board):
        return all(card == "matched" for row in board for card in row)
    
    board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["BEE", "PANDA", "FISH", "MONKEY"],
                    ["BEE", "PANDA", "FISH", "MONKEY"]]

    if all_cards_matched(board): 
        print("All cards matched!")
        print("WINNER")

test_winner()