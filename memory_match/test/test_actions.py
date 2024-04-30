import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memorymatch_folder.actions import display_cards, shuffle_cards, reveal_cards, flip_cards, match, display_cards, pick_card
from memorymatch_folder.board import print_board, new_board

def test_shuffle():
  print("Shuffle card")
  board = new_board()
  shuffling_cards = shuffle_cards(board)
  assert shuffling_cards == "shuffle cards" 

def test_reveal_cards():
  print("Reveal cards")
  board = new_board()
  reveal_cards(board, row, column, 0, 0)
  assert board[0][0] == cards[0]

def test_flip_cards():
  print("Flip cards")
  board = new_board()
  flip_cards(board, row, column, 0, 0)
  assert board[0][0] == cards[0]

def test_pick_card():
  print("Pick card")
  board = new_board()
  pick_card(board, row, column, 0, 0)
  assert board[0][0] == cards[0]

def test_match_cards():
  print("Match cards")
  board = new_board()
  match(board, row, column, 0, 0)
  assert board[0][0] == cards[0]

def test_display_card():
  print("Display card")
  board = new_board()
  display_card(board, row, column, 0, 0)
  assert board[0][0] == cards[0]    