#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.cn/problems/zigzag-conversion/description/
#
# algorithms
# Medium (52.01%)
# Likes:    1820
# Dislikes: 0
# Total Accepted:    486.7K
# Total Submissions: 935.6K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#

question_content="""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)


P   A   H   N
A P L S I I G
Y   I   R


And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a
number of rows:


string convert(string s, int numRows);



Example 1:


Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


Example 2:


Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I


Example 3:


Input: s = "A", numRows = 1
Output: "A"



Constraints:


1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def getRowFromZ(s, i, numRows=4):
            ans = ''
            if i < len(s):
                ans += s[i]
            if i != numRows-1 and (2*numRows-3) - (i-1)  < len(s):
                ans += s[(2*numRows-3) - (i-1)]
            return ans
        
        for i in range(4):
            print(getRowFromZ("123456", i, ))
        return

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """ o(n) 按照行号和列周期分为两重for循环 """
        if numRows == 1:
            return s
        
        ans = ""
        for i in range(numRows):
            # 列周期, 每个周期有(2*numRows-2)个字母
            for k in range((len(s) // (2*numRows-2)) + 1):
                # 添加竖线字母
                j = i + k*(2*numRows-2)
                if j < len(s):
                    ans += s[j]

                # 添加斜线字母
                if i != 0 and  i != numRows-1:
                    j = (2*numRows-3) - (i-1) + k*(2*numRows-2)
                    if j < len(s):
                        ans += s[j]

        return ans
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

