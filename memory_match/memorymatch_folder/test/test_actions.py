import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from actions import display_cards, shuffle_cards, reveal_cards, flip_cards, match, display_cards
from board import print_board
def test_shuffle_cards():
    
    sample_board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
             ["DOG", "CAT", "GIRAFFE", "RACOON"],
             ["BEE", "PANDA", "FISH", "MONKEY"],
             ["BEE", "PANDA", "FISH", "MONKEY"]]
    
    sample_cards = ["DOG", "BEE", "CAT", "PANDA", "FISH", "GIRAFFE", "RACOON", "MONKEY"]

    print("Testing shuffle cards function:")
    shuffle_cards(sample_board, sample_cards)
test_shuffle_cards()

def test_reveal_cards():
    print("Testing reveal cards function:")
    
    # Test case 1: Reveal a card at row 2, column 3
    print("\nTest Case 1:")
    print("Expected Output: reveal cards")
    reveal_cards([["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["BEE", "PANDA", "FISH", "MONKEY"],
                    ["BEE", "PANDA", "FISH", "MONKEY"]], 2, 3)
    
    # Test case 2: Reveal a card at row 0, column 0
    print("\nTest Case 2:")
    print("Expected Output: reveal cards")
    reveal_cards([["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["BEE", "PANDA", "FISH", "MONKEY"],
                    ["BEE", "PANDA", "FISH", "MONKEY"]], 0, 0)


test_reveal_cards()


def test_flip_cards():
    sample_board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["BEE", "PANDA", "FISH", "MONKEY"],
                    ["BEE", "PANDA", "FISH", "MONKEY"]]
    
    print("Testing flip cards function:")
    # Test code to flip a card at row=1, column=1
    print("Initial board:")
    print_board(sample_board)
    print("Flipping card at row=1, column=1:")
    flip_cards(sample_board, 1, 1)
    print("Updated board:")
    print_board(sample_board)

test_flip_cards()

def test_pick_card():
    sample_board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["BEE", "PANDA", "FISH", "MONKEY"],
                    ["BEE", "PANDA", "FISH", "MONKEY"]]
    
    print("Testing pick card function:")
    # Test code to pick a card at row=1, column=1
    print("Initial board:")
    print_board(sample_board)
    print("picking card at row=1, column=1:")
    flip_cards(sample_board, 1, 1)
    print("Updated board:")
    print_board(sample_board)

test_pick_card()

def test_match():

    sample_board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["BEE", "PANDA", "FISH", "MONKEY"],
                    ["BEE", "PANDA", "FISH", "MONKEY"]]

    print("Testing match function:")
    
    #Matching cards
    print("Test 1: Matching cards")
    match(sample_board, 0, 0, 1, 0, 0, 1)
    
    #Non-matching cards
    print("Test 2: Non-matching cards")
    match(sample_board, 0, 0, 1, 0, 0, 2)

test_match()

def test_display_card():

    sample_board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["DOG", "CAT", "GIRAFFE", "RACOON"],
                    ["BEE", "PANDA", "FISH", "MONKEY"],
                    ["BEE", "PANDA", "FISH", "MONKEY"]]
    sample_cards = ["DOG", "CAT", "GIRAFFE", "RACOON", "BEE", "PANDA", "FISH", "MONKEY"]

    print("Testing display cards function:")
    display_cards(sample_board, sample_cards)

test_display_card()
    
       