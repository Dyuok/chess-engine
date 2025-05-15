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

def move(board, start_row, start_col, end_row, end_col,):
  direction = -1 if board[start_row][start_col].isupper() else 1
  piece = board[start_row][start_col]
  if board[start_row][start_col].lower() == 'p' and board[end_row][end_col] == '.' and start_col != end_col:
    board[end_row - direction][end_col] = '.'
  board[start_row][start_col] = '.'
  board[end_row][end_col] = piece

def is_valid_move(board, start_row, start_col, end_row, end_col, turn, en_passant_target):
    piece = board[start_row][start_col]
    target = board[end_row][end_col]
    dr = end_row - start_row
    dc = end_col - start_col
    direction = -1 if piece.isupper() else 1  # white up, black down
    start_rank = 6 if piece == 'P' else 1
    
    temp_board = [row[:] for row in board]
    move(temp_board, start_row, start_col, end_row, end_col)
    if is_in_check(temp_board, turn):
      return False
   

    if piece.lower() == 'p':
        # Move forward
        if dc == 0 and dr == direction and target == '.':
            return True
        # Two-step forward
        if dc == 0 and dr == 2 * direction and start_row == start_rank:
            if board[start_row + direction][start_col] == '.' and target == '.':
               return True
        # Capture
        if abs(dc) == 1 and dr == direction and target != '.' and target.isupper() != piece.isupper():
            return True
        # En passant capture
        if abs(dc) == 1 and dr == direction and (end_row, end_col) == en_passant_target:
            return True

    elif piece.lower() == 'k':
        if abs(dr) <= 1 and abs(dc) <= 1:
            if target == '.' or target.isupper() != piece.isupper():
                if not is_square_attacked(board, end_row, end_col, turn):
                  return True

    return False

def is_square_attacked(board, row, col, turn):
   direction = -1 if turn == 'b' else 1
   pawn = 'P' if turn == 'b' else 'p'
   for dc in [-1, 1]:
        r, c = row + direction, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == pawn:
            return True
   enemy_king = 'K' if turn == 'b' else 'k'
   for dr in [-1, 0, 1]:
      for dc in [-1, 0, 1]:
         if dr == 0 and dc == 0:
            continue
         r, c = row + dr, col + dc
         if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == enemy_king:
            return True
   return False     
   
def find_king(board, turn):
    king = 'K' if turn == 'w' else 'k'
    for r in range(8):
        for c in range(8):
            if board[r][c] == king:
                return r, c
    return None

def is_in_check(board, turn):
    king_pos = find_king(board, turn)
    if not king_pos:
        return False
    return is_square_attacked(board, *king_pos, turn)

if __name__ == "__main__":
   board = create_board()
   en_passant_target = None
   turn = 'w'
   while True:
        print_board(board)
        print(f"{'White' if turn == 'w' else 'Black'} to move.")

        try:
            move_input = input("Enter move (e.g., 'e2 e4'): ")
            print(f"Raw input: '{move_input}'")
            start_pos, end_pos = move_input.strip().split()
            start_col = ord(start_pos[0].lower()) - ord('a')
            start_row = 8 - int(start_pos[1])
            end_col = ord(end_pos[0].lower()) - ord('a')
            end_row = 8 - int(end_pos[1])
        except ValueError:
            print("Invalid input format.")
            continue
        

        piece = board[start_row][start_col]
        if piece == '.' or (turn == 'w' and piece.islower()) or (turn == 'b' and piece.isupper()):
            print("Invalid piece selection.")
            continue
        
        if not is_valid_move(board, start_row, start_col, end_row, end_col, turn, en_passant_target):
         print("Illegal move.")
         continue

        move(board, start_row, start_col, end_row, end_col)

        if piece.lower() == 'p' and abs(end_row - start_row) == 2:
         direction = -1 if piece.isupper() else 1
         en_passant_target = (start_row + direction, start_col)
        else:
         en_passant_target = None

        turn = 'b' if turn == 'w' else 'w'

