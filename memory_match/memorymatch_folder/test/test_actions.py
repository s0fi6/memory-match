import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from actions import shuffle_cards, reveal_cards

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
    reveal_cards([[" ", " ", " ", " "],
                  [" ", " ", " ", " "],
                  [" ", " ", " ", " "],
                  [" ", " ", " ", " "]], 2, 3)
    
    # Test case 2: Reveal a card at row 0, column 0
    print("\nTest Case 2:")
    print("Expected Output: reveal cards")
    reveal_cards([[" ", " ", " ", " "],
                  [" ", " ", " ", " "],
                  [" ", " ", " ", " "],
                  [" ", " ", " ", " "]], 0, 0)

# Run the test cases
test_reveal_cards()