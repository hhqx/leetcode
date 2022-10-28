import collections

question_content = """
English description is not available for the problem. Please switch to Chinese. 

输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4 
解释：最长递增路径为 [1, 2, 6, 9]。

输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4 
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。


输入：matrix = [[1]]
输出：1


 Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 记忆化搜索 数组 动态规划 矩阵 👍 29 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        maxVal = -1

        def calculate(i, j):
            nonlocal maxVal
            if not (0 <= i < m and 0 <= j < n):
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            else:
                ans = 1
                for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if (0 <= x < m and 0 <= y < n) and matrix[i][j] < matrix[x][y]:
                        # print(matrix[x][y])
                        dpxy = calculate(x, y) + 1
                    else:
                        dpxy = 0
                    # print(dpxy, )
                    ans = max(ans, dpxy)

                dp[i][j] = ans
                maxVal = max(ans, maxVal)
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1:
                    calculate(i, j)

        return maxVal

class Solution:
    """ 拓扑排序法(bfs从出度为1的点开始遍历) """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        degree = [[0]*n for _ in range(m)]
        queue = collections.deque()

        # 统计节点出度
        for i in range(m):
            for j in range(n):
                outdegree = 0
                for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if (0 <= x < m and 0 <= y < n) and matrix[i][j] < matrix[x][y]:
                        outdegree += 1
                degree[i][j] = outdegree
                if outdegree == 0:
                    queue.append((i, j))

        # 拓扑排序
        cnt = 0
        while queue:
            length = len(queue)
            # 广度优先遍历, 一次for循环一层
            for _ in range(length):
                i, j = queue.popleft()
                # 遍历可能连接到i,j的点x,y, 删除i,j后修改x,y的出度
                for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if (0 <= x < m and 0 <= y < n) and matrix[x][y] < matrix[i][j]:
                        degree[x][y] -= 1
                        if degree[x][y] == 0:
                            queue.append((x, y))
            cnt += 1

        return cnt

class Solution:
    """ 排序后动态规划, 类似广度优先搜索"""
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        x = len(matrix)
        y = len(matrix[0])
        dp = [[1 for __ in range(y)] for __ in range(x)]
        numsSort = sorted(sum(
            [[(matrix[i][j], i, j) for j in range(y)] for i in range(x)], []
        ))
        for i, j, k in numsSort[1:]:
            dp[j][k] = 1+max(
                            dp[j-1][k] if j and matrix[j-1][k]<i else 0,
                            dp[j][k-1] if k and matrix[j][k-1]<i else 0,
                            dp[j+1][k] if j != x-1 and matrix[j+1][k]<i else 0,
                            dp[j][k+1] if k != y-1 and matrix[j][k+1]<i else 0
                            )
        return max(sum(dp, []))
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
