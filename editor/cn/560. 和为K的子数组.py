
question_content = """
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。 

 

 示例 1： 
测试用例:[-1,-1,1]
			0
测试结果:3
期望结果:1

输入：nums = [1,1,1], k = 2
输出：2
 

 示例 2： 

 
输入：nums = [1,2,3], k = 3
输出：2
 

 

 提示： 

 
 1 <= nums.length <= 2 * 10⁴ 
 -1000 <= nums[i] <= 1000 
 -10⁷ <= k <= 10⁷ 
 

 Related Topics 数组 哈希表 前缀和 👍 1897 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        s = 0
        ans = 0
        for i in range(n):
            s += nums[i]
            ans += d[s-k]
            d[s] += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
