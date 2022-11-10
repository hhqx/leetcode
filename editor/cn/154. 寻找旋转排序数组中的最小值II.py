
question_content = """
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后
可能得到：

 
 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4] 
 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7] 
 

 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..
., a[n-2]] 。 

 给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。 

 你必须尽可能减少整个过程的操作步骤。 

 

 示例 1： 

 
输入：nums = [1,3,5]
输出：1
 

 示例 2： 

 
输入：nums = [2,2,2,0,1]
输出：0
 

 

 提示： 

 
 n == nums.length 
 1 <= n <= 5000 
 -5000 <= nums[i] <= 5000 
 nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转 
 

 

 进阶：这道题与 寻找旋转排序数组中的最小值 类似，但 nums 可能包含重复元素。允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 

 Related Topics 数组 二分查找 👍 557 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        特殊情况下的二分,
        nums[mid] == nums[right] 时, 只能筛选掉一个
        其他情况下, 能二分筛选掉一半

        """
        left, right = 0, len(nums)-1
        while right > left:
            mid = left + right >> 1
            if nums[mid] == nums[right]:
                right = right - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[right]

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
