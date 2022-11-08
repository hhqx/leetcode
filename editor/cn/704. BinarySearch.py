
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
 

 Related Topics 数组 二分查找 👍 1037 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisect_left(arr, tar, key=lambda x: x):
            """ 二分法查找 """
            left, right = -1, len(arr)
            while right - left > 1:
                mid = (right + left) // 2
                if arr[mid] < tar:
                    left = mid
                else:
                    right = mid
            return right
        def bisect_right(arr, tar, key=lambda x: x):
            """ 二分法查找 """
            left, right = -1, len(arr)
            while right - left > 1:
                mid = (right + left) // 2
                if arr[mid] <= tar:
                    left = mid
                else:
                    right = mid
            return right

        # Used for test:
        # Note: bisect_left 查找的是 a[i] >= tar 第一个下标,  bisect_right 查找的是 a[i] > tar 的第一个下标
        # bisect_right - bisect_left = 被该元素的出现次数
        a = [1, 2, 2, 3]
        q = [0, 1, 2, 3, 4]
        res_left = [bisect_left(a, num) for num in q]
        res_right = [bisect_right(a, num) for num in q]


        idx = bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
