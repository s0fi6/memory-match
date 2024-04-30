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
def print_board(board, flipped):
    print(
        f"""
 {board[0][0] if flipped[0][0] else "****"} |  {board[0][1] if flipped[0][1] else "****"} |  {board[0][2] if flipped[0][2] else "****"} |  {board[0][3] if flipped[0][3] else "****"} 
 ------------------
 {board[1][0] if flipped[1][0] else "****"} |  {board[1][1] if flipped[1][1] else "****"} |  {board[1][2] if flipped[1][2] else "****"} |  {board[1][3] if flipped[1][3] else "****"} 
 ------------------
 {board[2][0] if flipped[2][0] else "****"} |  {board[2][1] if flipped[2][1] else "****"} |  {board[2][2] if flipped[2][2] else "****"} |  {board[2][3] if flipped[2][3] else "****"} 
 ------------------
 {board[3][0] if flipped[3][0] else "****"} |  {board[3][1] if flipped[3][1] else "****"} |  {board[3][2] if flipped[3][2] else "****"} |  {board[3][3] if flipped[3][3] else "****"} 
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
