# coding=utf-8
question_content = """
English description is not available for the problem. Please switch to Chinese.
 Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序 👍 1003 👎 0

测试用例:[1,2,1,2,1]
测试结果:4
期望结果:3


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)

class bit_tree:
    def __init__(self, M, N):
        self.sz = N - M + 1
        self.M = M
        self.arr = [0] * (self.sz + 1)

    def add(self, x, val):
        idx = x - self.M + 1
        while idx < len(self.arr):
            self.arr[idx] += val
            idx += idx & -idx

    def query(self, x):
        idx = x - self.M + 1
        ans = 0
        while idx > 0:
            ans += self.arr[idx]
            idx -= idx & -idx
        return ans

    def update(self, x, val):
        self.add(x, val - self.query(x) + self.query(x - 1))


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """ 树状数组逆序对个数 """
        posi = list(sorted(range(len(nums)), key=lambda x: nums[x]))
        obj = bit_tree(0, len(nums))

        # for i in range(len(nums)):
        #     obj.add(i, 1)
        # print(posi)

        ans = 0
        for i in range(len(nums)):
            # val = obj.query(posi[i]-1)
            # obj.update(posi[i], 0)
            val = obj.query(posi[i] - 1) + posi[i]
            obj.add(posi[i], -1)

            ans += val

        return ans


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """ 归并排序求数组逆序对个数 """
        ans = 0
        def merge(a: List[int], b: List[int]):
            """ 合并有序列表 """
            nonlocal ans
            ret = []
            j = 0
            for i in range(len(a)):
                while j < len(b) and b[j] < a[i]:
                    ret.append(b[j])
                    j += 1
                ret.append(a[i])
                # 累加当前 a, b 区间内的逆序对个数
                ans += j
            for i in range(j, len(b)):
                ret.append(b[i])
            return ret

        def dfs(l, r):
            if r - l <= 1:
                return nums[l:r]
            mid = l + r >> 1
            left = dfs(l, mid)
            right = dfs(mid, r)
            ret = merge(left, right)
            return ret

        dfs(0, len(nums))
        return ans

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
