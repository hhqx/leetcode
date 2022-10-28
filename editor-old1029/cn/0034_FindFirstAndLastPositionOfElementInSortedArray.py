
question_content = """
Given an array of integers nums sorted in non-decreasing order, find the 
starting and ending position of a given target value. 

 If target is not found in the array, return [-1, -1]. 

 You must write an algorithm with O(log n) runtime complexity. 

 
# Example 1: 
# Input: nums = [2,2], target = 1
# Output: [-1,-1] 

 
 
Example 1: 
Input: nums = [1], target = 1
Output: [0,0] 

 
Example 1: 
Input: nums = [1,2,3], target = 2
Output: [1,1] 

 
Example 1: 
Input: nums = [1,3], target = 1
Output: [0,0] 

Example 1: 
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
 
Example 2: 
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 
 Example 3: 
 Input: nums = [], target = 0
Output: [-1,-1]
 
 
 Constraints: 

 
 0 <= nums.length <= 10⁵ 
 -10⁹ <= nums[i] <= 10⁹ 
 nums is a non-decreasing array. 
 -10⁹ <= target <= 10⁹ 
 

 Related Topics 数组 二分查找 👍 1870 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        out = [-1, -1]
        for i, state in enumerate(['left', 'right']):
            left, right = 0, len(nums) - 1
            while 0 <= left <= right <= len(nums):
                mid = (left + right) // 2
                mid_val = nums[mid]

                if state == 'left':
                    if target == mid_val:
                        if mid - 1 < 0 or nums[mid - 1] != target:
                            out[i] = mid
                            break
                        right = mid - 1
                        continue
                elif state == 'right':
                    if target == nums[mid]:
                        if mid + 1 > len(nums) - 1 or nums[mid + 1] != target:
                            out[i] = mid
                            break
                        left = mid + 1
                        continue

                if target > mid_val:
                    left = mid + 1
                elif target < mid_val:
                    right = mid - 1


        return out

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ 左闭右闭区间 """
        out = [None, None]
        for i, state in enumerate(['left', 'right']):
            left, right = 0, len(nums) - 1
            while 0 <= left <= right <= len(nums):
                mid = (left + right) // 2
                mid_val = nums[mid]

                if mid_val > target or (state == 'left' and mid_val >= target):
                    right = mid - 1
                    out[i] = mid
                else:
                    left = mid + 1
        if out[0] is not None and nums[out[0]] == target:
            if out[1] is not None:
                out[1] -= 1
            else:
                out[1] = len(nums) - 1
        else:
            out = [-1, -1]
        return out

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ 左开右开区间, 遵循循环不变量原则,  """
        idx_first, idx_last = -1, -1
        for isSearchFirstElement in [True, False]:
            left, right = -1, len(nums)  # 左开右开区间
            while right - left > 1:
                mid = (right + left) // 2
                mid_val = nums[mid]
                if mid_val < target or (not isSearchFirstElement and mid_val == target):
                    left = mid
                else:
                    right = mid
            # 循环退出时, right = left + 1
            # 若left,right不等于初始区间左右端点(非未定义状态), num[left]<target, nums[right]>target
            # isSearchFirstElement is True, 则num[left]<target, nums[right]>=target
            # isSearchFirstElement is False, 则num[left]<=target, nums[right]>target
            if isSearchFirstElement is True:
                idx_first = right if right < len(nums) and nums[right] == target else -1
            else:
                idx_last = left if left > -1 and nums[left] == target else -1
        return [idx_first, idx_last]
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
