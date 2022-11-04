import bisect

question_content = """
You are given a 0-indexed array of integers nums of length n. You are initially 
positioned at nums[0]. 

 Each element nums[i] represents the maximum length of a forward jump from 
index i. In other words, if you are at nums[i], you can jump to any nums[i + j] 
where: 

 
 0 <= j <= nums[i] and 
 i + j < n 
 

 Return the minimum number of jumps to reach nums[n - 1]. The test cases are 
generated such that you can reach nums[n - 1]. 

 
 
测试用例:[1,2,3]
测试结果:1
期望结果:2
 
 Example 1: 

 
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 
step from index 0 to 1, then 3 steps to the last index.
 

 Example 2: 

 
Input: nums = [2,3,0,1,4]
Output: 2
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁴ 
 0 <= nums[i] <= 1000 
 

 Related Topics 贪心 数组 动态规划 👍 1858 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        """ 动态规划, 时间复杂度: o( n * log(n) ) """
        n = len(nums)
        dp = [float('inf')] * n
        # dp[i] 表示 i 跳到 n-1 的最小次数
        dp[n - 1] = 0

        st = deque([n-1])
        for i in range(n - 1 - 1, -1, -1):
            """

            # 1 2 3 4
            2 => 2
            2.5 => 2
            所以是 bisect_right - 1

            """

            tmp = i + nums[i]
            idx = bisect.bisect_right(st, tmp) - 1
            if idx >= 0:
                dp[i] = dp[st[idx]] + 1

            while st and dp[i] <= dp[st[0]]:
                st.popleft()
            st.appendleft(i)

        return dp[0]


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        贪心法, 时间复杂度: o( n )

        1. 根据贪心原则选择下一跳的落点, 贪心原则是:
            找出具有最远下一跳的落点的下一跳

        2. 算法过程:
            (1). 对于当前点 start 根据其步长往后遍历至 start + nums[start], 找到找出具有最远下一跳的落点的下一跳, 记为 maxNext
            (2) 对于 (1). 中的 next, 若 next 已经到达终点, 退出并返回 step + 1
            (3). 更新 start 为 maxNext, step += 1

        3. 由于下一跳的所有下一跳中必定有一个超出了当前下一跳的范围, 否则到不了终点, 以实际上算法的时间复杂度不超过 o(n), 考虑每一跳步长都是 1 的情况需要跳 n 次, 故算法的时间复杂度为: o(n).

        """
        step = 0

        if len(nums) == 1:
            return 0

        start = 0
        while start < len(nums):
            maxNext = None
            for next in range(start + 1, start + nums[start] + 1):
                if next >= len(nums) - 1:
                    return step + 1
                # 贪心地选择下一个能到达最远位置的做为下一跳的点
                if maxNext is None:
                    maxNext = next
                else:
                    maxNext = max(maxNext, next, key=lambda x: (x + nums[x], x))

            start = maxNext
            step += 1

        return step
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
