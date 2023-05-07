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

输入：
5
[27,31,31,15,15,27,27,11,15]
[[1,10,1],[0,5,4],[0,0,12],[0,7,28],[1,10,4],[0,8,29],[1,8,7],[0,1,4],[0,2,24],[1,10,13]]
输出：
5

输入：
3
[1,1,5,5,5,1,5,5]
[[1,10,1],[1,8,6],[0,0,1],[1,9,2],[0,6,7],[0,0,7],[1,10,0],[1,9,0]]
输出：
7


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


class Solution:
    def getNandResult(self, k: int, arr: List[int], operations: List[List[int]]) -> int:
        """ 暴力模拟 """
        mask = (1 << k) - 1

        def nand(a, b):
            return mask - (a & b)

        n = len(arr)
        result = []
        for op, x, y in operations:
            if op == 0:
                arr[x] = y
            else:
                ret = y
                for i in range(x * n):
                    ret = nand(ret, arr[i % n])
                result.append(ret)

        ret = result[0]
        for i in range(1, len(result)):
            ret = ret ^ result[i]
        ans = ret
        print(result)
        return ans

from sortedcontainers import SortedList
class class_nand:
    def __init__(self, nums, k):
        self.k = k
        self.n = len(nums)
        self.bits = [SortedList(idx for idx, x in enumerate(nums) if not (x >> i & 1)) for i in range(k)]

    def update(self, idx, x):
        for i in range(self.k):
            zero_arr = self.bits[i]
            is_bit0 = not (x >> i & 1)
            # 二分查找, 判断是否存idx
            res = zero_arr.bisect_left(idx)
            if res < len(zero_arr) and zero_arr[res] == idx:
                if is_bit0:
                    pass
                else:
                    zero_arr.remove(idx)
            else:
                if is_bit0:
                    zero_arr.add(idx)
    def query(self, idx):
        ret = 0
        # !这里需要注意移位赋值时需要从高往低输入
        for i in range(self.k-1, -1, -1):
            zero_arr = self.bits[i]
            # 二分查找, 判断是否存idx
            res = zero_arr.bisect_left(idx)
            if res < len(zero_arr) and zero_arr[res] == idx:
                ret = (ret << 1) | 0
            else:
                ret = (ret << 1) | 1
        return ret
    def get(self, repeat=1, initial=None) -> int:
        """ 计算 nand 结果, 计算最后连续1的个数 """
        init_bit = [initial >> i & 1 for i in range(self.k)] if initial is not None else []
        ans = []
        for i in range(self.k):
            zero_arr = self.bits[i]
            last = zero_arr[-1] if len(zero_arr) else -1
            cnt = self.n-1 - last
            ans.append(cnt)

        # convert to int
        # !这里需要注意移位赋值时需要从高往低输入
        ret = 0
        for i in range(self.k-1, -1, -1):
            cnt = ans[i]
            # 这里的判断条件很关键, 画真值表判断得出结论
            # if cnt == 0:  # 该条件情况可以被下面的方式涵盖
            #     bit = 1
            # else:
            if cnt == self.n:
                cnt *= repeat
                cnt += init_bit[i]

                bit = cnt % 2 == 1
            else:
                bit = cnt % 2 == 0

            ret <<= 1
            ret |= bit
        return ret

class Solution:
    def getNandResult(self, k: int, arr: List[int], operations: List[List[int]]) -> int:
        """
        动态更新, 动态查询, 单点更新, 区间查询
        根据 nand 性质拆解, 统计每位最后一个bit0的位置
        SortedList 动态查询最后一个bit0的位置(也即动态查询最后一段连续bit1的个数)
        """
        mask = (1 << k) - 1

        def nand(a, b):
            return mask - (a & b)

        n = len(arr)
        obj = class_nand(arr, k)
        for i in range(n):
            q = obj.query(i)
            tar = arr[i]
            assert q == tar, ""

        result = []
        for op, x, y in operations:
            if op == 0:
                arr[x] = y
                obj.update(x, y)
            else:
                # ret = y
                # for i in range(x * n):
                #     ret = nand(ret, arr[i % n])
                ret2 = obj.get(repeat=x, initial=y)
                # assert ret == ret2, ""
                result.append(ret2)

        ret = result[0]
        for i in range(1, len(result)):
            ret = ret ^ result[i]
        ans = ret
        print(result)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
