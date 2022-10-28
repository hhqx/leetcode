#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Medium (71.13%)
# Likes:    1825
# Dislikes: 0
# Total Accepted:    727.9K
# Total Submissions: 1M
# Testcase Example:  '[7,1,5,3,6,4]'
#

question_content="""You are given an integer array prices where prices[i] is the price of a given
stock on the i^th day.

On each day, you may decide to buy and/or sell the stock. You can only hold
at most one share of the stock at any time. However, you can buy it then
immediately sell it on the same day.

Find and return the maximum profit you can achieve.


Example 1:


Input: prices = [4,3,2,1,2,3,4]
Output: 3


Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
3.
Total profit is 4 + 3 = 7.


Example 2:


Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
5-1 = 4.
Total profit is 4.


Example 3:


Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the
stock to achieve the maximum profit of 0.



Constraints:


1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        
		# It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            
			# either keep hold, or buy in stock today at stock price
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
			
			# either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        # maximum profit must be in not-hold state
        return cur_not_hold if prices else 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 超时 """
        if len(prices)==0:
            return 0
        
        True_K = len(prices)//2
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

    def maxProfit(self, prices: List[int]) -> int:
        """ 贪心 """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

