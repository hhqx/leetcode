#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.cn/problems/palindrome-number/description/
#
# algorithms
# Easy (56.84%)
# Likes:    2202
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '121'
#

question_content="""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.


For example, 121 is a palindrome while 123 is not.



Example 1:


Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:


Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it
becomes 121-. Therefore it is not a palindrome.


Example 3:


Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a
palindrome.



Constraints:


-2^31 <= x <= 2^31 - 1



Follow up: Could you solve it without converting the integer to a string?
"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        ans = []
        while x != 0:
            digit = x % 10
            ans.append(digit)
            x = x // 10
        
        for i in range(len(ans)//2):
            if ans[i] != ans[len(ans)-1-i]:
                return False
        return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

