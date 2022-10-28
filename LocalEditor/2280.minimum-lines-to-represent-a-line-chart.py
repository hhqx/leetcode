#
# @lc app=leetcode.cn id=2280 lang=python3
#
# [2280] Minimum Lines to Represent a Line Chart
#
# https://leetcode.cn/problems/minimum-lines-to-represent-a-line-chart/description/
#
# algorithms
# Medium (21.42%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 39.5K
# Testcase Example:  '[[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]'
#

question_content="""You are given a 2D integer array stockPrices where stockPrices[i] = [dayi,
pricei] indicates the price of the stock on day dayi is pricei. A line chart
is created from the array by plotting the points on an XY plane with the
X-axis representing the day and the Y-axis representing the price and
connecting adjacent points. One such example is shown below:

Return the minimum number of lines needed to represent the line chart.


Example 1:


Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
Output: 3
Explanation:
The diagram above represents the input, with the X-axis representing the day
and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5),
and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2),
and (8,1).
It can be shown that it is not possible to represent the line chart using
less than 3 lines.


Example 2:


Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
Output: 1
Explanation:
As shown in the diagram above, the line chart can be represented with a
single line.



Constraints:


1 <= stockPrices.length <= 10^5
stockPrices[i].length == 2
1 <= dayi, pricei <= 10^9
All dayi are distinct.


"""

from typing import *
from PythonLeetcodeRunner import *

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        def is_line(p1, p2, p3):
            """ 判断三点是否共线 """
            # 计算两个向量叉乘是否为零
            # (p3[0]-p1[0], p3[1]-p1[1])
            # (p2[0]-p1[0], p2[1]-p1[1])
            diff = (p3[0]-p1[0])*(p2[1]-p1[1]) - (p3[1]-p1[1])*(p2[0]-p1[0])
            print((p3[1]-p3[1])*(p2[0]-p1[0]))
            return abs(diff) < 1e-5
        
        if len(stockPrices) < 1:
            return 0
        # 核心思想为: 如果有连续两段的在同一直线上, 则需要的线段数减1
        total_num = len(stockPrices) - 1
        for i in range(2, len(stockPrices)):
            if is_line(stockPrices[i-2], stockPrices[i-1], stockPrices[i]):
                total_num -= 1
        
        return total_num
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

