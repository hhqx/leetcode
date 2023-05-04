question_content = """
Let's play the minesweeper game (Wikipedia, online game)! 

 You are given an m x n char matrix board representing the game board where: 

 
 'M' represents an unrevealed mine, 
 'E' represents an unrevealed empty square, 
 'B' represents a revealed blank square that has no adjacent mines (i.e., above,
 below, left, right, and all 4 diagonals), 
 digit ('1' to '8') represents how many mines are adjacent to this revealed 
square, and 
 'X' represents a revealed mine. 
 

 You are also given an integer array click where click = [clickr, clickc] 
represents the next click position among all the unrevealed squares ('M' or 'E'). 

 Return the board after revealing this position according to the following 
rules: 

 
 If a mine 'M' is revealed, then the game is over. You should change it to 'X'. 

 If an empty square 'E' with no adjacent mines is revealed, then change it to a 
revealed blank 'B' and all of its adjacent unrevealed squares should be 
revealed recursively. 
 If an empty square 'E' with at least one adjacent mine is revealed, then 
change it to a digit ('1' to '8') representing the number of adjacent mines. 
 Return the board when no more squares will be revealed. 
 

 
 Example 1: 
 
 
Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E",
"E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B",
"B","B","B","B"]]
 

 Example 2: 
 
 
Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1",
"B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B",
"B","B","B","B"]]
 

# 测试用例:[["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]
#         [0,0]
# 期望结果:[["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","2","M","1","B","B","1","1"],["M","2","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]]


测试用例:[["1","M","M","2","B","B","B","B"],["E","E","M","2","B","B","B","B"],["E","E","2","1","B","B","B","B"],["E","M","1","B","B","B","B","B"],["1","2","2","1","B","B","B","B"],["B","1","M","1","B","B","B","B"],["B","1","1","1","B","B","B","B"],["B","B","B","B","B","B","B","B"]]
        [1,1]
期望结果:[["1","M","M","2","B","B","B","B"],["E","3","M","2","B","B","B","B"],["E","E","2","1","B","B","B","B"],["E","M","1","B","B","B","B","B"],["1","2","2","1","B","B","B","B"],["B","1","M","1","B","B","B","B"],["B","1","1","1","B","B","B","B"],["B","B","B","B","B","B","B","B"]]

Constraints: 

 
 m == board.length 
 n == board[i].length 
 1 <= m, n <= 50 
 board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'. 
 click.length == 2 
 0 <= clickr < m 
 0 <= clickc < n 
 board[clickr][clickc] is either 'M' or 'E'. 
 

 Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 336 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """  """
        m, n = len(board), len(board[0])
        from itertools import product

        def count_adjacent(i, j):
            """ count land mine in adjacent region. """
            rows = range(max(0, i - 1), min(i + 1, m - 1) + 1)
            cols = range(max(0, j - 1), min(j + 1, n - 1) + 1)
            ret = sum(
                board[x][y] == 'M' for x, y in list(product(rows, cols))
            )
            # print(i, j, ret)
            return ret

        def dfs(i, j):
            """ dfs over all the 8 neighbors. """
            for x, y in product([i - 1, i, i + 1], [j - 1, j, j + 1]):
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if board[x][y] != "E":
                    continue
                cnt = count_adjacent(x, y)
                if cnt == 0:
                    board[x][y] = "B"
                    dfs(x, y)
                else:
                    board[x][y] = str(cnt)

        r, c = click
        if board[r][c] == "M":
            # click land mine, game over
            board[r][c] = "X"
        elif board[r][c] == "E":
            # dfs
            cnt = count_adjacent(r, c)
            if cnt != 0:
                board[r][c] = str(cnt)
            else:
                board[r][c] = "B"
                dfs(r, c)

        # for row in board:
        #     print(*row)
        return board


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
