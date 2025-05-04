import time


def print_solution(board):
    for row in board:
        print(row)
    print("\n")


# Utility function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col, n):
    # Check for queen in this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check for queen in upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for queen in lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# Backtracking function to solve n-queens
def solve_nqueens_backtracking(board, col, n):
    if col >= n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens_backtracking(board, col + 1, n) or res
            board[i][col] = 0  # BACKTRACK

    return res


# Branch and Bound utility function to check if a queen can be placed


def solve_nqueens_branch_and_bound(n):
    # Helper to solve N-Queens using Branch and Bound
    def bnb_helper(board, col):
        if col >= n:
            print_solution(board)
            return True

        res = False
        for i in range(n):
            if not row_lookup[i] and not slash_lookup[i + col] and not backslash_lookup[i - col + n - 1]:
                board[i][col] = 1
                row_lookup[i] = slash_lookup[i + col] = backslash_lookup[i - col + n - 1] = True


                res = bnb_helper(board, col + 1) or res


                board[i][col] = 0
                row_lookup[i] = slash_lookup[i + col] = backslash_lookup[i - col + n - 1] = False


        return res


    board = [[0] * n for _ in range(n)]
    row_lookup = [False] * n
    slash_lookup = [False] * (2 * n - 1)
    backslash_lookup = [False] * (2 * n - 1)


    if not bnb_helper(board, 0):
        print("No solution exists")


# Main driver code
n = int(input("Enter the value of N for N-Queens problem: "))


print("\nSolutions using Backtracking:")
board = [[0] * n for _ in range(n)]
start_time = time.time()
if not solve_nqueens_backtracking(board, 0, n):
    print("No solution exists")
end_time = time.time()
print(f"Execution time (Backtracking): {end_time - start_time:.5f} s")


print("\nSolutions using Branch and Bound:")
start_time = time.time()
solve_nqueens_branch_and_bound(n)
end_time = time.time()
print(f"Execution time (Branch and Bound): {end_time - start_time:.5f} s")
