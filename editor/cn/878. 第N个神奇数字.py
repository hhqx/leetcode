
question_content = """
一个正整数如果能被 a 或 b 整除，那么它是神奇的。 

 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 10⁹ + 7 取模 后的值。 

 

 
 

 示例 1： 

 
输入：n = 1, a = 2, b = 3
输出：2
 

 示例 2： 

 
输入：n = 4, a = 2, b = 3
输出：6
 

 

 提示： 

 
 1 <= n <= 10⁹ 
 2 <= a, b <= 4 * 10⁴ 
 

 

 Related Topics 数学 二分查找 👍 113 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def lcm(*a):
            """ get LCM of array a. """
            _lcm = a[0]
            for v in a[1:]:
                _lcm = _lcm * v // gcd(_lcm, v)
            return _lcm

        # 集合容斥原理, f(x) 的结果为[1,x]有多少个能整除a,b的数
        ab = lcm(a, b)
        f = lambda x: x // a + x // b - x // ab
        mod = int(1e9 + 7)

        # 二分查找第一个 xn , s.t. f(xn) = n
        xn = bisect.bisect_left(range(1, min(a, b) * n + 1), n, key=f) + 1

        return xn % mod


# runtime:40 ms
# memory:14.9 MB

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
