from functools import cache

question_content = """
You are given two integer arrays nums and multipliers of size n and m 
respectively, where n >= m. The arrays are 1-indexed. 

 You begin with a score of 0. You want to perform exactly m operations. On the 
iᵗʰ operation (1-indexed), you will: 

 
 Choose one integer x from either the start or the end of the array nums. 
 Add multipliers[i] * x to your score. 
 Remove x from the array nums. 
 

 Return the maximum score after performing m operations. 

 
 Example 1: 

 
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14. 

 Example 2: 

 
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

 
 Constraints: 

 
 n == nums.length 
 m == multipliers.length 
 1 <= m <= 10³ 
 m <= n <= 10⁵ 
 -1000 <= nums[i], multipliers[i] <= 1000 
 

 Related Topics 数组 动态规划 👍 77 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """ 记忆式搜索 """
        @cache
        def dfs(k, i, j):
            nonlocal nums, multipliers

            if k < len(multipliers):
                res = max(dfs(k + 1, i + 1, j) + nums[i] * multipliers[k],
                          dfs(k + 1, i, j - 1) + nums[j] * multipliers[k])
            else:
                res = 0

            # print(f'i={i},j={j},k={k}, res={res}')
            # print(f'i-j={i-j}')
            return res

        ans = dfs(0, 0, len(nums) - 1)
        dfs.cache_clear()
        return ans

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """ 动态规划自底向上 """

        # dp数组定义
        # dp[k][i][j] 表示 nums[i:j+1]和multipliers[k:] 最大分数
        dp = [[[0 for i in range(len(nums)+1)] for i in range(len(nums)+1)] for k in range(len(multipliers)+1)]

        # dp数组初始值设置

        # 设置初始值, 此题可以在dp数组中加一维用来初始化
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         dp[0][i][j] = max(nums[i] * multipliers[0],
        #                         nums[j] * multipliers[0])

        # 进行递归
        for k in range(len(multipliers)-1, -1, -1):  # 反序
            for i in range(len(nums)-1, -1, -1):  # 反序
                for j in range(i, len(nums)):
                    dp[k][i][j] = \
                        max(
                            dp[k+1][i+1][j] + nums[i] * multipliers[k],
                            dp[k+1][i][j-1] + nums[j] * multipliers[k]
                            )
        ans = dp[0][0][len(nums) - 1]
        return ans

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """ 动态规划自底向上 """

        # dp数组定义
        # dp[k][i][j] 表示 nums[i:j+1]和multipliers[k:] 最大分数
        dp = [[0 for i in range(len(nums)+1)] for i in range(len(nums)+1)]

        # dp数组初始值设置

        # 进行递归
        for i in range(len(nums)-1, -1+len(multipliers), -1):  # 反序
            for j in range(len(nums)-len(multipliers), len(nums)):
                if i+len(multipliers)-j > len(multipliers):
                    continue
                dp[i][j] = \
                    max(
                        dp[i+1][j] + nums[i] * multipliers[i+len(multipliers) - 1-j],
                        dp[i][j-1] + nums[j] * multipliers[i+len(multipliers) - 1-j]
                        )

        ans = float('-inf')
        for i in range(len(nums)+1):  # 反序
            ans = max(ans, dp[i][len(multipliers)-1])
        # ans = dp[0][0][len(nums) - 1]
        return ans


class Solution:
    """ 优化后的动态规划, 来源网络. """
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(nums), len(multipliers)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        ret = float("-inf")
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + nums[i - 1] * multipliers[i - 1]
            dp[0][i] = dp[0][i - 1] + nums[m - i] * multipliers[i - 1]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i + j > n: continue
                print(i, j)
                dp[i][j] = max(dp[i - 1][j] + nums[i-1] * multipliers[i + j - 1],
                               dp[i][j - 1] + nums[m-1-j+1] * multipliers[i + j - 1])

        for i in range(n + 1):
            # for j in range(n + 1):
            #     if i + j == n:
            #         ret = max(ret, dp[i][j])
            ret = max(ret, dp[i][n - i])
        return ret

class Solution1:
    """ 优化后的动态规划, 来源网络. """
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(nums), len(multipliers)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ret = float("-inf")
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + nums[i - 1] * multipliers[i - 1]

        for i in range(1, n + 1):
            dp[0][i] = dp[0][i - 1] + nums[m - i] * multipliers[i - 1]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i + j > n: continue
                dp[i][j] = max(dp[i - 1][j] + nums[i - 1] * multipliers[i + j - 1],
                               dp[i][j - 1] + nums[m - j] * multipliers[i + j - 1])

        for i in range(n + 1):
            # for j in range(n + 1):
            #     if i + j == n:
            #         ret = max(ret, dp[i][j])
            ret = max(ret, dp[i][n - i])
        return ret
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
