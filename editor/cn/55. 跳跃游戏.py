question_content = """
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。 

 数组中的每个元素代表你在该位置可以跳跃的最大长度。 

 判断你是否能够到达最后一个下标。 

 

 示例 1： 

 
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
 

 示例 2： 

 
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
 

 

 提示： 

 
 1 <= nums.length <= 3 * 10⁴ 
 0 <= nums[i] <= 10⁵ 
 

 Related Topics 贪心 数组 动态规划 👍 2297 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
            if reachable >= len(nums) - 1:
                return True

        assert 0, "error"


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            if reachable < i + nums[i]:
                reachable = i + nums[i]
            if reachable >= len(nums) - 1:
                return True

        assert 0, "error"


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
