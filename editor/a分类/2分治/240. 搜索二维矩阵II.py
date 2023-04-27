question_content = """
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性： 

 
 每行的元素从左到右升序排列。 
 每列的元素从上到下升序排列。 
 

 

 示例 1： 
 
 
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
 

 示例 2： 
 
 
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
 

 

 提示： 

 
 m == matrix.length 
 n == matrix[i].length 
 1 <= n, m <= 300 
 -10⁹ <= matrix[i][j] <= 10⁹ 
 每行的所有元素从左到右升序排列 
 每列的所有元素从上到下升序排列 
 -10⁹ <= target <= 10⁹ 
 

 Related Topics 数组 二分查找 分治 矩阵 👍 1257 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ 类似二叉搜索树递归 """
        m, n = len(matrix), len(matrix[0])
        ans = False

        def dfs(i, j):
            nonlocal ans
            if i >= m or j < 0:
                return
            if matrix[i][j] == target:
                ans = True
                return
            if matrix[i][j] > target:
                return dfs(i, j - 1)
            else:
                return dfs(i + 1, j)

        dfs(0, n - 1)
        return ans

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ 类似二叉搜索树迭代 """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
