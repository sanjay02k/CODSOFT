import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def winner(b, player):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in combos:
        if all(b[i] == player for i in combo):
            return True
    return False

def empty_cells():
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(is_max):
    if winner(board, "O"):
        return 1

    if winner(board, "X"):
        return -1

    if not empty_cells():
        return 0

    if is_max:
        best = -math.inf
        for move in empty_cells():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best = max(score, best)
        return best
    else:
        best = math.inf
        for move in empty_cells():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best = min(score, best)
        return best

def ai_move():
    best_score = -math.inf
    move = None

    for spot in empty_cells():
        board[spot] = "O"
        score = minimax(False)
        board[spot] = " "

        if score > best_score:
            best_score = score
            move = spot

    board[move] = "O"

print("🎮 Tic Tac Toe")
print("You = X")
print("AI = O")

while True:

    print_board()

    pos = int(input("Enter position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = "X"
    else:
        print("Invalid move")
        continue

    if winner(board, "X"):
        print_board()
        print("You Win!")
        break

    if not empty_cells():
        print_board()
        print("Draw!")
        break

    ai_move()

    if winner(board, "O"):
        print_board()
        print("AI Wins!")
        break

    if not empty_cells():
        print_board()
        print("Draw!")
        break