question_content = """
Given an m x n matrix board containing 'X' and 'O', capture all regions that 
are 4-directionally surrounded by 'X'. 

 A region is captured by flipping all 'O's into 'X's in that surrounded region. 


 
 Example 1: 
 
 
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",
"X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]
]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
 

 Example 2: 

 
Input: board = [["X"]]
Output: [["X"]]
 

 
 Constraints: 

 
 m == board.length 
 n == board[i].length 
 1 <= m, n <= 200 
 board[i][j] is 'X' or 'O'. 
 

 Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 959 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        一次bfs + 一次遍历
        """
        m, n = len(board), len(board[0])
        start = [(i, 0) for i in range(m) if board[i][0] == 'O'] + \
                [(i, n - 1) for i in range(m) if board[i][-1] == 'O'] + \
                [(0, i) for i in range(n) if board[0][i] == 'O'] + \
                [(m - 1, i) for i in range(n) if board[-1][i] == 'O']
        vis = set(start)
        q = deque(start)
        # print(start)
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j),):
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if (x, y) in vis or board[x][y] == 'X':
                        continue
                    vis.add((x, y))
                    q.append((x, y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in vis:
                    board[i][j] = 'X'

        return board


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        一次 dfs
        """
        m, n = len(board), len(board[0])
        vis = set()

        def dfs(i, j, val):
            if val is not None:
                board[i][j] = 'X'
            for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j),):
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if (x, y) in vis or board[x][y] == 'X':
                    continue
                vis.add((x, y))
                dfs(x, y, val)

        edgePoints = chain(
            ((i, 0) for i in range(m) if board[i][0] == 'O'),
            ((i, n - 1) for i in range(m) if board[i][-1] == 'O'),
            ((0, i) for i in range(n) if board[0][i] == 'O'),
            ((m - 1, i) for i in range(n) if board[-1][i] == 'O'),
        )
        # visit edge region
        for i, j in edgePoints:
            if (i, j) in vis:
                continue
            vis.add((i, j))
            dfs(i, j, None)

        # visit inner region
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if (i, j) in vis:
                    continue
                vis.add((i, j))
                dfs(i, j, 'X')

        # for row in board:
        #     print(*row)
        return board

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
