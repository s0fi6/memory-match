#Shuffle cards
import random

def shuffle_cards(board):
    for sublist in board:
        random.shuffle(sublist)

board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
    ["DOG", "CAT", "GIRAFFE", "RACOON"],
    ["BEE", "PANDA", "FISH", "MONKEY"],
    ["BEE", "PANDA", "FISH", "MONKEY"]]
shuffle_cards(board)
print(board)

#Reveal cards 
def reveal_cards(board, row, column):
    print("reveal cards")

#Flip cards
def flip_cards(board, row, column):
    print("reveal cards")

#Pick card
def pick_card(board, reveal_cards):
    print("pick cards")

#Check matching cards
def match(board, row1, column1, row2, column2, row3, column3, row4, column4):
    print("check matching cards")

#Display cards on board
def display_cards(board, cards):
    print("display cards on board")


