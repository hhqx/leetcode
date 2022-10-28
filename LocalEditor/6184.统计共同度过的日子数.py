#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode.cn/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (79.07%)
# Likes:    1086
# Dislikes: 0
# Total Accepted:    331.1K
# Total Submissions: 418.7K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#

question_content="""
Alice 和 Bob 计划分别去罗马开会。

给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。Alice 会在日期 arriveAlice 到 leaveAlice 之间在城市里（日期为闭区间），而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。每个字符串都包含 5 个字符，格式为 "MM-DD" ，对应着一个日期的月和日。

请你返回 Alice和 Bob 同时在罗马的天数。

你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。每个月份的天数分别为：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。

示例 1：
28-16+1+18
输入：arriveAlice = "02-15", leaveAlice = "03-18", arriveBob = "02-16", leaveBob = "03-19"
输出：3+28

输入：arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
输出：3

输入：arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
输出：0
解释：Alice 和 Bob 没有同时在罗马的日子，所以我们返回 0 。

"""

from posixpath import split
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def getDate(s):
            dates = []
            for d in s.split('-'):
                dates.append(int(d))
            return dates
        def dataSubs(d1, d2):
            return sum(month[d2[0]:d1[0]]) + d1[1] - d2[1] + 1
        
        dateStr = [arriveAlice, leaveAlice, arriveBob, leaveBob]
        date = [getDate(d) for d in dateStr]
        if date[0] > date[3] or date[1] < date[2]:
            return 0
        else:
            return dataSubs(min(date[1], date[3]), max(date[0], date[2]))
            
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

