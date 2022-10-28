#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (57.41%)
# Likes:    1219
# Dislikes: 0
# Total Accepted:    211.1K
# Total Submissions: 367.7K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#

question_content="""You are given an array prices where prices[i] is the price of a given stock
on the i^th day.

Find the maximum profit you can achieve. You may complete at most two
transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).


Example 1:


Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
3.

Example 2:


Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
are engaging multiple transactions at the same time. You must sell before
buying again.


Example 3:


Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.



Constraints:


1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        True_K = min(2, len(prices)//2)
        # dp_hold[i][k] 表示第i天结束有持有股票,有k次买入机会剩余的钱
        # dp_hold[i][0] = 0, dp_hold[0][k] = -prices[0]
        dp_hold = [[0] * (True_K+1) for i in range(len(prices))]
        dp_sale = [[0] * (True_K+1) for i in range(len(prices))]
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

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        """ 官方 """
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2

# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

