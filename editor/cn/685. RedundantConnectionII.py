question_content = """
In this problem, a rooted tree is a directed graph such that, there is exactly 
one node (the root) for which all other nodes are descendants of this node, plus 
every node has exactly one parent, except for the root node which has no 
parents. 

 The given input is a directed graph that started as a rooted tree with n nodes 
(with distinct values from 1 to n), with one additional directed edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge 
that already existed. 

 The resulting graph is given as a 2D-array of edges. Each element of edges is 
a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, 
where ui is a parent of child vi. 

 Return an edge that can be removed so that the resulting graph is a rooted 
tree of n nodes. If there are multiple answers, return the answer that occurs last 
in the given 2D-array. 

 
 Example 1: 
 
 
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
 

 Example 2: 
 
 
Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]
 
测试用例:[[2,1],[3,1],[4,2],[1,4]]
期望结果:[2,1]

测试用例:[[5,2],[5,1],[3,1],[3,4],[3,5]]
测试结果:[5,1]
期望结果:[3,1]

测试用例:[[4,1],[4,5],[2,4],[5,3],[2,1]]
测试结果:[5,3]
期望结果:[2,1]

 Constraints: 

 
 n == edges.length 
 3 <= n <= 1000 
 edges[i].length == 2 
 1 <= ui, vi <= n 
 ui != vi 
 

 Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 359 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]], n=None) -> List[int]:
        """
        每次添加后, 针对每个根节点dfs判断是否为树, o(n*n),
        思路错误, 只能找到哪条边存在冲突, 无法确定是哪一条
        """
        n = len(edges) if n is None else n
        g = [[] for _ in range(n)]

        def dfs(u):
            """ dfs 求树状图g 的子树u下的节点个数, 若  """
            r = 1
            for v in g[u]:
                if v in vis:
                    return -inf
                vis.add(v)
                r += dfs(v)
            return r

        roots = set(range(n))
        for k, (u, v) in enumerate(edges):
            g[u - 1].append(v - 1)

            # 维护入度为0的根节点roots
            if v - 1 in roots:
                roots.remove(v - 1)
            vis = set()
            cnt = 0
            for root in roots:
                vis.add(root)
                if g[root]:
                    cnt += dfs(root)
                else:
                    cnt += 1
            # 如果所有子树的节点之和不等于n说明存在环
            if cnt != n:
                if (r2 := self.findRedundantDirectedConnection(edges[:k] + edges[k + 1:], n=n)) is not None:
                    return r2
                return [u, v]

        return None


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        暴力枚举n种删除情况, dfs判断树是否合法, o(n*n)
        """
        n = len(edges)

        def dfs(u):
            """ dfs 求树状图g 的子树u下的节点个数, 若  """
            r = 1
            for v in g[u]:
                if v in vis:
                    return -inf
                vis.add(v)
                r += dfs(v)
            return r

        for i in range(n - 1, -1, -1):
            # 建图
            g = [[] for _ in range(n)]
            roots = set(range(n))
            for j, (u, v) in enumerate(edges):
                if i == j:
                    continue
                g[u - 1].append(v - 1)
                if v - 1 in roots:
                    roots.remove(v - 1)
            vis = set()
            if sum(dfs(root) for root in roots) == n:
                return edges[i]

        return None


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        dfs 找出冲突的路径path,
        1. 如果冲突的路径是不是环, 则找最后一个(u,v)满足v=path[-1]
        2. 如果冲突的路径是入度大于零的环(存在根节点), 返回path[-2:]
        3. 如果是入度等于零的环, 此时环中任意边删除均可构成树, 返回环中的最后一条边
        """
        n = len(edges)

        def dfs(u):
            if u in vis_prev:
                return False
            path.append(u)
            for v in g[u]:
                if v in vis:
                    # print('vis', vis, v, g[u])
                    path.append(v)
                    return True
                vis.add(v)
                if dfs(v):
                    return True
            path.pop()
            return False

        path = []
        vis = set()

        g = [[] for _ in range(n + 1)]
        roots = set(range(1, n + 1))
        for u, v in edges:
            g[u].append(v)
            if v in roots:
                roots.remove(v)

        print('roots', roots)
        vis_prev = set()
        if not roots:
            for root in range(1, n + 1):
                vis = {root}
                if dfs(root):
                    break
                vis_prev.union(vis)
        elif len(roots) == 1:
            root = roots.pop()
            path = []
            vis = {root}
            dfs(root)
        else:
            assert 0, ""

        # print(path)
        if any(path[-1] == u for u in path[:-1]):
            if path[0] != path[-1]:
                return path[-2:]
            # 入度为零的环
            edgeInCircle = set()
            for cur in range(len(path) - 1 - 1, -1, -1):
                edgeInCircle.add((path[cur], path[cur + 1]))
                if path[cur] == path[-1]:
                    break
            for u, v in reversed(edges):
                if (u, v) in edgeInCircle:
                    return [u, v]
        else:
            for u, v in reversed(edges):
                if v == path[-1]:
                    # 无环的冲突
                    return [u, v]
        return None


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
