#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.cn/problems/permutations/description/
#
# algorithms
# Medium (78.75%)
# Likes:    2216
# Dislikes: 0
# Total Accepted:    719.1K
# Total Submissions: 913.2K
# Testcase Example:  '[1,2,3]'
#

question_content="""Given an array nums of distinct integers, return all the possible
permutations. You can return the answer in any order.

Input: nums = [1,1,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:


1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        result = []
        path = []
        def dfs(startIndex):
            if len(nums) == len(path):
                result.append(path[:])
                return
            
            for i in range(startIndex, len(nums)+startIndex):
                if nums[i%len(nums)] in path:
                    continue
                path.append(nums[i%len(nums)])
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return result
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

