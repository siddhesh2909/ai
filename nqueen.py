class NQueens:
def __init__(self, N):
self.N = N
self.board = [[0] * N for _ in range(N)]
self.column = [False] * N self.diagonal1
= [False] * (2 * N - 1) self.diagonal2 =
[False] * (2 * N - 1)

def solve(self, row=0):
if row == self.N:
self.print_soluFon()
return True

for col in range(self.N):
if not self.is_safe(row, col):
conFnue

self.place_queen(row, col)
if self.solve(row + 1):
return True # Return true to get one soluFon only
self.remove_queen(row, col)

return False

def is_safe(self, row, col):
return not (self.column[col] or self.diagonal1[row - col + self.N - 1] or self.diagonal2[row
+ col])

def place_queen(self, row, col):
self.board[row][col] = 1
self.column[col] = True
self.diagonal1[row - col + self.N - 1] = True
self.diagonal2[row + col] = True

def remove_queen(self, row, col):
self.board[row][col] = 0
self.column[col] = False
self.diagonal1[row - col + self.N - 1] = False
self.diagonal2[row + col] = False

def print_soluFon(self):
print("\nSoluFon for N =", self.N)
print("Board layout:\n") for row
in self.board:
print(" ".join("Q" if col else "." for col in row))
print("\nQ = Queen, . = Empty Square\n")

if __name__ == "__main__":
try:
N = int(input("Enter the size of the board (N): "))
if N <= 0:
print("Please enter a posiFve integer greater than 0.")
else:
solver = NQueens(N)
if not solver.solve():
print("No soluFon exists.")
except ValueError:

print("Invalid input! Please enter a valid integer.")
