question_content = """
给你一个字符串 s，找到 s 中最长的回文子串。 

 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。 

 

 示例 1： 

 
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
 

 示例 2： 

 
输入：s = "cbbd"
输出："bb"
 

 

 提示： 

 
 1 <= s.length <= 1000 
 s 仅由数字和英文字母组成 
 

 Related Topics 字符串 动态规划 👍 6428 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ 枚举所有中心点, 从中间往左右扩展回文字符串 """
        def max_equal(l, r):
            ans = 0
            for i in range(len(s)):
                if l - i < 0 or r + i >= len(s):
                    break
                if s[l - i] != s[r + i]:
                    break
                ans = i + 1
            return [l - ans + 1, r + ans]

        ans = [-1, -1]
        for i in range(len(s)):
            v1 = max_equal(i, i)
            v2 = max_equal(i, i + 1)
            ans = max([ans, v1, v2], key=lambda x: x[1] - x[0])

        return s[ans[0]:ans[1]]


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
