import math

# Initialize the board as a list of 9 empty spaces
board = [' ' for _ in range(9)]

def print_board():
    """Renders the current game board to the console."""
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(b, p):
    """Checks if player 'p' has won the game."""
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    return any(all(b[i] == p for i in state) for state in win_states)

def get_empty_cells(b):
    """Returns a list of indices for available moves."""
    return [i for i, x in enumerate(b) if x == ' ']

def minimax(b, depth, is_maximizing):
    """The Minimax algorithm to find the best possible move."""
    if check_winner(b, 'O'): return 1   # AI Wins
    if check_winner(b, 'X'): return -1  # Human Wins
    if ' ' not in b: return 0           # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in get_empty_cells(b):
            b[i] = 'O'
            score = minimax(b, depth + 1, False)
            b[i] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in get_empty_cells(b):
            b[i] = 'X'
            score = minimax(b, depth + 1, True)
            b[i] = ' '
            best_score = min(score, best_score)
        return best_score

def ai_move():
    """Determines the best move for the AI using Minimax."""
    best_score = -math.inf
    move = 0
    for i in get_empty_cells(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    board[move] = 'O'

def play_game():
    """Main game loop."""
    print("Welcome to Tic Tac Toe! You are 'X', AI is 'O'.")
    print_board()
    
    while ' ' in board:
        try:
            move = int(input("Enter move (1-9): ")) - 1
            if board[move] != ' ':
                print("Space occupied!")
                continue
            board[move] = 'X'
        except (ValueError, IndexError):
            print("Invalid input!")
            continue

        if check_winner(board, 'X'):
            print_board()
            print("You won!")
            return

        if ' ' in board:
            ai_move()
            print_board()
            if check_winner(board, 'O'):
                print("AI won!")
                return
        else:
            break
            
    print("It's a draw!")

if __name__ == "__main__":
    play_game()