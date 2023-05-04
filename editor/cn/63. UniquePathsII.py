question_content = """
You are given an m x n integer array grid. There is a robot initially located 
at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-
right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
right at any point in time. 

 An obstacle and space are marked as 1 or 0 respectively in grid. A path that 
the robot takes cannot include any square that is an obstacle. 

 Return the number of possible unique paths that the robot can take to reach 
the bottom-right corner. 

 The testcases are generated so that the answer will be less than or equal to 2 
* 10⁹. 

 
 Example 1: 
 
 
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
 

 Example 2: 
 
 
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

 
 Constraints: 

 
 m == obstacleGrid.length 
 n == obstacleGrid[i].length 
 1 <= m, n <= 100 
 obstacleGrid[i][j] is 0 or 1. 
 

 Related Topics 数组 动态规划 矩阵 👍 1039 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        if grid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for j in range(1, n):
            if grid[0][j] == 1:
                continue
            dp[0][j] = dp[0][j-1]
        for i in range(1, m):
            if grid[i][0] == 1:
                continue
            dp[i][0] = dp[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
