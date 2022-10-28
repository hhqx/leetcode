#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.cn/problems/two-sum/description/
#
# algorithms
# Easy (52.81%)
# Likes:    15265
# Dislikes: 0
# Total Accepted:    3.8M
# Total Submissions: 7.2M
# Testcase Example:  '[2,7,11,15]\n9'
#

question_content="""Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.


Example 1:


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:


Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:


Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:


2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.



Follow-up: Can you come up with an algorithm that is less than O(n^2) time
complexity?
"""

from typing import *
from RunLeetCodeInPycharm import StartTest

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return 
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()




