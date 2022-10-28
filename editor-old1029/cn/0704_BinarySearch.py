
question_content = """
Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. If target exists, then 
return its index. Otherwise, return -1. 

 You must write an algorithm with O(log n) runtime complexity. 

 
 Example 1: 

 
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
 

 Example 2: 

 
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁴ 
 -10⁴ < nums[i], target < 10⁴ 
 All the integers in nums are unique. 
 nums is sorted in ascending order. 
 

 Related Topics 数组 二分查找 👍 955 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            # print(f'mid={mid}')
            mid_val = nums[mid]
            if target == mid_val:
                return mid
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
