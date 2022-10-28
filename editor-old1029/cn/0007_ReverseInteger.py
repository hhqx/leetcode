
question_content = """
Given a signed 32-bit integer x, return x with its digits reversed. If 
reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1
], then return 0. 

 Assume the environment does not allow you to store 64-bit integers (signed or 
unsigned). 

 
 Example 1: 

 
Input: x = -9463847412
Output: 0
 
Input: x = -8463847412
Output: -2147483648

Input: x = 8463847412
Output: 0
 
Input: x = 7463847412
Output: 2147483647
 
 
Input: x = 123
Output: 321
 

 Example 2: 

 
Input: x = -123
Output: -321
 

 Example 3: 

 
Input: x = 120
Output: 21
 

 
 Constraints: 

 
 -2³¹ <= x <= 2³¹ - 1 
 

 Related Topics 数学 👍 3633 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        # 映射到负数区间进行处理
        if x == 0:
            return 0
        elif x > 0:
            n = self.reverse(-x)
            if n == -2 ** 31:
                return 0
            else:
                return -n

        y = 0
        while x < 0:
            # 计算负数的每个数字
            digit = x % 10
            if digit == 0:
                x = x // 10
            else:
                digit = 10 - digit
                x = x // 10 + 1

            # 预先判断是否超出有符号数的范围
            # y*10 - digit < -2**31  => (digit - 2**31) / 10 > y  => (digit - 2**31) // 10 + (digit - 2**31) % 10 / 10 > y
            # => (digit - 2**31) % 10 == 0时: (digit - 2**31) // 10 > y
            #    (digit - 2**31) % 10 != 0时: (digit - 2**31) // 10 >= y
            m, remain = (digit - 2**31) // 10, (digit - 2**31) % 10
            if remain == 0 and m > y or remain != 0 and m >= y:
                return 0
            else:
                y = y * 10 - digit
                # print(digit)

        return y
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

