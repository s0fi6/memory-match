import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory_match.actions import shuffle_cards, flip_cards, match
from memory_match.board import print_board, new_board

def test_shuffle(): #ASSERT = please make sure that
  print("Testing shuffle card")
  board, flipped = new_board()
  shuffled_board = shuffle_cards(board, flipped)
  print("Shuffled board:")
  print_board(shuffled_board)
  print("Expected: Shuffled board")
  print("Actual:", shuffled_board)
  assert 
  #Is the first card still the same? 

def test_flip_cards():
  print("Testing flip cards")
  flipped  = new_board()
  flip_cards(flipped, 0, 0)
  assert flipped[0][0] == True 

def test_match_cards():
  print("Testing match cards")
  board, flipped = new_board()
  result = match(board, flipped, 0, 0, 1, 0)
  assert result == True
