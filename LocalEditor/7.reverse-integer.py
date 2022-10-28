#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.cn/problems/reverse-integer/description/
#
# algorithms
# Medium (35.37%)
# Likes:    3630
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 3.1M
# Testcase Example:  '123'
#

question_content="""Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or
unsigned).


Example 1:


Input: x = 123
Output: 321


Example 2:


Input: x = -123
Output: -321


Example 3:


Input: x = 120
Output: 21



Constraints:


-2^31 <= x <= 2^31 - 1


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        return int(str(x)[::-1])

# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

