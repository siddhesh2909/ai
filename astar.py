from random import choice

def checkWin(board, player):
    for i in range(0, 7, 3):
        if board[i] == player and board[i+1] == player and board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False

def checkTie(board):
    return all(cell != " " for cell in board)

def getAIMove(board, currentPlayer, aiPlayer):
    opponent = "O" if aiPlayer == "X" else "X"

    if checkWin(board, aiPlayer):
        return (-1, 10)
    if checkWin(board, opponent):
        return (-1, -10)
    if checkTie(board):
        return (-1, 0)

    moves = []

    for i in range(len(board)):
        if board[i] == " ":
            board[i] = currentPlayer
            score = getAIMove(board, "X" if currentPlayer == "O" else "O", aiPlayer)[1]
            moves.append((i, score))
            board[i] = " "

    if currentPlayer == aiPlayer:
        best = max(moves, key=lambda x: x[1])
    else:
        best = min(moves, key=lambda x: x[1])
    return best

def printBoard(board):
    print("\nBoard:")
    for i in range(9):
        print(board[i] if board[i] != " " else "_", end=" ")
        if (i + 1) % 3 == 0:
            print()
    print()

def main():
    board = [" " for _ in range(9)]
    human = input("Choose your symbol (X/O): ").upper()
    while human not in ["X", "O"]:
        human = input("Invalid. Choose X or O: ").upper()

    ai = "O" if human == "X" else "X"
    turn = choice(["human", "ai"])
    print(f"{turn.capitalize()} goes first.")

    while True:
        printBoard(board)

        if checkWin(board, human):
            print("You win!")
            break
        if checkWin(board, ai):
            print("AI wins!")
            break
        if checkTie(board):
            print("It's a tie!")
            break

        if turn == "human":
            move = int(input("Enter your move (0-8): "))
            while move < 0 or move > 8 or board[move] != " ":
                move = int(input("Invalid move. Try again (0-8): "))
            board[move] = human
            turn = "ai"
        else:
            print("AI is thinking...")
            move, _ = getAIMove(board, ai, ai)
            board[move] = ai
            turn = "human"

if __name__ == "__main__":
    main()
