
question_content = """
有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。 

 

 给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 10⁹ + 7 取模 的值。 

 平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。 

 

 示例 1: 

 

 
输入: n = 3
输出: 5
解释: 五种不同的方法如上所示。
 

 示例 2: 

 
输入: n = 1
输出: 1
 

 

 提示： 

 
 1 <= n <= 1000 
 

 Related Topics 动态规划 👍 258 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTilings(self, n: int) -> int:
        """ 带状态的 dp . """
        if n <= 2:
            return n

        MOD = int(1e9 + 7)

        # dp[][i] 表示铺到第i列时最后一列铺了多少个
        # dp[0]表示最后一列一个没铺, dp[1]表示铺了上面一个, dp[2]表示铺了下面一个, dp[3]表示铺满了
        dp = [[0] * (n + 1) for _ in range(4)]

        dp[0][0] = 1
        dp[3][0] = 1

        for i in range(1, n):
            dp[0][i] = (dp[3][i-1]) % MOD

            dp[1][i] = (dp[0][i-1] + dp[2][i-1]) % MOD

            dp[2][i] = (dp[0][i-1] + dp[1][i-1]) % MOD

            dp[3][i] = (dp[3][i-1] + dp[0][i-1] + dp[1][i-1] + dp[2][i-1]) % MOD

        return dp[3][n-1]

class Solution:
    def numTilings(self, n: int) -> int:
        """ dp + 矩阵快速幂"""
        if n <= 2:
            return n

        MOD = int(1e9 + 7)

        # dp[][i] 表示铺到第i列时最后一列铺了多少个
        # dp[0]表示最后一列一个没铺, dp[1]表示铺了上面一个, dp[2]表示铺了下面一个, dp[3]表示铺满了
        # dp = [[0] * (n + 1) for _ in range(4)]

        #         dp[0][0] = 1
        #         dp[3][0] = 1

        #         for i in range(1, n):
        #             dp[0][i] = dp[3][i-1]

        #             dp[1][i] = dp[0][i-1] + dp[2][i-1]

        #             dp[2][i] = dp[0][i-1] + dp[1][i-1]

        #             dp[3][i] = dp[3][i-1] + dp[0][i-1] + dp[1][i-1] + dp[2][i-1]

        def matrix_multiply(M, N):
            """ return P = M @ N """
            m, k, n = len(M), len(M[0]), len(N[0])
            P = []
            for i in range(m):
                Pi = []
                for j in range(n):
                    Pij = sum(M[i][kk] * N[kk][j] for kk in range(k)) % MOD
                    Pi.append(Pij)
                P.append(Pi)
            return P

        def matrix_pow(M, n):
            ans = [[1 if i == j else 0 for j in range(len(M[0]))] for i in range(len(M))]
            while n:
                if n & 1:
                    ans = matrix_multiply(ans, M)
                n >>= 1
                M = matrix_multiply(M, M)
            return ans

        # 用矩阵快速幂直接计算动态规划的一阶迭代递推
        M = [[0, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1], ]
        ans = [[1], [0], [0], [1]]
        M_n = matrix_pow(M, n - 1)
        ans = matrix_multiply(M_n, ans)

        return ans[3][0] % MOD
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
