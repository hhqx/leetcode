#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (74.51%)
# Likes:    783
# Dislikes: 0
# Total Accepted:    175.6K
# Total Submissions: 235.6K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#

question_content="""You are given an array prices where prices[i] is the price of a given stock
on the i^th day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many
transactions as you like, but you need to pay the transaction fee for each
transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).


Example 1:


Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.


Example 2:


Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6



Constraints:


1 <= prices.length <= 5 * 10^4
1 <= prices[i] < 5 * 10^4
0 <= fee < 5 * 10^4


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return
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

