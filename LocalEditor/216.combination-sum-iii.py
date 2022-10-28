#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.cn/problems/combination-sum-iii/description/
#
# algorithms
# Medium (72.33%)
# Likes:    542
# Dislikes: 0
# Total Accepted:    196K
# Total Submissions: 271.1K
#

question_content="""Find all valid combinations of k numbers that sum up to n such that the
following conditions are true:


Only numbers 1 through 9 are used.
Each number is used at most once.


Return a list of all possible valid combinations. The list must not contain
the same combination twice, and the combinations may be returned in any
order.


Example 1:


Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:


Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.


Example 3:


Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is
1+2+3+4 = 10 and since 10 > 1, there are no valid combination.



Constraints:


2 <= k <= 9
1 <= n <= 60


"""

from typing import *
from RunLeetCodeInPycharm import StartTest

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        total = n
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                if sum(path) == total:
                    res.append(path[:])
                return
            for i in range(StartIndex, n - (k-len(path)-1)):
                path.append(i + 1)
                if sum(path) <= total:
                    backtrack(n, k, i+1)
                path.pop()
        
        
        backtrack(9, k, 0)
        return res
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()




