question_content = """
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。 

 如果数组中不存在目标值 target，返回 [-1, -1]。 

 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。 

 

 示例 1： 

 
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4] 

 示例 2： 

 
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1] 

 示例 3： 

 
输入：nums = [], target = 0
输出：[-1,-1] 

 

 提示： 

 
 0 <= nums.length <= 10⁵ 
 -10⁹ <= nums[i] <= 10⁹ 
 nums 是一个非递减数组 
 -10⁹ <= target <= 10⁹ 
 

 Related Topics 数组 二分查找 👍 2266 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
# from bisect import bisect_left, bisect_right
def bisect_left(nums, tar, key=lambda x: x):
    left, right = 0, len(nums)
    while left < right:
        mid = left + right >> 1
        if key(nums[mid]) < tar:
            left = mid + 1
        else:
            right = mid
    return right


def bisect_right(nums, tar, key=lambda x: x):
    left, right = 0, len(nums)
    while left < right:
        mid = left + right >> 1
        if key(nums[mid]) <= tar:
            left = mid + 1
        else:
            right = mid
    return right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lidx = bisect_left(nums, target)
        ridx = bisect_right(nums, target) - 1

        if lidx >= len(nums) or ridx < 0 or lidx > ridx:
            return [-1, -1]
        return [lidx, ridx]


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
