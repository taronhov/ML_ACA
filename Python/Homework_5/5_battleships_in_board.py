""" 
Since "At least one horizontal or vertical cell separates between two battleships 
(i.e., there are no adjacent battleships).", the number of recursive calls can bereduced.
"""

def CountBattleships_1(board):
    row = len(board)
    col = len(board[0])

    counter = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'X':
                if i == 0 and j == 0:
                    counter += 1
                elif i == 0 and j != 0:
                    if board[i][j - 1] != 'X':
                        counter += 1
                elif i != 0 and j == 0:
                    if board[i - 1][j] != 'X':
                        counter += 1
                else:
                    if board[i - 1][j] != 'X' and board[i][j - 1] != 'X':
                        counter += 1

    return counter


def CountBattleships_2(board):
    row = len(board)
    col = len(board[0])

    counter = 0
    for r in range(row):
        for c in range(col):
            if board[r][c] == 'X':
                var = 1
                if (r > 0 and board[r-1][c] == 'X') or (c > 0 and board[r][c-1] == 'X'):
                    var = 0
                counter += var

    return counter


if __name__ == '__main__':

    board = [["X",".",".","X"], [".",".",".","X"], [".",".",".","X"]]

    print(CountBattleships_2(board))
