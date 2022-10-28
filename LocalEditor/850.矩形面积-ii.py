#
# @lc app=leetcode.cn id=850 lang=python3
#
# [850] 矩形面积 II
#
# https://leetcode.cn/problems/rectangle-area-ii/description/
#
# algorithms
# Hard (63.39%)
# Likes:    228
# Dislikes: 0
# Total Accepted:    17.5K
# Total Submissions: 27.6K
# Testcase Example:  '[[0,0,2,2],[1,0,2,3],[1,0,3,1]]'
#

question_content="""我们给出了一个（轴对齐的）二维矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2,
y2]，其中（x1，y1）是矩形 i 左下角的坐标， (xi1, yi1) 是该矩形 左下角 的坐标， (xi2, yi2) 是该矩形 右上角 的坐标。

计算平面中所有 rectangles 所覆盖的 总面积 。任何被两个或多个矩形覆盖的区域应只计算 一次 。

返回 总面积 。因为答案可能太大，返回 10^9 + 7 的 模 。



示例 1：




输入：rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
输出：6
解释：如图所示，三个矩形覆盖了总面积为6的区域。
从(1,1)到(2,2)，绿色矩形和红色矩形重叠。
从(1,0)到(2,3)，三个矩形都重叠。


示例 2：


输入：rectangles = [[0,0,1000000000,1000000000]]
输出：49
解释：答案是 10^18 对 (10^9 + 7) 取模的结果， 即 49 。




提示：


1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= xi1, yi1, xi2, yi2 <= 10^9
矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。


"""

from typing import *
from PythonLeetcodeRunner import *
from bisect import bisect_left

# @lc code=start
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        ybound = []
        xbound = set()
        for i, (x1, y1, x2, y2) in enumerate(rectangles):
            ybound.append((y1, 1, i))
            ybound.append((y2, -1, i))
            xbound.add(x1)
            xbound.add(x2)
        ybound.sort()
        xbound = sorted(list(xbound))
        # rectangles.sort(key=lambda x: )

        # 维护切割线长度
        segLen = [xbound[i+1]-xbound[i] for i in range(len(xbound)-1)]
        line = [0] * (len(xbound)-1)
        lineWidth = 0
        def add_line(x1, x2):
            nonlocal lineWidth
            id1, id2 = bisect_left(xbound, x1), bisect_left(xbound, x2)
            for i in range(id1, id2):
                if line[i] == 0:
                    lineWidth += segLen[i]
                line[i] += 1
        def remove_line(x1, x2):
            nonlocal lineWidth
            id1, id2 = bisect_left(xbound, x1), bisect_left(xbound, x2)
            for i in range(id1, id2):
                if line[i] == 1:
                    lineWidth -= segLen[i]
                line[i] -= 1
        
        # 沿着y轴从下往上动态扫描
        area = 0
        last_bound = ybound[0][0]
        for bound, flag, i in ybound:
            area += (bound-last_bound) * lineWidth
            area = area % (10**9+7)
            last_bound = bound
            if flag == 1:
                add_line(rectangles[i][0], rectangles[i][2])
            else:
                remove_line(rectangles[i][0], rectangles[i][2])
        
        return area

# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

