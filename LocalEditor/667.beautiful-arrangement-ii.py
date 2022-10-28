#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] Beautiful Arrangement II
#
# https://leetcode.cn/problems/beautiful-arrangement-ii/description/
#
# algorithms
# Medium (65.86%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 39.4K
# Testcase Example:  '3\n1'
#

question_content="""Given two integers n and k, construct a list answer that contains n different
positive integers ranging from 1 to n and obeys the following
requirement:


Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 -
a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct
integers.


Return the list answer. If there multiple valid answers, return any of
them.


Example 1:


Input: n = 3, k = 1
Output: [1,2,3]
Explanation: The [1,2,3] has three different positive integers ranging from 1
to 3, and the [1,1] has exactly 1 distinct integer: 1


Example 2:


Input: n = 3, k = 2
Output: [1,3,2]
Explanation: The [1,3,2] has three different positive integers ranging from 1
to 3, and the [2,1] has exactly 2 distinct integers: 1 and 2.



Constraints:


1 <= k < n <= 10^4


"""

from typing import *
from RunLeetCodeInPycharm import StartTest

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        return 

# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()




