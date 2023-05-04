question_content = """
给你一个包含若干 互不相同 整数的数组 nums ，你需要执行以下操作 直到数组为空 ： 

 
 如果数组中第一个元素是当前数组中的 最小值 ，则删除它。 
 否则，将第一个元素移动到数组的 末尾 。 
 

 请你返回需要多少个操作使 nums 为空。 

 

示例 1： 


输入：nums = [3,4,-1]
输出：5


示例 2： 

输入：nums = [1,2,4,3]
输出：5


示例 3： 

 
输入：nums = [1,2,3]
输出：3


 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 -109 <= nums[i] <= 10⁹ 
 nums 中的元素 互不相同 。 
 

 Related Topics 贪心 树状数组 线段树 数组 二分查找 有序集合 排序 👍 18 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
def lower_bit(x):
    return x & -x


class bit_tree:
    def __init__(self, M, N):
        sz = N - M + 1
        self.arr = [0] * (sz + 1)
        self.M = M

    def add(self, x, val):
        idx = x - self.M + 1
        while idx < len(self.arr):
            # print('idx', idx)
            self.arr[idx] += val
            idx += lower_bit(idx)

    def query(self, x):
        idx = x - self.M + 1
        ans = 0
        while idx > 0:
            ans += self.arr[idx]
            idx -= lower_bit(idx)
        return ans

    def update(self, x, val):
        ori = self.query(x) - self.query(x - 1)
        self.add(x, val - ori)


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        """ bit_tree + argsort """
        obj = bit_tree(0, len(nums) - 1)
        for i in range(len(nums)):
            obj.add(i, 1)

        ans, n = 0, len(nums)
        # posi = [idx for num, idx in sorted((num, i) for i, num in enumerate(nums))]
        posi = list(sorted(range(n), key=nums.__getitem__))

        last = -1
        for i in range(0, n):
            if posi[i] > last:
                val = obj.query(posi[i]) - obj.query(last)
            else:
                val = obj.query(len(nums) - 1) - obj.query(last) + obj.query(posi[i]) - obj.query(-1)

            obj.update(posi[i], 0)
            last = posi[i]
            ans += val

        return ans

    # leetcode submit region end(Prohibit modification and deletion)


# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
