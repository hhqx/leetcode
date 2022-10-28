#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (37.13%)
# Likes:    5716
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 3.2M
# Testcase Example:  '"babad"'
#

question_content="""Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the
same as the original string.


Example 1:


Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


Example 2:


Input: s = "cbbd"
Output: "bb"



Constraints:


1 <= s.length <= 1000
s consist of only digits and English letters.


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def maxRange(a, b, f=lambda x: x[1]-x[0]):
            if f(a)>=f(b):
                return a
            else:
                return b

        ans = (0, 0)
        for i in range(len(s)-1):
            j = i+1
            while j < len(s) and 2*i-j >= 0 and s[j] == s[2*i-j]:
                # ans = max(ans, j-(2*i-j)+1)
                ans = maxRange(ans, (2*i-j, j))
                j += 1
            
            j = i+1
            while j < len(s) and 2*i+1-j >= 0 and s[j] == s[2*i+1-j]:
                ans = maxRange(ans, (2*i-j+1, j))
                j += 1
        # print(ans)
        return s[ans[0]:ans[1]+1]
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

