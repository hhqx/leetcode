#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.cn/problems/sudoku-solver/description/
#
# algorithms
# Hard (67.63%)
# Likes:    1387
# Dislikes: 0
# Total Accepted:    168.8K
# Total Submissions: 249.6K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#

question_content="""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:


Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
of the grid.


The '.' character indicates empty cells.


Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output:
[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation:The input board is shown above and the only valid solution is
shown below:





Constraints:


board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.


"""



from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        result = []
        path = []

        rowUsed = [[False] * len(board) for i in range(len(board))]
        colUsed = [[False] * len(board) for i in range(len(board))]
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    rowUsed[i][int(c) - 1], colUsed[j][int(c) - 1] = True, True

        def add_ij(i, j):

            return i + j // len(board), j % len(board)

        success = False

        def get_optimal_ij():
            min_left = [float('inf'), 0, 0]
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c != '.':
                        continue
                    left_num = len(board) - sum([rowUsed[i][digit] or colUsed[i][digit] for digit in range(len(board))])
                    if 0 < left_num < min_left[0]:
                        min_left = [left_num, i, j]
                        # print(left_num)
            if len(min_left) <= 1:
                success = True
                return 0, 0, -1
            if min_left[0] > len(board):
                min_left[0] = -1
            return min_left[1], min_left[2], min_left[0]

        def dfs(i, j):
            # i, j = add_ij(i, j)
            # while i < len(board) and board[i][j] != '.':
            #     i, j = add_ij(i, j+1)
            #     print(f'i={i}, j={j},')

            i, j, left_num = get_optimal_ij()
            print(f'i={i}, j={j}, num={left_num}')
            if left_num == -1:
                return

            # return
            if i >= len(board):
                return

            # used = rowUsed[i] | colUsed[j]
            for digit in range(len(board)):
                if rowUsed[i][digit] or colUsed[j][digit]:
                    continue

                rowUsed[i][digit], colUsed[j][digit] = True, True
                board[i][j] = str(digit)
                # print(f'i={i}, j={j}, fill_digit={digit}')
                dfs(i, j + 1)
                if left_num == -1 or success:
                    return
                board[i][j] = '.'
                rowUsed[i][digit], colUsed[j][digit] = False, False

        dfs(0, 0)
        return
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
