question_content = """
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 

 

 示例 1： 
 
 
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],[
"1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
 

 示例 2： 

 
输入：matrix = []
输出：0
 

 示例 3： 

 
输入：matrix = [["0"]]
输出：0
 

 示例 4： 

 
输入：matrix = [["1"]]
输出：1
 

 示例 5： 

 
输入：matrix = [["0","0"]]
输出：0
 

 

 提示： 

 
 rows == matrix.length 
 cols == matrix[0].length 
 1 <= row, cols <= 200 
 matrix[i][j] 为 '0' 或 '1' 
 

 Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 1513 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = 1 + (dp[i-1][j] if i >= 1 else 0)

        # 找出dp[i]中的最大矩形
        for row in dp:
            R = [n] * n
            L = [-1] * n
            st = []
            for i, num in enumerate(row):
                while st and num < row[st[-1]]:
                    idx = st.pop()
                    R[idx] = i
                L[i] = st[-1] if st else -1
                st.append(i)
            for i in range(n):
                val = (R[i] - L[i] - 1) * row[i]
                ans = max(ans, val)

        return ans

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
