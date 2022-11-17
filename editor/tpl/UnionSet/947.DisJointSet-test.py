# %%
question_content = """
On a 2D plane, we place n stones at some integer coordinate points. Each 
coordinate point may have at most one stone. 

 A stone can be removed if it shares either the same row or the same column as 
another stone that has not been removed. 

 Given an array stones of length n where stones[i] = [xi, yi] represents the 
location of the iᵗʰ stone, return the largest possible number of stones that can 
be removed. 

 
 Example 1: 
测试用例:[[4,4],[5,5],[3,1],[1,4],[1,1],[2,3],[0,3],[2,4],[3,5]]
测试结果:7
期望结果:8
 
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another 
stone still on the plane.
 

 Example 2: 

 
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column 
with another stone still on the plane.
 

 Example 3: 

 
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

 
 Constraints: 

 
 1 <= stones.length <= 1000 
 0 <= xi, yi <= 10⁴ 
 No two stones are at the same coordinate point. 
 

 Related Topics 深度优先搜索 并查集 图 👍 294 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)

class DisjointSetUnion:
    def __init__(self):
        # 记录每个节点的父节点
        self.father = dict()
        # rank, 记录根节点的深度信息
        self.rank = dict()

    def find_(self, x: int) -> int:
        """ 找到当前节点的根节点, 若不存在, 创建它 """
        # 如果未收录该节点, 创建该节点, 让他指向自己, 设置层数为1
        if x not in self.father:
            self.father[x] = x
            self.rank[x] = 1
            return x

        # 如果指向自己, 说明找到了根节点
        while self.father[x] != x:
            # 若不指向自己, 则指针往上移动到父节点
            x = self.father[x]
        return x

    def find(self, x: int) -> int:
        """ 找到当前节点的根节点, 让当前节点指向根节点, 若不存在, 创建它 """
        # 如果未收录该节点, 创建该节点, 让他指向自己, 设置层数为1
        if x not in self.father:
            self.father[x] = x
            self.rank[x] = 1
            return x

        # 如果指向自己, 说明找到了根节点
        if self.father[x] == x:
            return x

        # 若不指向自己, 则递归查找根节点
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def unionSet(self, x: int, y: int):
        """ 带秩合并两个节点, 不带秩合并可能会出现超长链, 导致递归路径压缩时超过递归层数 """
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        # rx 的层数需要大于等于 ry 的层数
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        # rx 的层数 += ry 的层数, 当 rx 和 ry 的秩相同时, 合并后的秩加1
        self.rank[rx] = max(self.rank[rx], self.rank[ry]+1)
        # ry -> rx, ry 指向 rx
        self.father[ry] = rx

    def numberOfConnectedComponent(self) -> int:
        return sum(1 for x, fa in self.father.items() if x == fa)

    def count_ave_depth(self):
        dep = []
        for node in self.father:
            cnt = 1
            while node != self.father[node]:
                node = self.father[node]
                cnt += 1
            dep.append(cnt)
        ave = sum(dep) / len(dep)
        print(Counter(self.rank.values()))
        print(Counter(dep))
        print('average depth: ', ave)
        return ave

class DisjointSetUnion:
    def __init__(self):
        self.f = dict()
        self.rank = dict()

    def find(self, x: int) -> int:
        if x not in self.f:
            self.f[x] = x
            self.rank[x] = 1
            return x
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] = max(self.rank[fx], self.rank[fy] + 1)
        self.f[fy] = fx

    def numberOfConnectedComponent(self) -> int:
        return sum(1 for x, fa in self.f.items() if x == fa)


class DisjointSetUnion2:
    """ 不加rank, 会造出来超长链 """
    def __init__(self):
        self.f = dict()
        # self.rank = dict()

    def find(self, x: int) -> int:
        if x not in self.f:
            self.f[x] = x
            # self.rank[x] = 1
            return x
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        # if self.rank[fx] < self.rank[fy]:
        #     fx, fy = fy, fx
        # self.rank[fx] = max(self.rank[fx], self.rank[fy]+1)
        self.f[fy] = fx

    def numberOfConnectedComponent(self) -> int:
        return sum(1 for x, fa in self.f.items() if x == fa)



def Timing(f):
    """
    函数装饰器，用于显示函数运行时间
    """
    def rf(*args, **kwargs):
        import time
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print("function:'%s'" %f.__name__,'consumes {}ms'.format((end_time - start_time) * 1000))
        return result

    return rf



class Solution:

    def removeStones(self, stones: List[List[int]]) -> int:
        @Timing
        def f1():
            dsu = DisjointSetUnion()
            for x, y in stones:
                dsu.unionSet(x, y + 10001)
            return len(stones) - dsu.numberOfConnectedComponent()

        @Timing
        def f2():
            dsu = DisjointSetUnion2()
            for x, y in stones:
                dsu.unionSet(x, y + 10001)
            return len(stones) - dsu.numberOfConnectedComponent()

        ans = f1()
        f2()
        return ans

npairs = 9000
# npairs = 50
# ans = []
# for i in range(npairs):
#     ans.append([2*i, 2*i + 1])
#     ans.append([2*i + 2, 2*i + 1])

ans = [[i, i] for i in range(npairs)]
ans += [[i+1, i] for i in range(npairs)]
# ans[-1] = [npairs+10, 0]

# print(ans)

ret = Solution().removeStones(ans)
print(ret)
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

# if __name__ == "__main__":
#     TestObj = StartTest(question_content, Solution)
#     TestObj.run_test()
