#
# @lc app=leetcode.cn id=672 lang=python3
#
# [672] 灯泡开关 Ⅱ
#
# https://leetcode.cn/problems/bulb-switcher-ii/description/
#
# algorithms
# Medium (55.40%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 10.3K
# Testcase Example:  '1\n1'
#

question_content="""房间中有 n 只已经打开的灯泡，编号从 1 到 n 。墙上挂着 4 个开关 。

这 4 个开关各自都具有不同的功能，其中：


开关 1 ：反转当前所有灯的状态（即开变为关，关变为开）
开关 2 ：反转编号为偶数的灯的状态（即 2, 4, ...）
开关 3 ：反转编号为奇数的灯的状态（即 1, 3, ...）
开关 4 ：反转编号为 j = 3k + 1 的灯的状态，其中 k = 0, 1, 2, ...（即 1, 4, 7, 10, ...）


你必须 恰好 按压开关 presses 次。每次按压，你都需要从 4 个开关中选出一个来执行按压操作。

给你两个整数 n 和 presses ，执行完所有按压之后，返回 不同可能状态 的数量。



示例 1：


输入：n = 1, presses = 1
输出：2
解释：状态可以是：
- 按压开关 1 ，[关]
- 按压开关 2 ，[开]


示例 2：


输入：n = 2, presses = 1
输出：3
解释：状态可以是：
- 按压开关 1 ，[关, 关]
- 按压开关 2 ，[开, 关]
- 按压开关 3 ，[关, 开]


示例 3：


输入：n = 3, presses = 1
输出：4
解释：状态可以是：
- 按压开关 1 ，[关, 关, 关]
- 按压开关 2 ，[关, 开, 关]
- 按压开关 3 ，[开, 关, 开]
- 按压开关 4 ，[关, 开, 开]




提示：


1 <= n <= 1000
0 <= presses <= 1000


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if n > 4:
            n = 4 - (n % 2)
        def get_choice(n):
            # sum = 0
            result = []
            path = []
            def dfs(startIndex):
                if len(path) == 4-1:
                    s = sum(path)
                    if s >= n-1:
                        result.append(path[:] + [n-s])
                    return 
                for i in [0, 1]:
                    if sum(path) + i > n:
                        continue
                    path.append(i)
                    dfs(startIndex + 1)
                    path.pop()
            dfs(0)
            return result
        
        # choice = get_choice(1)
        # print(choice)

        choices = [get_choice(i) for i in range(5)]
        choices[2] += choices[0]
        choices[3] += choices[1]
        choices[4] += choices[2]
        # 0 1 2 3 4
        # 1 4 6 4 1
        for row in choices:
            print(row)
        # print(choices)
        return
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

