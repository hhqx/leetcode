
question_content = """
A boolean expression is an expression that evaluates to either true or false. 
It can be in one of the following shapes: 

 
 't' that evaluates to true. 
 'f' that evaluates to false. 
 '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
 
 '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of 
the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1. 
 '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the 
inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1. 
 

 Given a string expression that represents a boolean expression, return the 
evaluation of that expression. 

 It is guaranteed that the given expression is valid and follows the given 
rules. 

Input: expression = "&(|(f))"
Output: false
 
 Example 1: 

Input: 
expression = "!(&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))))"
Output: true

Input: expression = "!(&(!(t),&(f),|(f)))"
Output: true

Input: expression = "!(&(f,t))"
Output: true

 

Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
 

 Example 2: 

 
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
 

 Example 3: 

 
Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is 
now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 

 
 Constraints: 

 
 1 <= expression.length <= 2 * 10⁴ 
 expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', 
and ','. 
 

 Related Topics 栈 递归 字符串 👍 170 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """ 双栈法一次遍历, o(n) """
        s = expression
        ops = []
        nums = []

        def calc(op, args):
            s = sum(args)
            if op == '|':
                return s != 0
            elif op == '&':
                return s == len(args)
            elif op == '!':
                return not s

        for i, c in enumerate(s):
            if c == ',':
                continue
            elif c in {'|', '&', '!'}:
                ops.append(c)
            elif c == '(':
                nums.append('#')
            elif c in ['t', 'f']:
                nums.append(c == 't')
            elif c == ')':
                # get all the num after last '#'
                args = []
                n = nums.pop()
                while n != '#':
                    args.append(n)
                    n = nums.pop()

                # pop the operator, calculate the function result,
                # append the res to stack: nums.
                op = ops.pop()
                res = calc(op, args)
                nums.append(res)

            else:
                # invalid
                pass

        return nums[0]

class Solution1:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        dfs 递归法, 由于重复往复遍历, 效率最坏 o(n*n)

        递归的思路核心是把括号内的子函数文本提取出来递归求解, 但是要界定子函数在哪里终止又需要统计递归深度,
        只有当前')'深度等于起始'('的深度时才是一个完整的子函数字符串,
        这个过程中必然会跳过深度更大的子函数, 但未及时求解, 之后又返回来求解, 有一种脱裤子放pee的感觉..
        """
        s = expression
        def calc(op, args):
            if not len(args):
                print('error')
            s = sum(args)
            if op == '|':
                return s != 0
            elif op == '&':
                return s == len(args)
            elif op == '!':
                return not s

        def dfs(i, j):
            # tmp = s[i:j]
            args = []
            op = s[i]
            start = None
            depth = 0
            for cur in range(i+1, j):
                if s[cur] in {'|', '&', '!'}:
                    if depth == 0:
                        start = cur
                    depth += 1
                elif s[cur] == ')':
                    depth -= 1
                    if depth == 0:
                        res = dfs(start, cur)
                        args.append(res)
                elif s[cur] in {'t', 'f'} and depth == 0:
                    args.append(s[cur] == 't')

            return calc(op, args)

        return dfs(0, len(s)-1)
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
