#Create new board
def new_board():
    board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
        ["DOG", "CAT", "GIRAFFE", "RACOON"],
        ["BEE", "PANDA", "FISH", "MONKEY"],
        ["BEE", "PANDA", "FISH", "MONKEY"]]
    flipped = [[False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False]]
    return board, flipped

#Print current board
def print_board(board):
    print(
        f"""
 {board[0][0]} |  {board[0][1]} |  {board[0][2]} |  {board[0][3]} 
 ------------------
 {board[1][0]} |  {board[1][1]} |  {board[1][2]} |  {board[1][3]} 
 ------------------
 {board[2][0]} |  {board[2][1]} |  {board[2][2]} |  {board[2][3]} 
 ------------------
 {board[3][0]} |  {board[3][1]} |  {board[3][2]} |  {board[3][3]} 
 """
     )

#All cards ready
def all_cards(rows, columns):
    print("All cards ready")

#Winner
def game_winner(board, word_winner):
    print("Winner")

#Game over
def game_over(board, word_loser):
    print("Game over")