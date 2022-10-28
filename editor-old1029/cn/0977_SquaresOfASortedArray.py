
question_content = """
Given an integer array nums sorted in non-decreasing order, return an array of 
the squares of each number sorted in non-decreasing order. 

 
 Example 1: 

 
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
 

 Example 2: 

 
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁴ 
 -10⁴ <= nums[i] <= 10⁴ 
 nums is sorted in non-decreasing order. 
 

 
Follow up: Squaring each element and sorting the new array is very trivial, 
could you find an 
O(n) solution using a different approach?

 Related Topics 数组 双指针 排序 👍 620 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        head, tail = 0, len(nums) - 1
        squares = []
        ls = nums[head] ** 2
        rs = nums[tail] ** 2
        while head <= tail:
            if ls > rs:
                squares.insert(0, ls)
                head += 1
                ls = nums[head] ** 2
            else:
                squares.insert(0, rs)
                tail -= 1
                rs = nums[tail] ** 2
        return squares
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
