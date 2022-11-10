
question_content = """
在一个 n * m 的二维数组中，每一行都按照从左到右 非递减 的顺序排序，每一列都按照从上到下 非递减 的顺序排序。请完成一个高效的函数，输入这样的一个二维数
组和一个整数，判断数组中是否含有该整数。 

 

 示例: 
输入: 
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
5 
输出: true

输入: [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
20 
输出: false
 

 限制： 

 0 <= n <= 1000 

 0 <= m <= 1000 

 

 注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/ 

 Related Topics 数组 二分查找 分治 矩阵 👍 821 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        递归二分查找
        由于矩阵从左到右, 从上到下是非递减的, 所以可以根据这个把 大于 target 和 小于 target 的矩阵条排除
        对当前矩阵:
            1. 搜索最顶行 r0 第一个大于 target 的位置, 将它以及之后的排除, 该位置以及之后的列都必然大于 target
            2. 搜索最低行 r1 第一个大于等于 target 的位置, 将它之前的位置排除, 该位置之前的列都必然小于 target
            3. 列的搜索同理;
            4. 搜索过程中如果四个端点有某个等于 target , return True; 若矩阵为空, 则 return False
        """
        from bisect import bisect_left, bisect_right
        def bisect_left(arr, tar, key=lambda x: x):
            """ get first i that key(arr[i]) >= tar """
            left, right = 0, len(arr)
            while right > left:
                mid = left + right >> 1
                if key(arr[mid]) < tar:
                    left = mid + 1
                else:
                    right = mid
            return right
        def bisect_right(arr, tar, key=lambda x: x):
            """ get first i that key(arr[i]) > tar """
            left, right = 0, len(arr)
            while right > left:
                mid = left + right >> 1
                if key(arr[mid]) <= tar:
                    left = mid + 1
                else:
                    right = mid
            return right

        if not matrix or not matrix[0]:
            return False

        tar = target

        def get(r0, c0, r1, c1):
            nonlocal tar

            if r1 - r0 <= 0 or c1 - c0 <= 0:
                return False
            elif matrix[r0][c0] == tar or matrix[r1 - 1][c1 - 1] == tar or matrix[r1 - 1][c0] == tar or \
                    matrix[r0][c1 - 1] == tar:
                return True

            c1_ = bisect_right(range(c0, c1), tar, key=lambda x: matrix[r0][x]) + c0
            c0_ = bisect_left(range(c0, c1), tar, key=lambda x: matrix[r1 - 1][x]) + c0

            r1_ = bisect_right(range(r0, r1), tar, key=lambda x: matrix[x][c0]) + r0
            r0_ = bisect_left(range(r0, r1), tar, key=lambda x: matrix[x][c1 - 1]) + r0

            # print(r0, c0, r1, c1)
            return (r0_, c0_, r1_, c1_)

        m, n = len(matrix), len(matrix[0])
        # 迭代一步步缩小矩阵的范围
        args = (0, 0, m, n)
        res = get(*args)
        while isinstance(res, tuple):
            res = get(*res)
        return res

class Solution1:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        类似二叉搜索数查找, 把起点定在矩阵右上角, 向左是减小, 向下是增大

        """
        if not matrix or not matrix[0]:
            return False

        tar = target
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            # 若当前值等于, 返回 True
            if matrix[i][j] == tar:
                return True
            elif matrix[i][j] > tar:
                # 若大于, 向左移动减小值再继续搜索
                j -= 1
            else:
                # 若小于, 向下移动增大值再继续搜索
                i += 1

        return False

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
