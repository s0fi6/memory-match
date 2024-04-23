from memorymatch_folder.board import new_board, print_board, all_cards, game_winner, game_over

def test_new_board():
    print("Testing new_board function...")
    board = new_board()
    assert len(board) == 4
    assert len(board[0]) == 4
    print("New board created successfully.")
    print()

def test_print_board():
    print("Testing print_board function...")
    board = [["DOG", "CAT", "GIRAFFE", "RACOON"],
             ["DOG", "CAT", "GIRAFFE", "RACOON"],
             ["BEE", "PANDA", "FISH", "MONKEY"],
             ["BEE", "PANDA", "FISH", "MONKEY"]]
    print("Printing the board:")
    print_board(board)
    print("Printed the board successfully.")
    print()



