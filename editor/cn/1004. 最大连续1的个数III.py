question_content = """
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。 

 

 示例 1： 

 
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。 

 示例 2： 

 
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 nums[i] 不是 0 就是 1 
 0 <= k <= nums.length 
 

 Related Topics 数组 二分查找 前缀和 滑动窗口 👍 536 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """ 等价于计算最多包含k个0的最大长度 """
        cnt = 0
        n = len(nums)
        ans = 0
        j = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
            while j <= i and cnt > k:
                cnt -= nums[j] == 0
                j += 1
            ans = max(ans, i - j + 1)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
