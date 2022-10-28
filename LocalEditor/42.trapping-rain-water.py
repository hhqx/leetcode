#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (62.02%)
# Likes:    3807
# Dislikes: 0
# Total Accepted:    575.1K
# Total Submissions: 927.1K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#

question_content="""Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.


Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.


Example 2:


Input: height = [4,2,0,3,2,5]
Output: 9



Constraints:


n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        return
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

