#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.cn/problems/subsets/description/
#
# algorithms
# Medium (80.78%)
# Likes:    1782
# Dislikes: 0
# Total Accepted:    519.8K
# Total Submissions: 643.6K
# Testcase Example:  '[1,2,3]'
#

question_content="""Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.


Example 1:


Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


Example 2:


Input: nums = [0]
Output: [[],[0]]



Constraints:


1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[],]
        path = []
        def dfs(startIndex):
            if startIndex == len(nums):
                # result.append(path[:])
                return
            
            for i in range(startIndex, len(nums)):
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

