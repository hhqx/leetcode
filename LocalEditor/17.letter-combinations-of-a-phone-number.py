#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (57.80%)
# Likes:    2094
# Dislikes: 0
# Total Accepted:    565.3K
# Total Submissions: 978K
#

question_content="""Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent. Return the answer in any
order.

A mapping of digits to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.


Example 1:


Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Example 2:


Input: digits = ""
Output: []


Example 3:


Input: digits = "2"
Output: ["a","b","c"]



Constraints:


0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


"""

from typing import *
from unittest import result
from RunLeetCodeInPycharm import StartTest

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        table = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        res = []
        path = ""
        def backtrack(n, k, StartIndex):
            nonlocal path
            if len(path) == k:
                res.append(path[:])
                return
            chars = table[int(digits[StartIndex])]
            for c in chars:
                path += c
                backtrack(n, k, StartIndex+1)
                path = path[:-1]
        
        k = len(digits)
        backtrack(8, k, 0)
        return res
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()




