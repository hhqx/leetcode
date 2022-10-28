
question_content = """
Given a positive integer n, generate an n x n matrix filled with elements from 1
 to n² in spiral order. 

 
 Example 1: 
 
 
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
 

 Example 2: 

 
Input: n = 1
Output: [[1]]
 

 
 Constraints: 

 
 1 <= n <= 20 
 

 Related Topics 数组 矩阵 模拟 👍 803 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[[0] for i in range(n)] for i in range(n)]

        cnt = 1
        for i in range(n//2):
            start = [i, i]
            end = [i, n - 2 - i]
            x = start[0]
            for y in range(start[1], end[1] + 1, 1):
                M[x][y] = cnt
                cnt += 1

            start = [i, n - 1 - i]
            end = [n - 2 - i, n - 1 - i]
            y = start[1]
            for x in range(start[0], end[0] + 1, 1):
                M[x][y] = cnt
                cnt += 1

            start = [n - 1 - i, n - 1 - i]
            end = [n - 1 - i, i + 1]
            x = start[0]
            for y in range(start[1], end[1] - 1, -1):
                M[x][y] = cnt
                cnt += 1

            start = [n - 1 - i, i]
            end = [i + 1, i]
            y = start[1]
            for x in range(start[0], end[0] - 1, -1):
                M[x][y] = cnt
                cnt += 1

        if n % 2 == 1:
            M[n//2][n//2] = cnt
            cnt += 1
        print(M)
        return M

    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0  # 起始点
        loop, mid = n // 2, n // 2  # 迭代次数、n为奇数时，矩阵的中心点
        count = 1  # 计数

        for offset in range(1, loop + 1):  # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset):  # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):  # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1  # 更新起始点
            starty += 1

        if n % 2 != 0:  # n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
