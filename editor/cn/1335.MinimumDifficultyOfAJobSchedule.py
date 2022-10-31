import itertools
import operator

question_content = """
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work 
on the iᵗʰ job, you have to finish all the jobs j where 0 <= j < i). 

 You have to finish at least one task every day. The difficulty of a job 
schedule is the sum of difficulties of each day of the d days. The difficulty of a day 
is the maximum difficulty of a job done on that day. 

 You are given an integer array jobDifficulty and an integer d. The difficulty 
of the iᵗʰ job is jobDifficulty[i]. 

 Return the minimum difficulty of a job schedule. If you cannot find a schedule 
for the jobs return -1. 

 
 Example 1: 
 
 
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
 

 Example 2: 

 
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you 
cannot find a schedule for the given jobs.
 

 Example 3: 

 
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
 

 
 Constraints: 

 
 1 <= jobDifficulty.length <= 300 
 0 <= jobDifficulty[i] <= 1000 
 1 <= d <= 10 
 

 Related Topics 数组 动态规划 👍 83 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """ 动态规划, 状态递推整不明白. gg.. """
        n = len(jobDifficulty)
        # dp[len][d]
        dp = [[float('inf') for __ in range(d+1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = max(jobDifficulty[:i + 1])

        for dd in range(2, d+1):
            for Len in range(dd-1, n):
                seq = list(dp[j][dd - 1] + max(jobDifficulty[j:Len+1]) for j in range(d - 1, Len+1))
                if not seq:
                    dp[Len][dd] = float('inf')
                    continue
                dp[Len][dd] = min(
                    seq
                )
        return dp[n-1][d] if dp[n-1][d] != float('inf') else -1

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """ 记忆化搜索 """
        n = len(jobDifficulty)
        prefix = list(itertools.accumulate(jobDifficulty, operator.add))

        @cache
        def dfs(L, D):
            if L == D:
                return prefix[L-1]
            elif D == 1:
                return max(jobDifficulty[:L])

            ans = float('inf')
            for j in range(D-1, L):
                ans = min(ans, dfs(j, D-1) + max(jobDifficulty[j:L]))
            return ans

        ans = dfs(n, d)
        return ans if ans != float('inf') else -1


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
