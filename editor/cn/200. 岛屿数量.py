question_content = """
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 

 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 

 此外，你可以假设该网格的四条边均被水包围。 

 

 示例 1： 

 
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
 

 示例 2： 

 
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

 

 提示： 

 
 m == grid.length 
 n == grid[i].length 
 1 <= m, n <= 300 
 grid[i][j] 的值为 '0' 或 '1' 
 

 Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 2152 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class UnionSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.cnt = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            x = self.parent[x]
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.cnt -= 1
            self.parent[px] = py

    def count(self):
        return self.cnt


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ 并查集求网格岛屿连通域数量 """
        m, n = len(grid), len(grid[0])

        def f(i, j):
            idx = i * n + j
            return idx

        zero_cnt = 0
        obj = UnionSet(m * n)
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    if i - 1 >= 0 and grid[i - 1][j] == '1':
                        obj.union(f(i, j), f(i - 1, j))
                    if j - 1 >= 0 and grid[i][j - 1] == '1':
                        obj.union(f(i, j), f(i, j - 1))
                else:
                    zero_cnt += 1
        return obj.count() - zero_cnt
    # leetcode submit region end(Prohibit modification and deletion)


# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
