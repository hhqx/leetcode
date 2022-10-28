#
# @lc app=leetcode.cn id=935 lang=python3
#
# [935] 骑士拨号器
#
# https://leetcode.cn/problems/knight-dialer/description/
#
# algorithms
# Medium (49.93%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    8.6K
# Total Submissions: 17.2K
# Testcase Example:  '1'
#

question_content="""象棋骑士有一个独特的移动方式，它可以垂直移动两个方格，水平移动一个方格，或者水平移动两个方格，垂直移动一个方格(两者都形成一个 L 的形状)。

象棋骑士可能的移动方式如下图所示:



我们有一个象棋骑士和一个电话垫，如下所示，骑士只能站在一个数字单元格上(即蓝色单元格)。



给定一个整数 n，返回我们可以拨多少个长度为 n 的不同电话号码。

你可以将骑士放置在任何数字单元格上，然后你应该执行 n - 1 次移动来获得长度为 n 的号码。所有的跳跃应该是有效的骑士跳跃。

因为答案可能很大，所以输出答案模 10^9 + 7.






示例 1：


输入：n = 1
输出：10
解释：我们需要拨一个长度为1的数字，所以把骑士放在10个单元格中的任何一个数字单元格上都能满足条件。


示例 2：


输入：n = 2
输出：20
解释：我们可以拨打的所有有效号码为[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72,
76, 81, 83, 92, 94]


示例 3：


输入：n = 3131
输出：136006598
解释：注意取模




提示：


1 <= n <= 5000


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
DIR = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), )  # 8个可能的运动方向
M, N = 4, 3  # 键盘矩阵大小
MOD = int(1e9+7)

class Solution:
    def knightDialer(self, n: int) -> int:
        # dp[i][j] 由i,j作为序列起始点的可选路径个数
        dp = [[1 if (i, j) not in [(3, 0), (3, 2)] else 0 for j in range(N)] for i in range(M)]

        # 键盘矩阵中所有数字坐标
        ij = tuple((i, j) for i in range(M) for j in range(N) if (i, j) not in [(3,0), (3,2)])

        # 通向i,j 的可选点, 由于路径可逆, 所以结果等于i,j出发能成功到达的点
        choice = [[[] for __ in range(M)] for _ in range(M)]
        # 统计i,j的可能落点
        for i, j in ij:
            for di, dj in DIR:
                if 0 <= i + di < M and 0 <= j + dj < N and (i+di, j+dj) not in [(3,0), (3,2)]:
                    choice[i][j].append((i + di, j + dj))
        
        new = [[0] * N for _ in range(M)]
        for k in range(n-1):
            # 计算由i,j作为序列起始点的长度为k的可选路径个数 = 由(i,j)的可选点(ii,jj)作为序列起始点的 长度为k-1的 可选路径个数的 总和
            for i, j in ij:
                new[i][j] = sum(dp[ii][jj] for ii, jj in choice[i][j]) % MOD
            # 更新mat
            # dp = [row.copy() for row in new]  # 滚动更新dp数组(深层复制)
            dp, new = new, dp  # 采用这种方式直接更换对象名称更高效
        
        return sum(dp[i][j] for i, j in ij) % MOD
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

