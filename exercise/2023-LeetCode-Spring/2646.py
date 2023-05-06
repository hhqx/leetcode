question_content = """
2646. 最小化旅行的价格总和
现有一棵无向、无根的树，树中有 n 个节点，按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。

每个节点都关联一个价格。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价格。

给定路径的 价格总和 是该路径上所有节点的价格之和。

另给你一个二维整数数组 trips ，其中 trips[i] = [starti, endi] 表示您从节点 starti 开始第 i 次旅行，并通过任何你喜欢的路径前往节点 endi 。

在执行第一次旅行之前，你可以选择一些 非相邻节点 并将价格减半。

返回执行所有旅行的最小价格总和。

 

示例 1：


输入：n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
输出：23
解释：
上图表示将节点 2 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 、2 和 3 并使其价格减半后的树。
第 1 次旅行，选择路径 [0,1,3] 。路径的价格总和为 1 + 2 + 3 = 6 。
第 2 次旅行，选择路径 [2,1] 。路径的价格总和为 2 + 5 = 7 。
第 3 次旅行，选择路径 [2,1,3] 。路径的价格总和为 5 + 2 + 3 = 10 。
所有旅行的价格总和为 6 + 7 + 10 = 23 。可以证明，23 是可以实现的最小答案。
示例 2：


输入：
45
[[0,36],[3,37],[4,42],[9,32],[11,1],[1,24],[14,23],[16,8],[19,8],[21,6],[22,6],[6,25],[24,33],[26,18],[27,44],[33,28],[28,18],[37,23],[38,36],[36,41],[39,17],[41,10],[10,32],[32,18],[18,30],[30,15],[15,5],[5,20],[20,13],[13,2],[2,7],[7,25],[25,31],[31,12],[12,40],[40,35],[42,23],[23,35],[35,43],[43,34],[34,8],[8,17],[17,29],[29,44]]
[14,8,4,4,12,16,6,6,2,2,16,8,6,16,14,12,2,4,6,4,10,6,2,8,12,2,10,8,16,6,2,8,12,2,12,8,16,10,14,10,10,16,8,2,10]
[[4,33],[21,9],[40,35],[41,21],[18,8],[27,9],[36,11],[16,34],[39,14],[41,18]]
输出：655


输入：n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
输出：1
解释：
上图表示将节点 0 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 并使其价格减半后的树。 
第 1 次旅行，选择路径 [0] 。路径的价格总和为 1 。 
所有旅行的价格总和为 1 。可以证明，1 是可以实现的最小答案。
 

提示：

1 <= n <= 50
edges.length == n - 1
0 <= ai, bi <= n - 1
edges 表示一棵有效的树
price.length == n
price[i] 是一个偶数
1 <= price[i] <= 1000
1 <= trips.length <= 100
0 <= starti, endi <= n - 1
通过次数2,567提交次数5,443

link: https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        """ 使用差分的方式统计权重个数的话, 使用离线lcm的复杂度为:o(n+m), 暴力dfs复杂度为:o(n*m) """
        dcnt = 0

        n = len(price)
        old_price = price.copy()
        price = [0] * n

        # dfs, 树形dp
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 修改价格权重
        def dfs_m(u, end, par):
            """ dfs 求路径和 """
            nonlocal dcnt
            dcnt += 1

            # print('u',u)
            if u == end:
                # print("path", path)
                for x in path:
                    price[x] += old_price[x]
                return True
            ret = 0
            for v in g[u]:
                if v == par:
                    continue
                path.append(v)

                if dfs_m(v, end, u):
                    ret = True
                    path.pop()
                    break
                path.pop()

            return ret

        for s, end in trips:
            path = [s]
            assert dfs_m(s, end, -1), ""
        # print(price)
        total = sum(price)

        # dfs 递归bp
        @cache
        def dfs(u, flag, par):
            """ 树形打家劫舍, 树形dp """
            nonlocal dcnt
            dcnt += 1

            # print('u', u)
            ret0 = 0
            ret1 = 0
            for v in g[u]:
                if v == par:
                    continue
                r0 = dfs(v, 0, u)
                r1 = dfs(v, 1, u)

                ret0 += max(r1, r0)
                ret1 += r0

            if flag == 1:
                ret = ret1 + price[u]
            else:
                ret = ret0
            return ret

        ans = 0
        ans = max(dfs(0, 0, -1), dfs(0, 1, -1))
        print('ans', ans)
        print(total)

        print('dcnt', dcnt, 'n', len(price), 'm', len(trips))
        return total - ans // 2


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
