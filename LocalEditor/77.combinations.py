#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.cn/problems/combinations/description/
#
# algorithms
# Medium (77.22%)
# Likes:    1126
# Dislikes: 0
# Total Accepted:    420.7K
# Total Submissions: 544.8K
# Testcase Example:  '4\n2'
#

question_content="""Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.


Example 1:


Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
be the same combination.


Example 2:


Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.



Constraints:


1 <= n <= 20
1 <= k <= n


"""

from typing import *
from RunLeetCodeInPycharm import StartTest

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n - (k-len(path)-1)):
                path.append(i + 1)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 0)
        return res

# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()




