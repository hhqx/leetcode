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

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def add_ij(i, j):
            """ 坐标自增: 若j<len(board), j++; 否则j=0, i++;  """
            return i + j // len(board), j % len(board)

        def dfs(i, j):
            nonlocal success, board, rowUsed, colUsed
    
            # 坐标自增: 若j<len(board), j++; 否则j=0, i++; 
            # 若当前位置不需要填数字, 移到下一个坐标
            i, j = add_ij(i, j)
            while i < len(board) and board[i][j] != '.':
                i, j = add_ij(i, j+1) 
            
            # 如果移动到末尾则结束
            if i >= len(board):
                success = True
                return 

            for digit in range(len(board)):
                # 若当前数字非法, 则跳过该数字
                if rowUsed[i][digit] or colUsed[j][digit] or blockUsed[i//3][j//3][digit]:
                    continue
                
                # 尝试填入数字
                rowUsed[i][digit], colUsed[j][digit], blockUsed[i//3][j//3][digit] = True, True, True
                board[i][j] = str(digit+1)
                
                # 递归进入下一个待填数字
                dfs(i, j+1)

                if success:
                    return
                
                # 当前数字无法填入, 擦除该数字, 回溯
                board[i][j] = '.'
                rowUsed[i][digit], colUsed[j][digit], blockUsed[i//3][j//3][digit] = False, False, False
            
            return False

        # 初始化全局变量
        success = False
        rowUsed = [[False] * len(board) for i in range(len(board))]
        colUsed = [[False] * len(board) for i in range(len(board))]
        blockUsed = [[[False] * len(board) for i in range(3)] for i in range(3)]
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    rowUsed[i][int(c)-1], colUsed[j][int(c)-1], blockUsed[i//3][j//3][int(c)-1] = True, True, True
        
        dfs(0, 0)
        # show result
        for row in board:
            print(row)

        return board
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

