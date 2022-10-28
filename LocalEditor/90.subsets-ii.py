#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.cn/problems/subsets-ii/description/
#
# algorithms
# Medium (63.67%)
# Likes:    927
# Dislikes: 0
# Total Accepted:    241K
# Total Submissions: 378.5K
# Testcase Example:  '[1,2,2]'
#

question_content="""Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.


Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:


1 <= nums.length <= 10
-10 <= nums[i] <= 10


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[],]
        path = []
        def dfs(startIndex):
            if startIndex == len(nums):
                # result.append(path[:])
                return
            
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                result.append(path[:])
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return result
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

