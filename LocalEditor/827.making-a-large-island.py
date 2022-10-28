#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] Making A Large Island
#
# https://leetcode.cn/problems/making-a-large-island/description/
#
# algorithms
# Hard (39.60%)
# Likes:    249
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 56.6K
# Testcase Example:  '[[1,0],[0,1]]'
#

question_content="""You are given an n x n binary matrix grid. You are allowed to change at most
one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.


Example 1:


Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with
area = 3.


Example 2:


Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island
with area = 4.

Example 3:


Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.



Constraints:


n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        tags = [[-1] * n for _ in range(m)]
        
        def dfs(i, j):
            """ dfs遍历从i,j出发的连通岛屿, 给网格打上标签 """
            nonlocal tag, islandSize
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1], ]:
                ii, jj = i + di, j + dj
                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    continue
                # 打上边缘点标签
                if grid[ii][jj] == 0:
                    tags[ii][jj] = 0
                # 若是岛屿且未探索
                if grid[ii][jj] == 1 and tags[ii][jj] == -1:
                    tags[ii][jj] = tag
                    islandSize[tag-1] += 1
                    dfs(ii, jj)
        
        # dfs遍历索引网格点, 将岛屿打上tag标签, 0 表示岛屿边缘
        islandSize = []
        tag = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and tags[i][j] == -1:
                    islandSize.append(1)
                    tags[i][j] = tag
                    dfs(i, j)
                    tag += 1
        
        # dfs遍历非岛屿点
        maxSize = 1
        for i in range(m):
            for j in range(n):
                if tags[i][j] == 0:
                    # 统计四周连通的岛屿的面积和
                    sz = 0
                    d = set()
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1], ]:
                        ii, jj = i + di, j + dj
                        # 过滤地图外的点
                        if ii < 0 or ii >= m or jj < 0 or jj >= n:
                            continue
                        # 过滤岛屿点
                        if tags[ii][jj] in [-1, 0]:
                            continue
                        # 过滤重复岛屿点
                        if tags[ii][jj] in d:
                            continue
                        # 累加周围岛屿面积
                        d.add(tags[ii][jj])
                        sz += islandSize[tags[ii][jj]-1]
                    maxSize = max(maxSize, sz + 1)
        
        # 如果岛内没有任何岛屿边缘点(即maxSize为初始值), 返回原本的最大岛屿面积
        if maxSize==1 and len(islandSize):
            maxSize = max(islandSize)
        return maxSize
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

