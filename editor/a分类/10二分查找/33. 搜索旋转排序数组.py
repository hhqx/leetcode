import bisect

question_content = """
整数数组 nums 按升序排列，数组中的值 互不相同 。 

 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+
1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4
,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。 

 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。 

 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。 

 

 示例 1： 

 
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
 

 示例 2： 

 
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1 

 示例 3： 

 
输入：nums = [1], target = 0
输出：-1
 

 

 提示： 

 
 1 <= nums.length <= 5000 
 -10⁴ <= nums[i] <= 10⁴ 
 nums 中的每个值都 独一无二 
 题目数据保证 nums 在预先未知的某个下标上进行了旋转 
 -10⁴ <= target <= 10⁴ 
 

 Related Topics 数组 二分查找 👍 2588 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def in_arr(l, r):
            if not(nums[l] <= target <= nums[r-1]):
                return -1
            idx = bisect.bisect_left(nums, target, lo=l, hi=r)
            if idx < r and nums[idx] == target:
                return idx
            return -1

        left, right = 0, len(nums)
        while left < right:
            mid = left + right >> 1
            if nums[mid] > nums[left]:
                # find in [left, mid]
                if (idx := in_arr(left, mid+1)) != -1:
                    return idx
                left = mid + 1
            else:
                # find in [mid, right)
                if (idx := in_arr(mid, right)) != -1:
                    return idx
                right = mid
        return -1

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
