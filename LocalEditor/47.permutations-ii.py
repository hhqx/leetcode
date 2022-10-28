#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.cn/problems/permutations-ii/description/
#
# algorithms
# Medium (65.18%)
# Likes:    1186
# Dislikes: 0
# Total Accepted:    375.5K
# Total Submissions: 576.2K
# Testcase Example:  '[1,1,2]'
#

question_content="""Given a collection of numbers, nums, that might contain duplicates, return
all possible unique permutations in any order.


Example 1:


Input: nums = [1,1,2]
Output:
[[1,1,2],
[1,2,1],
[2,1,1]]


Example 2:


Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



Constraints:


1 <= nums.length <= 8
-10 <= nums[i] <= 10


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        flag_used = [False] * len(nums)
        def dfs(startIndex):
            if len(nums) == len(path):
                result.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not flag_used[i-1]:  # 数层上去重
                    continue
                if flag_used[i] is True:
                    continue
                flag_used[i] = True
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
                flag_used[i] = False
        
        dfs(0)
        return result
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

