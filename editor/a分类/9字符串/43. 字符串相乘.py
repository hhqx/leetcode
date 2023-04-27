question_content = """
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 

 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。 

 

 示例 1: 

 
输入: num1 = "2", num2 = "3"
输出: "6" 

 示例 2: 

 
输入: num1 = "123", num2 = "456"
输出: "56088" 

 

 提示： 

 
 1 <= num1.length, num2.length <= 200 
 num1 和 num2 只能由数字组成。 
 num1 和 num2 都不包含任何前导零，除了数字0本身。 
 

 Related Topics 数学 字符串 模拟 👍 1195 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """ 时间复杂度: o(log(n1) + log(n2)) """
        n1, n2 = len(num1), len(num2)
        if n1 < n2:
            return self.multiply(num2, num1)
        if num2 == '0':
            return '0'
        out = [0] * (n1 + n2 - 1)
        for i, c1 in enumerate(num1):
            for j, c2 in enumerate(num2):
                out[i + j] += int(c1) * int(c2)

        carry = 0
        for i in range(len(out) - 1, -1, -1):
            carry, digit = divmod(carry + out[i], 10)
            out[i] = digit
        if carry:
            out = [carry] + out
        ans = "".join(map(str, out))

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
