from collections import defaultdict

question_content = """
Implement the myAtoi(string s) function, which converts a string to a 32-bit 
signed integer (similar to C/C++'s atoi function). 

 The algorithm for myAtoi(string s) is as follows: 

 
 Read in and ignore any leading whitespace. 
 Check if the next character (if not already at the end of the string) is '-' 
or '+'. Read this character in if it is either. This determines if the final 
result is negative or positive respectively. Assume the result is positive if 
neither is present. 
 Read in next the characters until the next non-digit character or the end of 
the input is reached. The rest of the string is ignored. 
 Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no 
digits were read, then the integer is 0. Change the sign as necessary (from step 
2). 
 If the integer is out of the 32-bit signed integer range [-2³¹, 2³¹ - 1], then 
clamp the integer so that it remains in the range. Specifically, integers less 
than -2³¹ should be clamped to -2³¹, and integers greater than 2³¹ - 1 should be 
clamped to 2³¹ - 1. 
 Return the integer as the final result. 
 

 Note: 

 
 Only the space character ' ' is considered a whitespace character. 
 Do not ignore any characters other than the leading whitespace or the rest of 
the string after the digits. 
 

 
 Example 1: 

 
Input: s = "42.42.42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the 
current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-2³¹, 2³¹ - 1], the final result is 42.
 

 Example 2: 

 
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-2³¹, 2³¹ - 1], the final result is -42.
 

 Example 3: 

 
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading 
whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' 
nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next 
character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-2³¹, 2³¹ - 1], the final result is 4193.
 

 
 Constraints: 

 
 0 <= s.length <= 200 
 s consists of English letters (lower-case and upper-case), digits (0-9), ' ', 
'+', '-', and '.'. 
 

 Related Topics 字符串 👍 1531 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """ 考虑不符合条件的字符串 """
    def myAtoi(self, s: str) -> int:
        val = 0.0

        leadingZeros = True
        dir = 1
        base = 1  # 比例, 小数点前为1, 小数点后为1.0/10
        isIntergePart = True

        # 字符数量限制, 只允许出现数字或有限的正负号,小数点,前导空格
        d = defaultdict(int)
        for k, v in [['-', 1], ['+', 1], ['.', 1], [' ', 2 ** 20]]:
            d[k] = v

        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                d['-'] = 0
                d['+'] = 0
                d[' '] = 0
                if c != '0':
                    leadingZeros = False
                if not leadingZeros:
                    if isIntergePart:
                        val = val * 10 + (ord(c) - ord('0'))
                    else:
                        val = val + (ord(c) - ord('0')) * base
                        base = base / 10
            else:
                d[c] -= 1
                if d[c] < 0:
                    break
                # 非空格之后不允许出现空格
                if c != ' ':
                    d[' '] = 0
                # 出现符号之后不允许出现正负号
                if c in ['-', '+']:
                    d['-'] = 0
                    d['+'] = 0

                if c == '-':
                    dir = -1
                elif c == '.':
                    base = 1.0 / 10
                    isIntergePart = False

        # 限幅
        val = val * dir
        if val > 2 ** 31 - 1:
            val = 2 ** 31 - 1
        elif val < -2 ** 31:
            val = -2 ** 31

        return int(val)

class Solution:
    """ 考虑不符合条件的字符串 """
    def myAtof(self, s: str) -> int:
        val = 0.0

        leadingZeros = True
        dir = 1
        base = 1  # 比例, 小数点前为1, 小数点后为1.0/10
        isIntergePart = True

        # 字符数量限制, 只允许出现数字或有限的正负号,小数点,前导空格
        d = defaultdict(int)
        for k, v in [['-', 1], ['+', 1], ['.', 1], [' ', 2 ** 20]]:
            d[k] = v

        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                d['-'] = 0
                d['+'] = 0
                d[' '] = 0
                if c != '0':
                    leadingZeros = False
                if not leadingZeros:
                    if isIntergePart:
                        val = val * 10 + (ord(c) - ord('0'))
                    else:
                        val = val + (ord(c) - ord('0')) * base
                        base = base / 10
            else:
                d[c] -= 1
                if d[c] < 0:
                    break
                # 非空格之后不允许出现空格
                if c != ' ':
                    d[' '] = 0
                # 出现符号之后不允许出现正负号
                if c in ['-', '+']:
                    d['-'] = 0
                    d['+'] = 0

                if c == '-':
                    dir = -1
                elif c == '.':
                    base = 1.0 / 10
                    isIntergePart = False

        # 限幅
        val = val * dir
        if val > 2 ** 31 - 1:
            val = 2 ** 31 - 1
        elif val < -2 ** 31:
            val = -2 ** 31

        return val


INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution1:
    def myAtoi(self, s: str) -> int:
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans

# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
