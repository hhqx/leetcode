#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (42.36%)
# Likes:    805
# Dislikes: 0
# Total Accepted:    150K
# Total Submissions: 354.2K
# Testcase Example:  '2\n[2,4,1]'
#

question_content="""You are given an integer array prices where prices[i] is the price of a given
stock on the i^th day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k
transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).


Example 1:



Input: k = 2, prices = [6,1,3,2,4,7]
Output: 7



Input: k = 2, prices = []
Output: 0


Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
4-2 = 2.


Example 2:


Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit
= 3-0 = 3.



Constraints:


0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def M(i, j):
            """ 无限制交易次数 """
            nonlocal prices
            if len(prices)==0:
                return 0
            if j <= i + 1:
                return max(prices[j] - prices[i], 0)
            else:
                return max(M(i, j-1) + M(j-1, j), prices[j] - prices[i])
                # if prices[j] > prices[j-1]:
                #     return max(M(i, j-1) + prices[j] - prices[j-1], prices[j] - prices[i])
                # else:
                #     return max(M(i, j-1) + 0, prices[j] - prices[i])
        
        return M(0, len(prices)-1)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        def M(i, j, k) -> int:
            """ 限制交易次数为k, 状态变量设计的有问题, 只计算了一部分情况 """
            nonlocal prices
            if k <= 0:
                return 0
            if j <= i + 1:
                return max(prices[j] - prices[i], 0)
            else:
                # MAX = 0
                # for m in range(i, j):
                #     tmp = M(i, m) + M(m, j)
                #     if tmp > MAX:
                #         MAX = tmp
                    
                    if prices[j] > prices[j-1]:
                        return max(M(i, j-1, k-1) + prices[j] - prices[j-1], prices[j] - prices[i])
                    else:
                        return max(M(i, j-1, k) + 0, prices[j] - prices[i])
        
        return M(0, len(prices)-1, k)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        True_K = min(k, len(prices)//2)
        # dp_hold[i][k] 表示第i天结束有持有股票,有k次买入机会剩余的钱
        # dp_hold[i][0] = 0, dp_hold[0][k] = -prices[0]
        dp_hold = [[0 for i in range(True_K+1)] for i in range(len(prices))]
        dp_sale = [[0 for i in range(True_K+1)] for i in range(len(prices))]
        for k in range(1, True_K+1):
            dp_hold[0][k] = -prices[0]
            # dp_sale[0][k] = prices[0]  # 第一天没有股票不能卖出, 取默认值零
        
        # 状态转移方程
        # dp_hold[i][k] = max(dp_hold[i-1][k], dp_sale[i-1][k-1] - prices[i])
        # dp_sale[i][k] = max(dp_sale[i-1][k], dp_hold[i-1][k] + prices[i])
        
        for i in range(1, len(prices)):
            for k in range(1, True_K+1):
                dp_hold[i][k] = max(dp_hold[i-1][k], dp_sale[i-1][k-1] - prices[i])
                dp_sale[i][k] = max(dp_sale[i-1][k], dp_hold[i-1][k] + prices[i])
        
        return dp_sale[len(prices)-1][True_K]
        
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

