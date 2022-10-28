import bisect
import collections
from collections import defaultdict

question_content = """
有一棵 n 个节点的无向树，节点编号为 0 到 n - 1 。

给你一个长度为 n 下标从 0 开始的整数数组 nums ，其中 nums[i] 表示第 i 个节点的值。同时给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 与 bi 之间有一条边。

你可以 删除 一些边，将这棵树分成几个连通块。一个连通块的 价值 定义为这个连通块中 所有 节点 i 对应的 nums[i] 之和。

你需要删除一些边，删除后得到的各个连通块的价值都相等。请返回你可以删除的边数 最多 为多少。

 

示例 1：

[6,2,2,2,6]
[[0,1],[1,2],[1,3],[3,4]]

输入：nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]] 
输出：2 
解释：上图展示了我们可以删除边 [0,1] 和 [3,4] 。得到的连通块为 [0] ，[1,2,3] 和 [4] 。每个连通块的价值都为 6 。可以证明没有别的更好的删除方案存在了，所以答案为 2 。
示例 2：

输入：nums = [1,2,1,1,1], edges = [[0,1],[1,3],[3,4],[4,2]]
输出：1


# 输入：nums = [2], edges = []
# 输出：0
解释：没有任何边可以删除。
 

提示：

1 <= n <= 2 * 104
nums.length == n
1 <= nums[i] <= 50
edges.length == n - 1
edges[i].length == 2
0 <= edges[i][0], edges[i][1] <= n - 1
edges 表示一棵合法的树。
通过次数924提交次数1,588

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/create-components-with-same-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedList
def print(*args, **kwargs):
    return
class Solution:
    """ 2022年10月17日00:54:21 """
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        def get_factors(n):
            """ 输入n, 返回n的因数 """
            N = int(n ** (0.5))
            ans = []
            for i in range(1, N+1):
                if n % i == 0:
                    ans += [i, n // i]
            if N * N == n:
                ans.pop()
            # ans.sort(reverse=True)
            ans.sort()
            return ans

        # print(get_factors(9))

        # 枚举数组和的所有因子
        total = sum(nums)
        # print(get_factors(total))
        ans = 0

        # 计算node度
        degree = [0] * len(nums)
        for i, o in edges:
            degree[i] += 1
            degree[o] += 1

        # 统计度为1的node
        # q = [i for i, d in enumerate(degree) if d == 1]

        deque = collections.deque()
        deque.extend([i for i, d in enumerate(degree) if d == 1])

        # dic = defaultdict(list)
        # for i, o in edges:
        #     dic[i].append(o)
        #     dic[o].append(i)
        dic = defaultdict(SortedList)
        for i, o in edges:
            dic[i].add(o)
            dic[o].add(i)

        # dic = [[0] * len(nums) for _ in range(len(nums))]
        # for i, o in edges:
        #     dic[i][0] = True
        #     dic[o][i] = True

        for factor in get_factors(total):

            # # 计算node度
            # degree = [0] * len(nums)
            # for i, o in edges:
            #     degree[i] += 1
            #     degree[o] += 1

            # 统计度为1的node
            # q = [i for i, d in enumerate(degree) if d == 1]
            q = deque.copy()
            # 计算节点连接关系
            # d = defaultdict(list)
            # for i, o in edges:
            #     d[i].append(o)
            #     d[o].append(i)

            # d = [dic[i].copy() for i in range(len(nums))]
            d = {k: v.copy() for k, v in dic.items()}

            # 广度遍历
            def bfs(nums, factor):
                ans = 0
                flag = 1
                cnt = 0
                print('\n\n', q, factor)
                while q and flag:
                    for _ in range(len(q)):
                        idx = q.popleft()
                        # 如果当前节点值等于因数, 则划分
                        print('cnt', cnt)
                        print(d)
                        print('idx', idx, nums[idx])

                        if cnt == len(nums)-1:
                            if nums[idx] == factor:
                                return ans
                            else:
                                return None

                        next = d[idx][0]  # 当前节点有且仅有一个节点

                        if nums[idx] == factor:
                            ans += 1

                        elif nums[idx] < factor:
                            # 将当前节点的值汇聚到上一层
                            nums[next] += nums[idx]
                        else:
                            # 如果当前节点值大于因数, 循环终止, 不存在价值相同划分
                            return None
                        # 移除该边的连接
                        # d[next].remove(idx)
                        del d[next][bisect.bisect_left(d[next], idx)]
                        # 如果移除后度为1, 加入队列q
                        if len(d[next]) == 1:
                            q.append(next)
                        cnt += 1
                return ans
            ans = bfs(nums[:], factor)
            # ans = bfs(nums)
            if ans:
                break

        # print((total / factor - 1), ans)
        return ans if ans else 0

class Solution1:
    """ 2022年10月17日00:54:21 """
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        def get_factors(n):
            """ 输入n, 返回n的因数 """
            N = int(n ** (0.5))
            ans = []
            for i in range(1, N+1):
                if n % i == 0:
                    ans += [i, n // i]
            if N * N == n:
                ans.pop()
            # ans.sort(reverse=True)
            ans.sort()
            return ans

        print(get_factors(9))

        # 枚举数组和的所有因子
        total = sum(nums)
        print(get_factors(total))
        ans = 0

        # 计算node度
        degree = [0] * len(nums)
        for i, o in edges:
            degree[i] += 1
            degree[o] += 1

        # 统计度为1的node
        # q = [i for i, d in enumerate(degree) if d == 1]

        deque = collections.deque()
        deque.extend([i for i, d in enumerate(degree) if d == 1])

        dic = defaultdict(list)
        for i, o in edges:
            dic[i].append(o)
            dic[o].append(i)

        for factor in get_factors(total):

            # 计算node度
            degree = [0] * len(nums)
            for i, o in edges:
                degree[i] += 1
                degree[o] += 1

            # 统计度为1的node
            # q = [i for i, d in enumerate(degree) if d == 1]
            q = deque.copy()
            # 计算节点连接关系
            d = defaultdict(list)
            for i, o in edges:
                d[i].append(o)
                d[o].append(i)
            # d = dic.copy()

            # 广度遍历
            def bfs(nums, factor):
                ans = 0
                flag = 1
                cnt = 0
                print('\n\n', q, factor)
                while q and flag:
                    for _ in range(len(q)):
                        idx = q.popleft()
                        # 如果当前节点值等于因数, 则划分
                        print('cnt', cnt)
                        print(d)
                        print('idx', idx, nums[idx])

                        if cnt == len(nums)-1:
                            if nums[idx] == factor:
                                return ans
                            else:
                                return None

                        next = d[idx][0]  # 当前节点有且仅有一个节点

                        if nums[idx] == factor:
                            ans += 1

                        elif nums[idx] < factor:
                            # 将当前节点的值汇聚到上一层
                            nums[next] += nums[idx]
                        else:
                            # 如果当前节点值大于因数, 循环终止, 不存在价值相同划分
                            return None
                        # 移除该边的连接
                        d[next].remove(idx)
                        # 如果移除后度为1, 加入队列q
                        if len(d[next]) == 1:
                            q.append(next)
                        cnt += 1
                return ans
            ans = bfs(nums[:], factor)
            # ans = bfs(nums)
            if ans:
                break

        # print((total / factor - 1), ans)
        return ans


class Solution1:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        def get_factors(n):
            """ 输入n, 返回n的因数 """
            N = int(n ** (0.5))
            ans = []
            for i in range(1, N):
                if n % i == 0:
                    ans += [i, n // i]
            if n % N == 0:
                ans.append(N)
            # ans.sort(reverse=True)
            ans.sort()
            return ans

        # print(get_factors(18))

        # 枚举数组和的所有因子
        total = sum(nums)
        ans = 0
        # for factor in get_factors(total):
        for factor in [6]:

            # 计算node度
            degree = [0] * len(nums)
            for i, o in edges:
                degree[i] += 1
                degree[o] += 1

            # 统计度为1的node
            q = [i for i, d in enumerate(degree) if d == 1]
            # 计算节点连接关系
            d = defaultdict(list)
            for i, o in edges:
                d[i].append(o)
                d[o].append(i)

            # 广度遍历
            flag = 1
            while q and flag:
                print(q, factor)
                for _ in range(len(q)):
                    idx = q.pop(0)
                    # 如果当前节点值等于因数, 则划分
                    print(d, q)
                    print('idx', idx, nums[idx])
                    # if len(q) == 0:
                    #     if nums[idx] == factor:
                    #         # ans += 1
                    #         pass
                    #     else:
                    #         flag = 0
                    #     break
                    next = d[idx][0]  # 当前节点有且仅有一个节点

                    if nums[idx] == factor:
                        ans += 1

                    elif nums[idx] < factor:
                        # 将当前节点的值汇聚到上一层
                        nums[next] += nums[idx]
                    else:
                        # 如果当前节点值大于因数, 循环终止, 不存在价值相同划分
                        flag = 0
                        break
                    # 移除该边的连接
                    d[next].remove(idx)
                    d[idx].remove(next)
                    print(f'remove {next}->{idx}')
                    # 如果移除后度为1, 加入队列q
                    if len(d[next]) == 1:
                        print(nums[next])
                        q.append(next)
                    if len(q) == 1:
                        break
            if flag == 1:
                # 如果已经找到最大分划,退出
                break
            else:
                ans = 0

        # print((total / factor - 1), ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
