#
# -*- coding: utf-8 -*-
question_content = """
给你一个大小为 m x n 的矩阵 grid ，其中每个单元格都放置有一个字符： 

 
 'W' 表示一堵墙 
 'E' 表示一个敌人 
 '0'（数字 0）表示一个空位 
 

 返回你使用 一颗炸弹 可以击杀的最大敌人数目。你只能把炸弹放在一个空位里。 

 由于炸弹的威力不足以穿透墙体，炸弹只能击杀同一行和同一列没被墙体挡住的敌人。 

 

 示例 1： 
 
 
输入：grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
输出：3
 

 示例 2： 
 
 
输入：grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
输出：1
 

 

 提示： 

 
 m == grid.length 
 n == grid[i].length 
 1 <= m, n <= 500 
 grid[i][j] 可以是 'W'、'E' 或 '0' 
 

 Related Topics 数组 动态规划 矩阵 👍 94 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """ 四个方向动态规划dp """
        m, n = len(grid), len(grid[0])
        dp = [[0] *n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                cnt = grid[i][j] == 'E'
                # cnt = 0
                if i+1 < m:
                    cnt += dp[i+1][j]
                dp[i][j] = cnt
        bottom = dp

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 'W':
                    continue
                cnt = grid[i][j] == 'E'
                # cnt = 0
                if j + 1 < n:
                    cnt += dp[i][j+1]
                dp[i][j] = cnt
        right = dp

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                cnt = grid[i][j] == 'E'
                # cnt = 0
                if i-1>=0:
                    cnt += dp[i-1][j]
                dp[i][j] = cnt
        top = dp

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                cnt = grid[i][j] == 'E'
                if j - 1 >= 0:
                    cnt += dp[i][j-1]
                dp[i][j] = cnt
        left = dp

        ans = max(
            top[i][j] + left[i][j] + right[i][j] + bottom[i][j]
            if grid[i][j] == '0' else 0
            for i in range(m) for j in range(n)
        )
        # print(top)
        # print(grid)

        return ans

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """ 行列分别搜索 dfs """
        m, n = len(grid), len(grid[0])
        row = [[0] * n for _ in range(m)]
        col = [[0] * n for _ in range(m)]

        def dfs(i, j, delta):
            nonlocal cnt
            di, dj = delta
            # print(i, j, cnt)
            cnt += grid[i][j] == 'E'
            for dir in [1, -1]:
                x, y = i+di*dir, j+dj*dir
                if x >= m or x < 0 or y >= n or y < 0:
                    continue
                if (x, y) in vis or grid[x][y] == 'W':
                    continue
                vis.add((x, y))
                dfs(x, y, delta)
        vis_total = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                if (i, j) in vis_total:
                    continue
                cnt = 0
                vis = {(i, j)}
                dfs(i, j, (0, 1))
                for x, y in vis:
                    row[x][y] = cnt
                vis_total.update(vis)
        vis_total = set()
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 'W':
                    continue
                if (i, j) in vis_total:
                    print('in vis', i, j)
                    continue
                cnt = 0
                vis = {(i, j)}
                dfs(i, j, (1, 0))
                for x, y in vis:
                    col[x][y] = cnt
                vis_total.update(vis)

        ans = max(
            row[i][j] + col[i][j] if grid[i][j] == '0' else 0
            for i in range(m) for j in range(n)
        )
        return ans


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """ 行列分别搜索, 用数组循环 """
        m, n = len(grid), len(grid[0])
        row = [[0] * n for _ in range(m)]
        col = [[0] * n for _ in range(m)]
        for i in range(m):
            start = -1
            cnt = 0
            for j in range(n+1):
                if j == n or grid[i][j] == "W":
                    for k in range(start+1, j):
                        row[i][k] = cnt
                    cnt = 0
                    start = j
                elif grid[i][j] == 'E':
                    cnt += 1
        for j in range(n):
            start = -1
            cnt = 0
            for i in range(m+1):
                if i == m or grid[i][j] == "W":
                    for k in range(start+1, i):
                        col[k][j] = cnt
                    cnt = 0
                    start = i
                elif grid[i][j] == 'E':
                    cnt += 1

        ans = max(
            row[i][j] + col[i][j] if grid[i][j] == '0' else 0
            for i in range(m) for j in range(n)
        )
        return ans

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
