#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode.cn/problems/divide-two-integers/description/
#
# algorithms
# Medium (22.19%)
# Likes:    1000
# Dislikes: 0
# Total Accepted:    188.2K
# Total Submissions: 848.4K
# Testcase Example:  '10\n3'
#

question_content="""给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
-2



示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2


输入: dividend = 7, divisor = 3
输出: 2
解释: 7/-3 = truncate(-2.33333..) = -2




提示：


被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。


"""

from tkinter import W
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2**31 and divisor == -1:
            return 2**31-1
        elif dividend==-2**31 and divisor == 1:
            return -2**31
        
        # 将
        if dividend < 0:
            return -self.divide(-dividend, divisor)
        elif divisor < 0:
            return -self.divide(dividend, -divisor)

        # 
        ans = 0
        base = 1 << 31
        while base > 0 and dividend != 0:
            if dividend >= divisor * base:
                ans |= base
                dividend -= divisor * base
            base >>= 1

        return ans

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 判断可能溢出的特殊情况
        if dividend==-2**31 and divisor == -1:
            return 2**31-1
        elif dividend==-2**31 and divisor == 1:
            return -2**31
        
        # 映射到正数范围处理
        if dividend < 0:
            return -self.divide(-dividend, divisor)
        elif divisor < 0:
            return -self.divide(dividend, -divisor)

        # 
        ans = 0
        for i in range(31, -1, -1):
            base = 1 << i
            if dividend == 0: break
            
            # 此处说明一下, 负数右移最小值为-1, 
            # 若divisor==-1, dividend <= divisor << i 和 dividend >> i <= divisor 可能不等价
            if dividend >= divisor << i:  # 若使用此条件需要判断是否溢出
            # if dividend >> i + dividend % (1<<(i)) >= divisor:
                ans |= base
                dividend -= divisor << i

        return ans
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

