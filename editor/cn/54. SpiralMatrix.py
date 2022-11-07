question_content = """
Given an m x n matrix, return all elements of the matrix in spiral order. 

 
 Example 1: 
 
 
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
 

 Example 2: 
 
 
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

 
 Constraints: 

 
 m == matrix.length 
 n == matrix[i].length 
 1 <= m, n <= 10 
 -100 <= matrix[i][j] <= 100 
 

 Related Topics 数组 矩阵 模拟 👍 1255 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def get_line(start, end):
            """ Get all the points from start to end: [start, end) """
            # if end[1] != start[1] and end[0] != start[0] and (end[1]-start[1] != end[0]-start[0]):
            if end[1] != start[1] and end[0] != start[0]:
                # Used for debug, [start end) line must be vertical or horizaltol
                return None

            ans = []
            # delta[i] equals to -1, 1 or 0
            delta = tuple((e - s) // abs(e - s) if e != s else 0 for e, s in zip(end, start))

            # while current cursor not reach end, append it
            cur = start
            # print(start)
            while cur != end:
                # append cursor
                ans.append(matrix[cur[0]][cur[1]])
                # update current cursor
                cur = tuple(map(operator.add, cur, delta))

            return ans

        m, n = len(matrix), len(matrix[0])
        ans = []

        for k in range(100):
            # w, h 最最外圈四个矩形条的长高
            w, h = m - 1 - 2 * k, n - 1 - 2 * k
            if w <= 0 or h <= 0:
                # 若 m, n 有奇数边(w==0 或 h==0), 需单独加上剩下的长条
                if w == 0 and h >= 0:
                    ans.extend(get_line((k, k), (k, k + h + 1)))
                elif w >= 0 and h == 0:
                    ans.extend(get_line((k, k), (k + w + 1, k)))
                break

            # rectangular vertex
            vertex = ((k, k), (k, k + h), (k + w, k + h), (k + w, k))

            # tranverse the rectangular edges
            for i in range(len(vertex)):
                start, end = vertex[i], vertex[(i + 1) % len(vertex)]
                points = get_line(start, end)

                # extend to ans
                ans.extend(points)

        return ans


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ 打标记模拟法 """
        m, n = len(matrix), len(matrix[0])
        ans = []

        top, bottom, left, right = 0, m - 1, 0, n - 1
        DIR = ((0, 1), (1, 0), (-1, 0), (0, -1))
        dir = 0
        INF = float('inf')
        x, y = 0, 0

        for i in range(m * n):
            # append track
            ans.append(matrix[x][y])
            # add mark
            matrix[x][y] = INF
            if i >= m * n - 1:
                break
            # search for a valid direction
            nx, ny = x + DIR[dir][0], y + DIR[dir][1]
            while not ((0 <= nx <= m - 1) and (0 <= ny <= n - 1) and matrix[nx][ny] != INF):
                dir = (dir + 1) % len(DIR)
                nx, ny = x + DIR[dir][0], y + DIR[dir][1]
                # print(dir, x + DIR[dir][0], y + DIR[dir][1])

            # move to next step
            x, y = nx, ny

        return ans


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ 一层一层模拟法, 官解二 """
        m, n = len(matrix), len(matrix[0])
        ans = []

        top, bottom, left, right = 0, m - 1, 0, n - 1
        row, col = 0, 0
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                ans.append(matrix[row][col])
            for row in range(top + 1, bottom + 1):
                ans.append(matrix[row][col])
            if top < bottom and left < right:
                for col in range(right - 1, left - 1, -1):
                    ans.append(matrix[row][col])
                for row in range(bottom - 1, top, -1):
                    ans.append(matrix[row][col])

            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
