#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#
# https://leetcode.cn/problems/maximum-profit-in-job-scheduling/description/
#
# algorithms
# Hard (48.61%)
# Likes:    273
# Dislikes: 0
# Total Accepted:    21.2K
# Total Submissions: 38.6K
# Testcase Example:  '[1,2,3,3]\n[3,4,5,6]\n[50,10,40,70]'
#

question_content="""你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。



示例 1：



输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
输出：120
解释：
我们选出第 1 份和第 4 份工作， 
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。


示例 2：

⁠

输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
输出：150
解释：
我们选择第 1，4，5 份工作。 
共获得报酬 150 = 20 + 70 + 60。


示例 3：



输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
输出：6




提示：


1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4


"""

from typing import *
from PythonLeetcodeRunner import *
from collections import defaultdict
import bisect
from functools import cache

# @lc code=start
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        pairs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        startTime, endTime, profit = [], [], []
        for s, e,p in pairs:
            startTime.append(s)
            endTime.append(e)
            profit.append(p)
        
        d = defaultdict()
        @cache
        def dp(t):
            ans = 0
            idx = bisect.bisect_right(endTime, t)
            idx_l = bisect.bisect_left(endTime, t)
            if idx == 0:
                ans = 0
            # elif idx == 1:
            #     return profit[0]
            elif idx_l == idx:
                if endTime[idx] in d:
                    ans = d[endTime[idx_l]]
                else:
                    ans = dp(endTime[idx_l])
                    d[endTime[idx_l]] = ans
                    # return ans
            else:
                ans = 0
                if idx_l-1 >= 0:
                    ans = dp(endTime[idx_l-1])



                for i in range(idx_l, idx):
                    ans = max(ans, dp(startTime[i])  + profit[i])
                d[endTime[idx_l]] = ans
                
                # print(f'dp({t})={ans}')
            
            return ans
        
        # for t in endTime:
        #     print(f't:{t}, dp[t]: {dp(t)}')
        # print(dp(4))
        # print(dp(6))
        
        return dp(endTime[-1])


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """ dfs记忆化递归 + 二分法查找"""

        # 根据结束时间对 startTime, endTime, profit 进行排序
        pairs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        startTime, endTime, profit = zip(*pairs)

        @cache
        def dp(t):
            # 如果输入t小于最小的结束时间, 返回0
            if t < endTime[0]:
                return 0

            ans = 0

            # 从当前t时刻往前搜索,
            # 递推方程为:
            #   若t不在endTime, dp(t) = dp(t_left_nearest_in_endTime)
            #   若在, dp(t) = max(max(dp(start_i)+profit_i) ,dp(t_left_nearest_in_endTime))
            #       其中start_i,profit_i是结束表中等于t的元素对于的起始时间和收益

            # 查找结束点
            # idx 为t在数组endTime中最右侧的位置, 若不存在则是第一个小于t的位置
            idx = bisect.bisect_right(endTime, t) - 1
            # 递推方程
            for i in range(idx, -1, -1):
                if endTime[i] != t:  # 若当前点不在结束表中, 返回t左侧第一个对应的值
                    ans = max(ans, dp(endTime[i]))
                    break
                else:
                    # 若在结束表中, 一直往左搜索, 取搜索的过程中的最大值返回
                    ans = max(ans, dp(startTime[i]) + profit[i])
            return ans

        return dp(endTime[-1])

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """ dfs记忆化递归 + 二分法查找"""
        pairs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        startTime, endTime, profit = zip(*pairs)
        @cache
        def dp(t):
            if t < endTime[0]:
                return 0
            ans = 0
            for i in range(bisect.bisect_right(endTime, t) - 1, -1, -1):
                if endTime[i] != t:  # 若当前点不在结束表中, 返回t左侧第一个对应的值
                    ans = max(ans, dp(endTime[i]))
                    break
                else:
                    ans = max(ans, dp(startTime[i]) + profit[i])
            return ans
        return dp(endTime[-1])
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

