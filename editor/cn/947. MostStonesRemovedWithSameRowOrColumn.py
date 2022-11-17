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

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """ 邻接表保存图, dfs 遍历求连通域 """
        n = len(stones)
        # 邻接表保存边, o(n*n) 建图
        edge = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    edge[i].append(j)
                    edge[j].append(i)

        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)

        # dfs 遍历所有点
        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)

        return n - num


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """ 哈希保存每个行列, 每个行列只连接到起始点上 """
        n = len(stones)
        # 邻接表保存边, o(n) 建图
        edge = defaultdict(list)
        # 哈希表保存行列第一次出现的节点,
        d = defaultdict(int)
        for i in range(n):
            keyx, keyy = (0, stones[i][0]), (1, stones[i][1])
            # 若该行有节点, 连接到它, 否则在该行记录下当前节点
            if keyx in d:
                j = d[keyx]
                edge[i].append(j)
                edge[j].append(i)
            else:
                d[keyx] = i

            # 若该列有节点, 连接到它
            if keyy in d:
                j = d[keyy]
                edge[i].append(j)
                edge[j].append(i)
            else:
                d[keyy] = i

        # # o(n) 建图, 先把同行或同列的节点保存到一个集合, 再连接到一起
        # d = defaultdict(list)
        # for i in range(len(stones)):
        #     x, y = stones[i]
        #     d[(0, x)].append(i)
        #     d[(1, y)].append(i)
        # # 连接一个集合里面的节点
        # for nodes in d.values():
        #     start = nodes[0]
        #     for node in nodes[1:]:
        #         edge[start].append(node)
        #         edge[node].append(start)

        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)

        # dfs 遍历所有点
        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)

        return n - num


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


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
