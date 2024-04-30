#Shuffle cards
import random

def shuffle_cards(board, flipped):
    for sublist in board:
        random.shuffle(sublist)

#Reveal cards 
def reveal_cards(board, row, column):
    print("reveal cards")

#Flip cards
def flip_cards(board, row, column):
    print("reveal cards")

#Check matching cards
def match(board, flipped, row1, column1, row2, column2):
    print("check matching cards")

#Display cards on board
def display_cards(board, cards):
    print("display cards on board")


