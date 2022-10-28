#
# @lc app=leetcode.cn id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#
# https://leetcode.cn/problems/maximum-ascending-subarray-sum/description/
#
# algorithms
# Easy (67.20%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    25.1K
# Total Submissions: 36.2K
# Testcase Example:  '[10,20,30,5,10,50]'
#

question_content="""Given an array of positive integers nums, return the maximum possible sum of
an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is
ascending.


Example 1:


Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of
65.


Example 2:


Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum
of 150.


Example 3:


Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of
33.



Constraints:


1 <= nums.length <= 100
1 <= nums[i] <= 100


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        left, right = 0, 1
        sum = nums[0]
        ans = sum
        while right < len(nums):
            if nums[right-1] < nums[right]:
                sum += nums[right]
                right += 1
            else:
                sum = nums[right]
                right += 1
                # break
            ans = max(sum, ans)
        return ans
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

