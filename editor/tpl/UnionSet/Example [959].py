question_content = r"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of 
a '/', '\', or blank space ' '. These characters divide the square into 
contiguous regions. 

 Given the grid grid represented as a string array, return the number of 
regions. 

 Note that backslash characters are escaped, so a '\' is represented as '\\'. 


 Example 1: 


Input: grid = [" /","/ "]
Output: 2


 Example 2: 


Input: grid = [" /","  "]
Output: 1


 Example 3: 


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, 
and "/\\" refers to /\.



 Constraints: 


 n == grid.length == grid[i].length 
 1 <= n <= 30 
 grid[i][j] is either '/', '\', or ' '. 


 Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 320 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        """ 将 \, / 替换成 3*3 的网格后求连通块个数. """
        m1, n1 = len(grid), len(grid[0])

        # ngrid 的长宽都是原来的 3 倍
        m, n = 3 * m1, 3 * n1
        ngrid = [[0] * n for _ in range(m)]
        # 构造 ngrid
        for i in range(n1):
            for j in range(m1):
                # 因为图像坐标系左上角才是原点
                if grid[i][j] == '\\':
                    for x, y in ((0, 0), (1, 1), (2, 2),):
                        ngrid[3 * i + x][3 * j + y] = 1
                elif grid[i][j] == '/':
                    for x, y in ((0, 2), (1, 1), (2, 0),):
                        ngrid[3 * i + x][3 * j + y] = 1

        # for row in ngrid:
        #     print(row)

        # 求连通域个数
        def dfs(x, y):
            ''' dfs 遍历连通域并打上标签 '''
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),):
                if 0 <= i < m and 0 <= j < n and ngrid[i][j] == 0:
                    ngrid[i][j] = 2
                    dfs(i, j)
            return

        cnt = 0
        for i in range(m):
            for j in range(n):
                if ngrid[i][j] == 0:
                    ngrid[i][j] = 2
                    dfs(i, j)
                    cnt += 1

        return cnt


class UF:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0
        # 初始化 parent，size 和 cnt
        for i in range(M):
            self.parent[i] = i
            self.cnt += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q): return
        leader_p = self.find(p)
        leader_q = self.find(q)
        self.parent[leader_p] = leader_q
        self.cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        N = n * n * 4
        uf = UF(N)

        def get_pos(row, col, i):
            return (row * n + col) * 4 + i

        for row in range(n):
            for col in range(n):
                v = grid[row][col]
                if row > 0:
                    uf.union(get_pos(row - 1, col, 2), get_pos(row, col, 1))
                if col > 0:
                    uf.union(get_pos(row, col - 1, 3), get_pos(row, col, 0))
                if v == '/':
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 1))
                    uf.union(get_pos(row, col, 2), get_pos(row, col, 3))
                if v == '\\':
                    uf.union(get_pos(row, col, 1), get_pos(row, col, 3))
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 2))
                if v == ' ':
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 1))
                    uf.union(get_pos(row, col, 1), get_pos(row, col, 2))
                    uf.union(get_pos(row, col, 2), get_pos(row, col, 3))

        return uf.cnt


# 作者：fe-lucifer
# 链接：https://leetcode.cn/problems/regions-cut-by-slashes/solution/liang-chong-fang-fa-bing-cha-ji-he-dfs95-uhof/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
