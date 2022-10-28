#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.cn/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (73.27%)
# Likes:    1265
# Dislikes: 0
# Total Accepted:    232.7K
# Total Submissions: 317.6K
# Testcase Example:  '"aab"'
#

question_content="""Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.


Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]


Constraints:


1 <= s.length <= 16
s contains only lowercase English letters.


"""

from functools import cache
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        @cache
        def isPalindrome(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        
        # @cache
        # def isPalindrome(i: int, j: int) -> int:
        #     if i >= j:
        #         return 1
        #     return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        
        result = []
        path = []
        def backtracking(s, startIndex):
            if len(s) == startIndex:
                result.append(path[:])
                return
            
            for i in range(startIndex, len(s)):
                # if not isPalindrome(startIndex, i):
                if not isPalindrome(s[startIndex:i+1]):
                    continue
                path.append(s[startIndex:i+1])
                backtracking(s, i+1)
                path.pop()

        backtracking(s, 0)
        isPalindrome.cache_clear()
        return result
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

