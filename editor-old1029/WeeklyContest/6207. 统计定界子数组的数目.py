question_content = """
示例 1：

# 输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# 输出：2
解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。
示例 2：

输入：nums = [1,1,1,1], minK = 1, maxK = 1
输出：10
解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。
 

提示：

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106



"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        Min = Max = start = -1
        ans = 0
        for i, n in enumerate(nums):
            if n > maxK or n < minK:
                start = -1
            if n == maxK:
                Max = i
            if n == minK:
                Min = i
            length = max(0, min(Min, Max) - start)
            ans += length
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
