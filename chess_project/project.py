def create_board():
 board = [
    ['.', '.', '.', 'k', '.', '.', '.', '.'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['.', '.', '.', 'K', '.', '.', '.', '.']
 ]
 return board

def print_board(board):
 for row in board:
    print(''.join(row))
 print()

def move(board, start_row, start_col, end_row, end_col):
  piece = board[start_row][start_col]
  board[start_row][start_col] = '.'
  board[end_row][end_col] = piece

if __name__ == "__main__":
    board = create_board()
    move(board, 6, 0, 4, 0)
    print_board(board)

