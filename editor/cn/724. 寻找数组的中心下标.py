import itertools

question_content = """
给你一个整数数组 nums ，请计算数组的 中心下标 。 

 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。 

 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。 

 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。 

 

示例 1： 
测试用例:
[-1,-1,0,1,1,0]

期望结果:
5


输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
 

 示例 2： 

 
输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。 

 示例 3： 

 
输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。 

 

 提示： 

 
 1 <= nums.length <= 10⁴ 
 -1000 <= nums[i] <= 1000 
 

 

 注意：本题与主站 1991 题相同：https://leetcode-cn.com/problems/find-the-middle-index-in-
array/ 

 Related Topics 数组 前缀和 👍 530 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        p = list(itertools.accumulate(nums, initial=0))
        ans = -1
        for i in range(n):
            lval = p[i]
            rval = p[-1] - p[i+1]
            if lval == rval:
                return i
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
