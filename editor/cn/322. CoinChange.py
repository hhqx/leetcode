question_content = """
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money. 

 Return the fewest number of coins that you need to make up that amount. If 
that amount of money cannot be made up by any combination of the coins, return -1. 

 You may assume that you have an infinite number of each kind of coin. 

 
 Example 1: 

 
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
 

 Example 2: 

 
Input: coins = [2], amount = 3
Output: -1
 

 Example 3: 

 
Input: coins = [1], amount = 0
Output: 0
 

 
 Constraints: 

 
 1 <= coins.length <= 12 
 1 <= coins[i] <= 2³¹ - 1 
 0 <= amount <= 10⁴ 
 

 Related Topics 广度优先搜索 数组 动态规划 👍 2200 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        无限背包问题, 滚动数组优化

        详细推导: https://leetcode.cn/problems/coin-change/solution/by-flix-su7s/

        """
        # coins.sort(reverse=True)
        n = len(coins)
        INF = float('inf')

        # dp[i][j] 表示 coins[:i+1] 中 取得 j 的最小硬币数
        dp = [INF] * (amount + 1)

        # dp初值, 只有一个元素时
        # for j in range(amount+1):
        #     if j % coins[0] == 0:
        #         dp[j] = j // coins[0]
        #     else:
        #         dp[j] = INF
        for k in range(amount // coins[0] + 1):
            dp[k * coins[0]] = k

        # dp递归
        for i in range(1, n):
            for j in range(coins[i], amount + 1):
                # if j-coins[i] >= 0:
                dp[j] = min(dp[j - coins[i]] + 1, dp[j])

        ans = dp[amount]
        return ans if ans != INF else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ 无限背包问题, 滚动数组优化 """
        # coins.sort(reverse=True)
        n = len(coins)
        INF = float('inf')

        # dp[i][j] 表示 coins[:i+1] 中 取得 j 的最小硬币数
        # dp = [INF] * (amount+1)
        dp = defaultdict(lambda: INF)
        from sortedcontainers import SortedDict
        dp = SortedDict()

        # dp初值, 只有一个元素时
        # for j in range(amount+1):
        #     if j % coins[0] == 0:
        #         dp[j] = j // coins[0]
        #     else:
        #         dp[j] = INF

        # for k in range(amount // coins[0]+1):
        #     dp[k * coins[0]] = k
        dp[0] = 0

        # dp递归
        for i in range(0, n):
            # for j in range(coins[i], amount + 1):
            #     # if j-coins[i] >= 0:
            #     dp[j] = min(dp[j - coins[i]] + 1, dp[j])

            for key in dp:
                # print(key)
                if key + coins[i] <= amount:
                    dp[key + coins[i]] = min(dp.get(key + coins[i], INF), dp[key] + 1)

            # j = coins[i]

        ans = dp.get(amount, INF)
        return ans if ans != INF else -1
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
