from typing import *

class SegmentTree:
    def __init__(self, nums, func):
        n = len(nums)
        # f记录的是特定区间，f[k]，序号为k的点：该节点掌管的索引为l,r，值区间l~r的数字总和
        self.nums = [0] + nums  # 加一个哨兵节点，使得数组的有效索引为1～n
        self.f = [0 for i in range(4 * n)]
        self.func = func
        self.buildTree(1, 1, n)


    def buildTree(self, k, l, r):
        # 序号为k的索引，掌管的范围是l~r
        # 这里要注意，对于一棵数组长度确定的线段树，k是可以唯一确定l,r的
        # 例如根节点1 一定对应 1~n
        # 即同一个k对应唯一的l,r
        if l == r:
            # 叶子节点
            self.f[k] = self.nums[l]
            return
        mid = (l + r) // 2
        # 分治 + 后序遍历的思想
        self.buildTree(2 * k, l, mid)  # 处理左孩子
        self.buildTree(2 * k + 1, mid + 1, r)  # 处理右孩子
        # self.f[k] = self.f[2 * k] + self.f[2 * k + 1]  # 父节点的信息为左右孩子汇总
        self.f[k] = self.func(self.f[2 * k], self.f[2 * k + 1])  # 父节点的信息为左右孩子汇总

    def update(self, k, l, r, i, x):
        # 序号为k的索引，掌管的范围是l~r
        # 对数组索引为i的节点增量更新x
        self.f[k] += x
        if l == r:
            # 叶子节点
            return
        mid = (l + r) // 2
        # 看索引i在左右子树的哪一边。递归更新
        if i <= mid:  # 在左子树
            self.update(2 * k, l, mid, i, x)
        elif i > mid:  # 在右子树
            self.update(2 * k + 1, mid + 1, r, i, x)

    def query(self, k, l, r, start, end):
        # start~end始终是l~r的子区间
        # 序号为k的索引，掌管的范围是l~r
        # 在整棵树上进行搜寻 start~end 索引所汇总的范围和
        if l == start and r == end:
            return self.f[k]
        mid = (l + r) // 2
        if end <= mid:  # 如果start~end完全在左半边，则只需要算左子树
            return self.query(2 * k, l, mid, start, end)
        if mid < start:  # 如果start~end完全在右半边，则只需要算右子树
            return self.query(2 * k + 1, mid + 1, r, start, end)
        # 否则，需要同时考虑左右孩子
        leftPart = self.query(2 * k, l, mid, start, mid)  # 注意：在这里最后一个参数是mid而不是end
        rightPart = self.query(2 * k + 1, mid + 1, r, mid + 1, end)  # 注意：在这里倒数第二个参数是mid+1而不是start
        # 因为：# start~end始终是l~r的子区间，否则递归会没有出口
        # return leftPart + rightPart
        return self.func(leftPart, rightPart)


class NumArray:
    def __init__(self, nums: List[int], func=None):
        self.st = SegmentTree(nums, func)
        self.nums = nums
        for i in range(len(nums)):
            self.update(i, nums[i])

        # 牢记，在这种建树模式下，一个k唯一确定l和r

    def update(self, index: int, val: int) -> None:
        # delta = val - self.nums[index]  # 增量更新
        # self.nums[index] = val
        self.st.update(1, 1, len(self.nums), index + 1, val)

    def get(self, left: int, right: int) -> int:
        return self.st.query(1, 1, len(self.nums), left + 1, right + 1)


def sum(a, b):
    return a + b
def And(a, b):
    return a & b
def Or(a, b):
    return a | b
class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = self.add = 0

F = sum
F = And
F = Or

class SegmentTree:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: int) -> None:
        if l <= lc and rc <= r:
            node.add += v
            node.val += v
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)

    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> int:
        if l <= lc and rc <= r:
            return node.val
        # 先确保所有关联的懒标记下沉下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, 0
        if l <= mid:
            ans = SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同样为不同题目中的更新方式
            ans = F(ans, SegmentTree.query(node.rs, mid + 1, rc, l, r))
        return ans

    @staticmethod
    def pushdown(node: Node) -> None:
        # 懒标记, 在需要的时候才开拓节点和赋值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if not node.add:
            return
        node.ls.add += node.add
        node.rs.add += node.add
        node.ls.val += node.add
        node.rs.val += node.add
        node.add = 0

    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为最大值
        # node.val = max(node.ls.val, node.rs.val)
        # node.val = nand(node.ls.val, node.rs.val)
        node.val = F(node.ls.val, node.rs.val)