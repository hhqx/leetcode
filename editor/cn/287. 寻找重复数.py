
question_content = """
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。 

 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。 

 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。 

 

 示例 1： 
测试用例:[3,2,2,2,4]
测试结果:3
期望结果:2
 
输入：nums = [1,3,4,2,2]
输出：2
 

 示例 2： 

 
输入：nums = [3,1,3,4,2]
输出：3
 

 

 提示： 

 
 1 <= n <= 10⁵ 
 nums.length == n + 1 
 1 <= nums[i] <= n 
 nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次 
 

 

 进阶： 

 
 如何证明 nums 中至少存在一个重复的数字? 
 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？ 
 

 Related Topics 位运算 数组 双指针 二分查找 👍 1975 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 快慢指针判环,
        floyd 算法判圈
        基本思路是(这个思路大错特错!): 每个起始点初始化为i, 根据 x = nums[x]-1 进行快慢指针迭代, 找到入环口, 若入环口非节点本身,
            则认为当次循环i的起始点位置为重复元素(实际上不是), 由于理论错误导致写了改了调试了很久很久, 下次直接看答案, 理解了照着敲.
            花时间太多了没用, 不需要自己想出来, 直接看答案
        """
        n = len(nums)

        for i, num in enumerate(nums):
            slow, fast = i, i
            # fast, slow先相遇
            # if i == 4:
            #     print(i)
            while True:
                fast = nums[fast]-1
                fast = nums[fast]-1
                slow = nums[slow]-1
                if fast == slow:
                    break

            # 移动fast, slow到环入口点前一步
            fast = i
            while fast != slow:
                fast = nums[fast]-1
                slow = nums[slow]-1

            # 此时fast指向入口
            if fast != i:
                # 如果入口节点不是当前节点 i, 说明当前节点指向了一个环, 且环中没有自己
                return num

        return None

"""
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return fast

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
