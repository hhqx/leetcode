
question_content = """
Given an array of positive integers nums and a positive integer target, return 
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
 of which the sum is greater than or equal to target. If there is no such 
subarray, return 0 instead. 

 
 Example 1: 

 
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem 
constraint.
 

 Example 2: 

 
Input: target = 4, nums = [1,4,4]
Output: 1
 

 Example 3: 

 
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

 
 Constraints: 

 
 1 <= target <= 10⁹ 
 1 <= nums.length <= 10⁵ 
 1 <= nums[i] <= 10⁴ 
 

 
Follow up: If you have figured out the 
O(n) solution, try coding another solution of which the time complexity is 
O(n log(n)).

 Related Topics 数组 二分查找 前缀和 滑动窗口 👍 1322 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sum = 0
        min_cnt = len(nums)
        while right < len(nums) or sum >= target:
            if sum < target:
                sum += nums[right]
                right += 1
            else:
                sum -= nums[left]
                left += 1
                if right - left < min_cnt:
                    min_cnt = right - left

        if min_cnt >= len(nums):
            return 0
        return min_cnt + 1
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
