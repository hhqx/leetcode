question_content = """
You are given an m x n integer matrix grid where each cell is either 0 (empty) 
or 1 (obstacle). You can move up, down, left, or right from and to an empty cell 
in one step. 

 Return the minimum number of steps to walk from the upper left corner (0, 0) 
to the lower right corner (m - 1, n - 1) given that you can eliminate at most k 
obstacles. If it is not possible to find such walk return -1. 

 
 Example 1: 

测试用例:[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0],[0,0,0],[0,1,1],[0,0,0],[0,0,0],[0,1,1],[0,0,0],[0,0,0],[0,1,1],[0,0,0],[0,0,0],[0,1,1],[0,0,0],[0,0,0],[0,1,1],[0,0,0],[0,0,0],[0,1,1],[0,0,0],[0,0,0],[0,1,1],[0,0,0],[0,0,0],[0,1,1],[0,0,0]]
        1
测试结果:34
期望结果:30

测试用例:[[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]
        1
测试结果:26
期望结果:20
 
测试用例:[[0,0,1,0,0],[0,1,0,1,0]]
    2
测试结果:-1
期望结果:5

Input: grid = [[0]], k = 1
Output: 0

Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such 
path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

 Example 2: 
 
 
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

 
 Constraints: 

 
 m == grid.length 
 n == grid[i].length 
 1 <= m, n <= 40 
 1 <= k <= m * n 
 grid[i][j] is either 0 or 1. 
 grid[0][0] == grid[m - 1][n - 1] == 0 
 

 Related Topics 广度优先搜索 数组 矩阵 👍 212 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        INF = float('inf')
        m, n = len(grid), len(grid[0])
        dp = [[[INF] * n for _ in range(m)] for __ in range(k + 1)]

        def neighbor(x, y):
            ans = [
                (xx, yy) for xx, yy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),)
                if 0 <= xx < m and 0 <= yy < n
            ]
            # for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1),):
            return ans

        # 初始化k=0时的情况, bfs求最短路径
        # dp0 = [[INF] * n for _ in range(m)]
        dp0 = dp[0]

        q = deque([(m - 1, n - 1)])
        visited = [[0] * n for _ in range(m)]
        visited[m - 1][n - 1] = True  # 入队后记得添加访问标记
        cnt = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                dp0[x][y] = cnt

                # 添加邻居点
                next = neighbor(x, y)
                for i, j in next:
                    if not visited[i][j] and grid[i][j] == 0:
                        q.append((i, j))
                        visited[i][j] = True
            cnt += 1

        # 动态规划状态转移, 尝试根据可破坏的障碍物个数进行动态规划
        for kk in range(1, k + 1):
            # 预想的是当前点最小路径等于上一个破坏障碍个数的所以邻居的最小值, 结果说明只是部分合理
            for i in range(m):
                for j in range(n):
                    # dp[kk][i][j] = min(dp[kk-1][i][j] 's nerghbor)
                    if dp[kk - 1][i][j] == INF or 1:
                        next = neighbor(i, j)
                        if next:
                            dp[kk][i][j] = min(dp[kk - 1][ii][jj] + 1 for ii, jj in next)
                        dp[kk][i][j] = min(dp[kk][i][j], dp[kk - 1][i][j])
            for i in range(m):
                for j in range(n):
                    # dp[kk][i][j] = min(dp[kk-1][i][j] 's nerghbor)
                    # if dp[kk-1][i][j] != INF:
                    if grid[i][j] == 0 or dp[kk - 1][i][j] != INF:
                        # if grid[i][j] == 0:
                        # if dp[kk][i][j] != INF or dp[kk-1][i][j] != INF:
                        next = neighbor(i, j)
                        if next:
                            dp[kk][i][j] = min(dp[kk][ii][jj] + 1 for ii, jj in next)
                        dp[kk][i][j] = min(dp[kk][i][j], dp[kk - 1][i][j])
        ans = dp[k][0][0]
        return ans if ans != INF else -1


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        这个方法在终点附件一碰到障碍物就用掉了次数, 不是最优情况,
        有时需要在中间某个地方用这个次数收益更大
        """
        m, n = len(grid), len(grid[0])

        def neighbor(x, y):
            ans = [
                (xx, yy) for xx, yy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),)
                if 0 <= xx < m and 0 <= yy < n
            ]
            return ans

        # bfs求最短路径
        dp0 = [[-1] * n for _ in range(m)]
        q = deque([(m - 1, n - 1, k)])
        # visited = [[0] * n for _ in range(m)]
        # visited[m - 1][n - 1] = True  # 入队后记得添加访问标记
        visited = set([(m - 1, n - 1, k)])  # 以后入队标记改成这种集合方式
        cnt = 0
        while q:
            for _ in range(len(q)):
                x, y, left_k = q.popleft()
                dp0[x][y] = cnt
                left_k -= grid[x][y]  # 剩余破坏步长

                # 添加邻居点
                next = neighbor(x, y)
                for i, j in next:
                    if (i, j) not in visited and left_k >= 0:
                        q.append((i, j, left_k))
                        visited.add((i, j))
            cnt += 1
        return dp0[0][0]

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        bfs + 队列 + 状态图(每个节点的visited标记变成剩余步长, 若状态不一样可以重走该路径)
        """
        m, n = len(grid), len(grid[0])

        def neighbor(x, y):
            ans = [
                (xx, yy) for xx, yy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),)
                if 0 <= xx < m and 0 <= yy < n
            ]
            return ans

        # ans = []
        # bfs求最短路径
        q = deque([(m - 1, n - 1, k)])
        s = [[set() for _ in range(n)] for __ in range(m)]
        s[m-1][n-1].add(k)
        cnt = 0
        while q:
            for _ in range(len(q)):
                x, y, left_k = q.popleft()
                left_k -= grid[x][y]  # 剩余破坏步长
                if (x, y) == (0, 0):
                    # ans.append(cnt)  # 由于求的是最短路径, bfs第一个到达的路径一定是最短的
                    return cnt

                # 添加邻居点
                next = neighbor(x, y)
                for i, j in next:
                    if left_k not in s[i][j] and left_k >= 0:
                        q.append((i, j, left_k))
                        s[i][j].add(left_k)
            cnt += 1
        # return min(ans) if ans else -1
        return -1

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        bfs + 队列 + 剩余步长状态的visited标记
        """
        m, n = len(grid), len(grid[0])

        # bfs求最短路径
        q = deque([(m - 1, n - 1, k)])
        visited = set([(m - 1, n - 1, k)])  # 以后入队标记改成这种集合方式
        cnt = 0
        while q:
            for _ in range(len(q)):
                x, y, left_k = q.popleft()
                left_k -= grid[x][y]  # 剩余破坏步长
                if (x, y) == (0, 0):  # 到达终点退出
                    return cnt

                # 搜索邻居点
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),):
                    if 0 <= i < m and 0 <= j < n:
                        if (i, j, left_k) not in visited and left_k >= 0:
                            q.append((i, j, left_k))
                            visited.add((i, j, left_k))
            cnt += 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
