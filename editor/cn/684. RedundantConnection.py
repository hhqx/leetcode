question_content = """
In this problem, a tree is an undirected graph that is connected and has no 
cycles. 

 You are given a graph that started as a tree with n nodes labeled from 1 to n, 
with one additional edge added. The added edge has two different vertices 
chosen from 1 to n, and was not an edge that already existed. The graph is 
represented as an array edges of length n where edges[i] = [ai, bi] indicates that there 
is an edge between nodes ai and bi in the graph. 

 Return an edge that can be removed so that the resulting graph is a tree of n 
nodes. If there are multiple answers, return the answer that occurs last in the 
input. 

 
 Example 1: 
 
 
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
 

 Example 2: 
 
 
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

 
 Constraints: 

 
 n == edges.length 
 3 <= n <= 1000 
 edges[i].length == 2 
 1 <= ai < bi <= edges.length 
 ai != bi 
 There are no repeated edges. 
 The given graph is connected. 
 

 Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 557 👎 0

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
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            # 把x分支的祖先指向y分支的祖先, 同时进行路径压缩
            self.parent[px] = py
            self.cnt -= 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        obj = UnionSet(n)
        for u, v in edges:
            before = obj.cnt
            obj.union(u-1, v-1)
            if obj.cnt == before:
                return [u, v]

        return None


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
