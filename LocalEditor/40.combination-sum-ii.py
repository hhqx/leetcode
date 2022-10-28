#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.cn/problems/combination-sum-ii/description/
#
# algorithms
# Medium (60.44%)
# Likes:    1104
# Dislikes: 0
# Total Accepted:    347.7K
# Total Submissions: 575.2K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#

question_content="""Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.


Example 1:


Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]


Example 2:


Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]



Constraints:


1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

