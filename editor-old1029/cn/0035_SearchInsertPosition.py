
question_content = """
Given a sorted array of distinct integers and a target value, return the index 
if the target is found. If not, return the index where it would be if it were 
inserted in order. 

 You must write an algorithm with O(log n) runtime complexity. 

 
 Example 1: 

 
Input: nums = [1,3,5,6], target = 5
Output: 2
 

 Example 2: 

 
Input: nums = [1,3,5,6], target = 2
Output: 1
 

 Example 3: 

 
Input: nums = [1,3,5,6], target = 7
Output: 4
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁴ 
 -10⁴ <= nums[i] <= 10⁴ 
 nums contains distinct values sorted in ascending order. 
 -10⁴ <= target <= 10⁴ 
 

 Related Topics 数组 二分查找 👍 1687 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            mid_val = nums[mid]
            if target == mid_val:
                return mid
            if left == right:
                idx = mid + 1 if target > mid_val else mid - 1
                return idx
                # if target > mid_val:
                #     idx = mid + 1
                # else:
                #     idx = mid - 1
            if target > mid_val:
                left = mid + 1
            elif target < mid_val:
                right = mid - 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
