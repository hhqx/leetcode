from operator import xor

question_content = """
5. 与非的谜题
通过的用户数59
尝试过的用户数85
用户总通过次数60
用户总提交次数137
题目难度Hard
在永恒之森中，封存着有关万灵之树线索的卷轴，只要探险队通过最后的考验，便可以获取前往万灵之树的线索。

探险队需要从一段不断变化的谜题数组中找到最终的密码，初始的谜题为长度为 n 的数组 arr（下标从 0 开始），数组中的数字代表了 k 位二进制数。
破解谜题的过程中，需要使用 与非（NAND） 运算方式，operations[i] = [type,x,y] 表示第 i 次进行的谜题操作信息：

若 type = 0，表示修改操作，将谜题数组中下标 x 的数字变化为 y；
若 type = 1，表示运算操作，将数字 y 进行 x*n 次「与非」操作，第 i 次与非操作为 y = y NAND arr[i%n]；
运算操作结果即：y NAND arr[0%n] NAND arr[1%n] NAND arr[2%n] ... NAND arr[(x*n-1)%n]

最后，将所有运算操作的结果按顺序逐一进行 异或（XOR）运算，从而得到最终解开封印的密码。请返回最终解开封印的密码。

注意:

「与非」（NAND）的操作为：先进行 与 操作，后进行 非 操作。
例如：两个三位二进制数2和3，其与非结果为 NOT ((010) AND (011)) = (101) = 5

示例 1：

输入:
k = 3,
arr = [1,2],
operations = [[1,2,3],[0,0,3],[1,2,2]]

输出: 2

解释：
初始的谜题数组为 [1,2]，二进制位数为 3，
第 0 次进行运算操作，将数字 3(011) 进行 2*2 次「与非」运算，
运算操作结果为 3 NAND 1 NAND 2 NAND 1 NAND 2 = 5
第 1 次进行修改操作，谜题数组的第 0 个数字变化为 3，谜题变成 [3,2]
第 2 次进行运算操作，将数字 2(010) 进行 2*2 次「与非」运算，
运算操作结果为 2 NAND 3 NAND 2 NAND 3 NAND 2 = 7
所有运算操作结果进行「异或」运算为 5 XOR 7 = 2
因此得到的最终密码为 2。

示例 2：

输入:
k = 4,
arr = [4,6,4,7,10,9,11],
operations = [[1,5,7],[1,7,14],[0,6,7],[1,6,5]]
输出: 9
解释:
初始的谜题数组为 [4,6,4,7,10,9,11],
第 0 次进行运算操作，运算操作结果为 5；
第 1 次进行运算操作，运算操作结果为 5；
第 2 次进行修改操作，修改后谜题数组为 [4, 6, 4, 7, 10, 9, 7]；
第 3 次进行运算操作，运算操作结果为 9；
所有运算操作结果进行「异或」运算为 5 XOR 5 XOR 9 = 9；
因此得到的最终密码为 9。

提示:

1 <= arr.length, operations.length <= 10^4
1 <= k <= 30
0 <= arr[i] < 2^k
若 type = 0，0 <= x < arr.length 且 0 <= y < 2^k
若 type = 1，1 <= x < 10^9 且 0 <= y < 2^k
保证存在 type = 1 的操作"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
from operator import xor

MASK = (1 << 30) - 1
def nand(a, b):
    return ~(a & b)
def And(a, b):
    return a & b & MASK
def Or(a, b):
    return a | b
class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = self.add = 0

F = nand
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

MAX = int(10**4)
# class MyCalendarTwo:
#
#     def __init__(self):
#         self.rt = SegmentTree().root
#
#     def book(self, start: int, end: int) -> bool:
#         # if SegmentTree.query(self.rt, 0, MAX, start, end - 1) < 2:
#         #     SegmentTree.update(self.rt, 0, MAX, start, end - 1, 1)
#         #     return True
#         # return False
#
#         SegmentTree.update(self.rt, 0, MAX, start, end - 1, 1)

class Solution:
    def getNandResult(self, k: int, arr: List[int], operations: List[List[int]]) -> int:
        mask = (1 << k) - 1
        n = len(arr)
        # obj = class_segment(0, n+1)
        obj = SegmentTree().root
        for i in range(n):
            # obj.update(i, arr[i])
            # obj.update(i, arr[i])
            SegmentTree.update(obj, 0, MAX, i-1, i, ~arr[i])
        for i in range(n):
            val = SegmentTree.query(obj, 0, MAX, i-1, i)
            tar = ~arr[i]
            assert val == tar, "error"

        result = []
        for op, x, y in operations:
            if op == 0:
                # arr[x] = y
                # obj.update(x, y)
                # obj.update(x, ~y)
                SegmentTree.update(obj, 0, MAX, x, x, ~y)
            else:
                # ret = y
                # x = 1  # 等价
                # for i in range(x * n):
                #     ret = nand(ret, arr[i % n])
                # ret = obj.get(0, n)
                ret = SegmentTree.query(obj, 0, MAX, 0, n-1)
                result.append(ret)

        ret = result[0]
        for i in range(1, len(result)):
            ret = ret ^ result[i]
        ans = ret & mask
        print(result)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
