
question_content = """
Given two non-negative integers num1 and num2 represented as strings, return 
the product of num1 and num2, also represented as a string. 

 Note: You must not use any built-in BigInteger library or convert the inputs 
to integer directly. 

 
 Example 1: 
Input: num1 = "2", num2 = "3"
Output: "6"
 
 Example 2: 
Input: num1 = "123", num2 = "456"
Output: "56088"
 
 
 Constraints: 

 
 1 <= num1.length, num2.length <= 200 
 num1 and num2 consist of digits only. 
 Both num1 and num2 do not contain any leading zero, except the number 0 itself.
 
 

 Related Topics 数学 字符串 模拟 👍 1085 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """ 求出对应权值的和, 再从低位往高位遍历进位 """
        if len(num1) < len(num2):
            return self.multiply(num2, num1)

        if num2 == '0':
            return '0'

        # 求出带权的乘积数组结果, 位置 i 处的权值为 10**i
        n1, n2 = len(num1), len(num2)
        s = [0] * (n1 + n2 - 1)
        for i in range(n1):
            for j in range(n2):
                s[len(s) - 1 - (i + j)] += int(num1[i]) * int(num2[j])

        # 把带权数组里面的值往高位进位
        ans = []
        carry = 0
        for i in range(len(s)):
            carry, digit = (s[i] + carry) // 10, (s[i] + carry) % 10
            # 添加上对于位数的数字
            ans.append(str(digit))
        # 若仍有进位, 添加该数到末尾
        if carry:
            ans.append(str(carry))

        return ''.join(ans[::-1])


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
