question_content = """
You are given a 0-indexed 2D integer array transactions, where transactions[i] =
 [costi, cashbacki]. 

 The array describes transactions, where each transaction must be completed 
exactly once in some order. At any given moment, you have a certain amount of money.
 In order to complete transaction i, money >= costi must hold true. After 
performing a transaction, money becomes money - costi + cashbacki. 

 Return the minimum amount of money required before any transaction so that all 
of the transactions can be completed regardless of the order of the 
transactions. 

 
 Example 1: 

 
Input: transactions = [[3,9],[0,4],[7,10],[3,5],[0,9],[9,3],[7,4],[0,0],[3,3],[8,0]]
Output: 24
 
Input: transactions = [[2,1],[5,0],[4,2]]
Output: 10
Explanation:
Starting with money = 10, the transactions can be performed in any order.
It can be shown that starting with money < 10 will fail to complete all 
transactions in some order.
 

 Example 2: 

 
Input: transactions = [[3,0],[0,3]]
Output: 3
Explanation:
- If transactions are in the order [[3,0],[0,3]], the minimum money required to 
complete the transactions is 3.
- If transactions are in the order [[0,3],[3,0]], the minimum money required to 
complete the transactions is 0.
Thus, starting with money = 3, the transactions can be performed in any order.
 

 
 Constraints: 

 
 1 <= transactions.length <= 10⁵ 
 transactions[i].length == 2 
 0 <= costi, cashbacki <= 10⁹ 
 

 Related Topics 贪心 数组 排序 👍 12 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """ 暴力排序 """

    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # 最小值出现在连续负收益结束后开始正收益的点
        Min = float('inf')
        m = 0
        # 负收益根据back正序
        down = [transactions[i] for i in range(len(transactions)) if transactions[i][0] >= transactions[i][1]]
        down.sort(key=lambda x: x[1])
        # 正收益根据cash倒序
        up = [transactions[i] for i in range(len(transactions)) if transactions[i][0] < transactions[i][1]]
        up.sort(key=lambda x: x[0], reverse=True)

        for cash, back in down + up:
            m -= cash
            Min = min(Min, m)
            m += back

        return -Min


class Solution:
    """ 贪心思想 """
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        """ 最小值出现在连续负收益结束前一个点未回款时, 或开始正收益的点刚支出后 """
        money, MaxCash, MaxBack = 0, 0, 0
        for cash, back in transactions:
            if cash >= back:
                money += -cash + back
                MaxBack = max(MaxBack, back)
            else:
                MaxCash = max(MaxCash, cash)

        return -min(money - MaxBack, money - MaxCash)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
