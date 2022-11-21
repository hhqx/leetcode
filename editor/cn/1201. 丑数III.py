
question_content = """
给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。 

 丑数是可以被 a 或 b 或 c 整除的 正整数 。 

 

 示例 1： 

 
输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。 

 示例 2： 

 
输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
 

 示例 3： 

 
输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
 

 示例 4： 

 
输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984
 

 

 提示： 

 
 1 <= n, a, b, c <= 10^9 
 1 <= a * b * c <= 10^18 
 本题结果在 [1, 2 * 10^9] 的范围内 
 

 Related Topics 数学 二分查找 数论 👍 120 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """ 容斥原理, 二分法查找丑数 """
        def lcm(*a):
            """ get LCM of array a. """
            _lcm = a[0]
            for v in a[1:]:
                _lcm = _lcm * v // gcd(_lcm, v)
            return _lcm

        # 集合容斥原理, f(x) 的结果为[1,x]有多少个能整除a,b,c的数
        abc, ab, ac, bc = lcm(a, b, c), lcm(a, b), lcm(a, c), lcm(b, c)
        f = lambda x: x // a + x // b + x // c + x // abc - x // ab - x // ac - x // bc

        # 二分查找第一个 xn , s.t. f(xn) = n
        xn = bisect.bisect_left(range(1, min(int(2e9), a * b * c * n)), n, key=f) + 1

        return xn
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
