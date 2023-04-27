question_content = """
3. 最强祝福力场
通过的用户数188
尝试过的用户数347
用户总通过次数188
用户总提交次数558
题目难度Medium
小扣在探索丛林的过程中，无意间发现了传说中“落寞的黄金之都”。而在这片建筑废墟的地带中，小扣使用探测仪监测到了存在某种带有「祝福」效果的力场。
经过不断的勘测记录，小扣将所有力场的分布都记录了下来。forceField[i] = [x,y,side] 表示第 i 片力场将覆盖以坐标 (x,y) 为中心，边长为 side 的正方形区域。

若任意一点的 力场强度 等于覆盖该点的力场数量，请求出在这片地带中 力场强度 最强处的 力场强度。

注意：

力场范围的边缘同样被力场覆盖。
示例 1：

输入：
forceField = [[0,0,1],[1,0,1]]

输出：2

解释：如图所示，（0.5, 0) 处力场强度最强为 2， （0.5，-0.5）处力场强度同样是 2。
image.png

示例 2：

输入：
forceField = [[4,4,6],[7,5,3],[1,6,2],[5,6,3]]

输出：3

解释：如下图所示，
forceField[0]、forceField[1]、forceField[3] 重叠的区域力场强度最大，返回 3
image.png

提示：

1 <= forceField.length <= 100
forceField[i].length == 3
0 <= forceField[i][0], forceField[i][1] <= 10^9
1 <= forceField[i][2] <= 10^9

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        """ 离散形式的二维差分数组 """
        diff = []
        xcoord, ycoord = set([-inf]), set([-inf])
        for x, y, side in forceField:
            x, y, side = 2 * x, 2 * y, 2 * side
            x1, x2, y1, y2 = x - side // 2, x + side // 2 + 1, y - side // 2, y + side // 2 + 1,
            tmp = [[x1, y1, 1], [x1, y2, -1], [x2, y1, -1], [x2, y2, 1], ]
            diff.extend(tmp)
            xcoord = xcoord.union([x1, x2])
            ycoord = ycoord.union([y1, y2])

        xcoord = list(sorted(xcoord))
        ycoord = list(sorted(ycoord))
        # print(xcoord, ycoord)

        # 给差分二维数组赋初始值
        ans = -inf
        d = defaultdict(int)
        for x, y, val in diff:
            d[(x, y)] += val

        # 对二维数组进行累加积分
        for i in range(1, len(xcoord)):
            for j in range(1, len(ycoord)):
                x1, x2, y1, y2 = xcoord[i - 1], xcoord[i], ycoord[j - 1], ycoord[j],
                d[(x2, y2)] += d[(x1, y2)] + d[(x2, y1)] - d[(x1, y1)]
                ans = max(ans, d[(x2, y2)])

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
