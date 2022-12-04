question_content = """
6256. 将节点分成尽可能多的组
给你一个正整数 n ，表示一个 无向 图中的节点数目，节点编号从 1 到 n 。

同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 双向 边。注意给定的图可能是不连通的。

请你将图划分为 m 个组（编号从 1 开始），满足以下要求：

图中每个节点都只属于一个组。
图中每条边连接的两个点 [ai, bi] ，如果 ai 属于编号为 x 的组，bi 属于编号为 y 的组，那么 |y - x| = 1 。
请你返回最多可以将节点分为多少个组（也就是最大的 m ）。如果没办法在给定条件下分组，请你返回 -1 。

 

示例 1：
输入:
30
[[1,9],[30,27],[21,9],[2,10],[16,28],[1,27],[20,24],[22,24],[30,6],[30,19],[1,19],[30,11],[16,6],[16,29],[2,29],[2,23],[16,24],[1,25],[1,17],[16,23],[30,26],[16,12],[1,14],[13,23],[13,14],[2,19],[22,6],[30,3],[30,18],[20,8],[13,24],[20,9],[20,14],[13,28],[13,10],[2,8],[16,7],[16,10],[21,5],[20,15],[20,11],[2,26],[21,3],[22,10],[16,8],[2,17]]
输出:
8


输入：n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
输出：4
解释：如上图所示，
- 节点 5 在第一个组。
- 节点 1 在第二个组。
- 节点 2 和节点 4 在第三个组。
- 节点 3 和节点 6 在第四个组。
所有边都满足题目要求。
如果我们创建第五个组，将第三个组或者第四个组中任何一个节点放到第五个组，至少有一条边连接的两个节点所属的组编号不符合题目要求。
示例 2：

输入：n = 3, edges = [[1,2],[2,3],[3,1]]
输出：-1
解释：如果我们将节点 1 放入第一个组，节点 2 放入第二个组，节点 3 放入第三个组，前两条边满足题目要求，但第三条边不满足题目要求。
没有任何符合题目要求的分组方式。
 

提示：

1 <= n <= 500
1 <= edges.length <= 104
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
两个点之间至多只有一条边。
通过次数521提交次数2,281

"""
def plot_graph(edges):
    import matplotlib.pyplot as plt
    import networkx as nx
    G = nx.Graph()
    # H = nx.path_graph(10)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # 建图
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # vis = defaultdict(int)
        # bfs
        def bfs(s):
            start = [(s, 1)]
            q = deque(start)
            vis = defaultdict(int)
            vis[s] = 1
            # ret = float('-inf')
            ret = -1
            while q:
                for _ in range(len(q)):
                    u, layer = q.popleft()
                    ret = max(ret, layer)

                    for v in g[u]:
                        if v in vis and vis[v] == layer:
                            # print(s, u, v, layer)
                            return -1
                        if v not in vis:
                            vis[v] = layer + 1
                            q.append((v, layer + 1))

            return ret

        ans = 0
        label = [0] * (n + 1)
        # bfs
        for start in range(1, n + 1):
            # group连通域
            group = []
            if label[start] != 0:
                continue

            q = deque([start])
            vis = set([start])
            ret = -1
            while q:
                for _ in range(len(q)):
                    u = q.pop()
                    label[u] = 1
                    group.append(u)
                    for v in g[u]:
                        if v not in vis:
                            vis.add(v)
                            q.append(v)
            # print(group)

            # 对每个连通域bfs
            tmp = float('-inf')
            for u in group:
                dep = bfs(u)
                if dep >= 0:
                    tmp = max(tmp, dep)
            # 累加不同连通域的结果
            if tmp > 0:
                ans += tmp
            else:
                ans = 0
                break

        return ans if ans != 0 else -1

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
