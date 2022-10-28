#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] Increasing Subsequences
#
# https://leetcode.cn/problems/increasing-subsequences/description/
#
# algorithms
# Medium (52.76%)
# Likes:    514
# Dislikes: 0
# Total Accepted:    99.5K
# Total Submissions: 188.6K
# Testcase Example:  '[4,6,7,7]'
#

question_content="""Given an integer array nums, return all the different possible increasing
subsequences of the given array with at least two elements. You may return
the answer in any order.

The given array may contain duplicates, and two equal integers should also be
considered a special case of increasing sequence.


Example 1:


Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]


Example 2:


Input: nums = [4,4,3,2,1]
Output: [[4,4]]



Constraints:


1 <= nums.length <= 15
-100 <= nums[i] <= 100


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        
        def dfs(startIndex):

            if len(path) >= 2:
                    result.append(path[:])
            
            if startIndex == len(nums):
                return
            
            # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
            # usedSet = set()
            for i in range(startIndex, len(nums)):
                # 组合子集去重
                if nums[i] in nums[startIndex:i]:
                    continue

                # 筛选递增子序列
                if len(path) > 0 and nums[i] < path[-1]:
                    continue

                # usedSet.add(nums[i])
                path.append(nums[i])
                
                dfs(i + 1)
                path.pop()
            
        dfs(0)
        return result
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

