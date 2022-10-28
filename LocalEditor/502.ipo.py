#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
# https://leetcode.cn/problems/ipo/description/
#
# algorithms
# Hard (44.63%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    33.2K
# Total Submissions: 74.3K
#

question_content="""Suppose LeetCode will start its IPO soon. In order to sell a good price of
its shares to Venture Capital, LeetCode would like to work on some projects
to increase its capital before the IPO. Since it has limited resources, it
can only finish at most k distinct projects before the IPO. Help LeetCode
design the best way to maximize its total capital after finishing at most k
distinct projects.

You are given n projects where the i^th project has a pure profit profits[i]
and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its
pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize
your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.


Example 1:


Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project
indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project
indexed 2.
Since you can choose at most 2 projects, you need to finish the project
indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.


Example 2:


Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6



Constraints:


1 <= k <= 10^5
0 <= w <= 10^9
n == profits.length
n == capital.length
1 <= n <= 10^5
0 <= profits[i] <= 10^4
0 <= capital[i] <= 10^9


"""

from typing import *
from RunLeetCodeInPycharm import StartTest

# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = sorted(zip(profits, capital), key=lambda x: x[1])
        import heapq 

        heap = []  # 大顶堆
        max_profit = float('-inf')
        for i, (p, c) in enumerate(pairs):
            
            
            while heap and w < c and w >= heap[0][1]:
                w += -heap[0][0]
                k -= 1
                heapq.heappop(heap)
                if k == 0:
                    return w
            
            heapq.heappush(heap, (-p, c))

        while heap and w >= heap[0][1] and k > 0:
            w += -heap[0][0]
            k -= 1
            heapq.heappop(heap)

        return w
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()




