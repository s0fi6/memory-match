import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory_match.actions import shuffle_cards, flip_cards, match
from memory_match.board import print_board, new_board

def test_shuffle():
  print("Testing shuffle card")
  board, flipped = new_board()
  shuffled_board = shuffle_cards(board, flipped)
  print("Shuffled board:")
  print_board(shuffled_board)
  print("Expected: Shuffled board")
  print("Actual:", shuffled_board)

def test_flip_cards():
  print("Testing flip cards")
  board, flipped  = new_board()
  flipped_cards = flip_cards(board, flipped, 0, 0)
  assert flipped_cards[0][0] == " "  

def test_match_cards():
  print("Testing match cards")
  board, flipped = new_board()
  result = match(board, flipped, 0, 0, 1, 0)
  assert result == True
