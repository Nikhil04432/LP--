def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n):
    if row == n:
        print_solution(board)
        return True  # Change to False if you want **all** solutions

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve(board, row + 1, n):
                return True
            board[row][col] = '.'  # Backtrack
    return False

def print_solution(board):
    for row in board:
        print(' '.join(row))
    print()

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0, n)

# Example usage
n = int(input("Enter value of N: "))
solve_n_queens(n)
