question_content = """
There is a robot on an m x n grid. The robot is initially located at the top-
left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner 
(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any 
point in time. 

 Given the two integers m and n, return the number of possible unique paths 
that the robot can take to reach the bottom-right corner. 

 The test cases are generated so that the answer will be less than or equal to 2
 * 10⁹. 

 
 Example 1: 
 
 
Input: m = 3, n = 7
Output: 28
 

 Example 2: 

 
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the 
bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

 
 Constraints: 

 
 1 <= m, n <= 100 
 

 Related Topics 数学 动态规划 组合数学 👍 1758 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """ 时间复杂度: o(mn),  空间复杂度: o(mn), 可以优化至o(m+n) """
        dp = [[0] * n for _ in range(m)]
        dp[0] = [1] * n
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])

        return dp[-1][-1]


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        """ 时间复杂度: o(mn),  空间复杂度: o(mn), 可以优化至o(m+n) """

        return comb(m + n-2, m-1)


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
