question_content = """
给你一个无向图（原始图），图中有 n 个节点，编号从 0 到 n - 1 。你决定将图中的每条边 细分 为一条节点链，每条边之间的新节点数各不相同。 

 图用由边组成的二维数组 edges 表示，其中 edges[i] = [ui, vi, cnti] 表示原始图中节点 ui 和 vi 之间存在一条边，
cnti 是将边 细分 后的新节点总数。注意，cnti == 0 表示边不可细分。 

 要 细分 边 [ui, vi] ，需要将其替换为 (cnti + 1) 条新边，和 cnti 个新节点。新节点为 x1, x2, ..., xcnti ，新边
为 [ui, x1], [x1, x2], [x2, x3], ..., [xcnti+1, xcnti], [xcnti, vi] 。 

 现在得到一个 新的细分图 ，请你计算从节点 0 出发，可以到达多少个节点？如果节点间距离是 maxMoves 或更少，则视为 可以到达 。 

 给你原始图和 maxMoves ，返回 新的细分图中从节点 0 出发 可到达的节点数 。 

 

 示例 1： 
 
 
输入：edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
输出：13
解释：边的细分情况如上图所示。
可以到达的节点已经用黄色标注出来。
 

 示例 2： 

 
输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
输出：23
 

 示例 3： 

 
输入：edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
输出：1
解释：节点 0 与图的其余部分没有连通，所以只有节点 0 可以到达。
 

 

 提示： 

 
 0 <= edges.length <= min(n * (n - 1) / 2, 10⁴) 
 edges[i].length == 3 
 0 <= ui < vi < n 
 图中 不存在平行边 
 0 <= cnti <= 10⁴ 
 0 <= maxMoves <= 10⁹ 
 1 <= n <= 3000 
 

 Related Topics 图 最短路 堆（优先队列） 👍 148 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
from heapq import heappop, heappush


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        """ djistra 算法, 时间复杂度: O(V)*log(E) """
        # 建图
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w + 1))
            graph[v].append((u, w + 1))

        def dijstra(g: List[List], start):
            """ dijstra 求原点到各个点的最短路径 """
            dis = [float('inf')] * len(g)
            dis[start] = 0

            # 用堆, 对集合中的最短路径进行扩展
            heap = [(0, start)]
            while heap:
                # pop 最短路径点
                ulen, u = heapq.heappop(heap)
                # 如果此路径比之前走过的路径长, 终止此路径
                if ulen > dis[u]:
                    continue
                # 找寻下一个点入堆
                for v, w in graph[u]:
                    vlen = ulen + w
                    # 若到达下一个点的新路径更短, 更新它
                    if vlen < dis[v]:
                        heapq.heappush(heap, (vlen, v))
                        dis[v] = vlen
            return dis

        # dijstra 求原点到各个点的最短路径
        start = 0
        dis = dijstra(graph, start)
        # print(dis)

        # 统计图中可到达的节点数
        ans = sum(plen <= maxMoves for plen in dis)

        # 统计边上的小节点, 计算从 u 到 v, 从 v 到 u, 至多还能剩下多少步
        for u, v, cnt in edges:
            ulen, vlen = dis[u], dis[v]
            u2v, v2u = max(0, maxMoves - ulen), max(0, maxMoves - vlen)
            ans += min(u2v + v2u, cnt)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
