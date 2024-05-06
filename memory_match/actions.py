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
    card1 = board[row1][column1]
    card2 = board[row2][column2]
    if card1 == card2:
        return True
    else:
        return False



