# Function to print the board
def print_solution(board):
    for row in board:
        for col in row:
            if col == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# ---------- Optimized Backtracking (with arrays) ----------
def is_safe(row, col, slash_diagonal, backslash_diagonal, columns, n):
    if slash_diagonal[row + col] or backslash_diagonal[row - col + n - 1] or columns[col]:
        return False
    return True

def solve_n_queens_optimized_util(board, row, slash_diagonal, backslash_diagonal, columns, solutions, n):
    if row == n:
        solution = [r[:] for r in board]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(row, col, slash_diagonal, backslash_diagonal, columns, n):
            board[row][col] = 1
            columns[col] = slash_diagonal[row + col] = backslash_diagonal[row - col + n - 1] = True

            solve_n_queens_optimized_util(board, row + 1, slash_diagonal, backslash_diagonal, columns, solutions, n)

            board[row][col] = 0
            columns[col] = slash_diagonal[row + col] = backslash_diagonal[row - col + n - 1] = False

def solve_n_queens_optimized(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    columns = [False] * n
    slash_diagonal = [False] * (2 * n - 1)
    backslash_diagonal = [False] * (2 * n - 1)
    solutions = []
    solve_n_queens_optimized_util(board, 0, slash_diagonal, backslash_diagonal, columns, solutions, n)
    return solutions

# ---------- Normal Backtracking (basic safety checks) ----------
def is_safe_basic(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Recursive function to solve N-Queens using normal backtracking
def solve_n_queens_basic_util(board, row, solutions, n):
    if row == n:
        # Create a deep copy of the board to store as a solution
        solution = []
        for i in range(n):
            new_row = []
            for j in range(n):
                new_row.append(board[i][j])
            solution.append(new_row)
        solutions.append(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe_basic(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_n_queens_basic_util(board, row + 1, solutions, n)
            board[row][col] = 0  # Backtrack

# Main function to initialize the board and call the recursive utility
def solve_n_queens_basic(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)

    solutions = []
    solve_n_queens_basic_util(board, 0, solutions, n)
    return solutions


# ------------------- MAIN -------------------
n = 4

# Optimized version
print("Optimized Backtracking (with lookup arrays):")
solutions_optimized = solve_n_queens_optimized(n)
print("Total solutions:", len(solutions_optimized))
for sol in solutions_optimized:
    print_solution(sol)

# Basic version
print("Basic Backtracking (no extra arrays):")
solutions_basic = solve_n_queens_basic(n)
print("Total solutions:", len(solutions_basic))
for sol in solutions_basic:
    print_solution(sol)
