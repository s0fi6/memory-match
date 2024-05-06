from board import new_board, print_board
from actions import shuffle_cards, match  

def main():
    rows = 4
    cols = 4  
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

board, flipped = new_board()        
while True:
    
    print_board(board, flipped)
    command = input("Enter a command: ")

    if command == "Shuffle cards":
        shuffle_cards(board, flipped)
   
    elif command == "Match": 
        row1 = int(input("Enter the first card's row number: "))
        column1 = int(input("Enter the first card's column number: "))
        row2 = int(input("Enter the second card's row number: "))
        column2 = int(input("Enter the second card's column number: "))
        matched = match(board, flipped, row1, column1, row2, column2)
        if matched:
            print("Cards match!")
            flipped[row1][column1] = True
            flipped[row2][column2] = True
        else:
            print("Cards don't match!")
            print("First card:", board[row1][column1])
            print("Second card:", board[row2][column2])

    elif command == 'exit':
     print("Exiting the game...")
     exit()
    
    else:
     print("I did not understand this command. Please try again.")