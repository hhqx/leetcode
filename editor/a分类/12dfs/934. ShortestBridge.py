question_content = """
You are given an n x n binary matrix grid where 1 represents land and 0 
represents water. 

 An island is a 4-directionally connected group of 1's not connected to any 
other 1's. There are exactly two islands in grid. 

 You may change 0's to 1's to connect the two islands to form one island. 

 Return the smallest number of 0's you must flip to connect the two islands. 

 
 Example 1: 

 
Input: grid = [[0,1],[1,0]]
Output: 1
 

 Example 2: 

 
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
 

 Example 3: 

 
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

 
 Constraints: 

 
 n == grid.length == grid[i].length 
 2 <= n <= 100 
 grid[i][j] is either 0 or 1. 
 There are exactly two islands in grid. 
 

 Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 449 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """ dfs + 多源bfs """
        m, n = len(grid), len(grid[0])
        edge = []
        vis1 = set()

        def dfs(i, j):
            for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j),):
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in vis1:
                    continue
                if grid[x][y] == 0:
                    edge.append((x, y))
                    continue
                vis1.add((x, y))
                dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                vis1.add((i, j))
                dfs(i, j)
                break
            else:
                continue
            break

        step = 0
        q = deque(edge)
        vis = set()
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if grid[i][j] == 1:
                    return step

                for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j),):
                    if x < 0 or x >= m or y < 0 or y >= n or (x, y) in vis:
                        continue
                    if (x, y) in vis1:
                        continue
                    vis.add((x, y))
                    q.append((x, y))
            step += 1

        return None


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
