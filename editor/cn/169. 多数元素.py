question_content = """
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。 

 你可以假设数组是非空的，并且给定的数组总是存在多数元素。 

 

 示例 1： 

 
输入：nums = [3,2,3]
输出：3 

 示例 2： 

 
输入：nums = [2,2,1,1,1,2,2]
输出：2
 
测试用例:[3,3,4]
测试结果:4
期望结果:3
 
提示：

 
 n == nums.length 
 1 <= n <= 5 * 10⁴ 
 -10⁹ <= nums[i] <= 10⁹ 
 

 

 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。 

 Related Topics 数组 哈希表 分治 计数 排序 👍 1779 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v > len(nums) // 2:
                return k
        return None

    def majorityElement(self, nums: List[int]) -> int:
        """ 摩尔投票法, 假设为多军乱战, 只要不杀自己人, 最后剩下的一定是target.
        可以想象成一个擂台, 各个人员依次登场, 如果台上无人则上台, 如果台上不是自己人就兑换掉一个, 如果是自己人就加入他们.
        """
        ans = inf
        cnt = 0
        for num in nums:
            if cnt == 0:
                ans = num
                cnt = 1
            elif ans == num:
                cnt += 1
            else:
                cnt -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
