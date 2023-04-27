question_content = """

 
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，
那么城市 a 与城市 c 间接相连。 

 
 

 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。 

 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 
isConnected[i][j] = 0 表示二者不直接相连。 

 返回矩阵中 省份 的数量。 

 

 示例 1： 
 
 
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
 

 示例 2： 
 
 
输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
 

 

 提示： 

 
 1 <= n <= 200 
 n == isConnected.length 
 n == isConnected[i].length 
 isConnected[i][j] 为 1 或 0 
 isConnected[i][i] == 1 
 isConnected[i][j] == isConnected[j][i] 
 

 Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 959 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class UnionSet:
    def __init__(self, n=0):
        self.parent = list(range(n))
        # self.cnt = n

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
            u = self.parent[u]
        return self.parent[u]

    def add(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py
            # self.cnt -= 1
        return

    def count(self):
        # return self.cnt
        n = len(self.parent)
        s = set()
        for i in range(n):
            s.add(self.find(i))
        return len(s)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """ dfs """
        n = len(isConnected)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    g[i].append(j)
                    g[j].append(i)

        # dfs
        vis = set()

        def dfs(u):
            for v in g[u]:
                if v in vis:
                    continue
                vis.add(v)
                dfs(v)

        cnt = 0
        for i in range(n):
            if i in vis:
                continue
            cnt += 1
            vis.add(i)
            dfs(i)
        return cnt

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """ dfs """
        n = len(isConnected)
        obj = UnionSet(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    obj.add(i, j)

        return obj.count()


class Solution1:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        cities = len(isConnected)
        parent = list(range(cities))

        for i in range(cities):
            for j in range(i + 1, cities):
                if isConnected[i][j] == 1:
                    union(i, j)

        provinces = sum(parent[i] == i for i in range(cities))
        return provinces

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
