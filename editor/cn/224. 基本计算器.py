question_content = """
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。 

 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。 

 

测试用例: s = "1-(     -2)" 
期望结果: 
3

 示例 1： 

 
输入：s = "-1 + 2"
输出：1
 

 示例 2： 

 
输入：s = " 2-1 + 2 "
输出：3
 

 示例 3： 

 
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
 

 

 提示： 

 
 1 <= s.length <= 3 * 10⁵ 
 s 由数字、'+'、'-'、'('、')'、和 ' ' 组成 
 s 表示一个有效的表达式 
 '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效) 
 '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的) 
 输入中不存在两个连续的操作符 
 每个数字和运行的计算将适合于一个有符号的 32位 整数 
 

 Related Topics 栈 递归 数学 字符串 👍 852 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        def cale(n1, n2, op):
            # s = f'{str(n1)} {op} {str(n2)}'
            f = {
                '+': lambda x: x[0] + x[1],
                '-': lambda x: x[0] - x[1],
                '*': lambda x: x[0] * x[1],
                '/': lambda x: x[0] / x[1],
            }
            return f[op]([n1, n2])

        # '#' 加在最后充当运算优先级最低的截止符号
        rank = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 5, ')': 0, '#': -10}
        ops = []
        nums = [0]

        # 为了方便, 添加一个优先级很低的结束符, 来把最后栈清空
        # s = " 2 + 24*2#"
        # s += '#'
        # s = s.replace(' ', '')
        # s = s.replace('(-', '(0-')

        import re
        # 正则替换, 把 '(  -' 替换成 '(0-'
        s = re.sub(pattern=r'(?<=\() *(?=\-)', repl='0', string=s) + '#'

        # 替换
        num = None
        for i, c in enumerate(s):
            if c.isdigit():
                # 这部分读入数字
                if num is None:
                    num = int(c)
                else:
                    num = num * 10 + int(c)
            else:
                # 如果不是数字, 保存读入数字结果
                if num is not None:
                    nums.append(num)
                    num = None

                # 当操作符栈顶优先级 <= 当前运算符, 求值
                if c == ' ':
                    continue
                else:
                    # 此处碰到下一个运算符

                    # 如果 '-' 前面是一个左括号, nums 中添加一个 0
                    # if c == '-' and (i == 0 or s[i - 1] in {'(', ' '}):
                    #     nums.append(0)

                    # 若栈顶优先级小于等于当前运算符, 计算前面的表达式
                    while ops and rank[ops[-1]] >= rank[c] and ops[-1] != '(':
                        op = ops.pop()
                        n2 = nums.pop()
                        n1 = nums.pop()
                        res = cale(n1, n2, op)
                        nums.append(res)
                    # ops.append(c)

                    # 如果当前运算符为 ')', 且上一个运算符为 ')' (按照设计当前为')'退出时一定是左括号栈顶)
                    if ops and ops[-1] == '(' and c == ')':
                        ops.pop()
                    else:
                        # 如果当前不是右括号, 添加该运算符
                        ops.append(c)
        return nums[-1]


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
