
question_content = """
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle in the 
histogram. 

 
 Example 1: 
 
 
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
 

 Example 2: 
 
 
Input: heights = [2,4]
Output: 4
 

 
 Constraints: 

 
 1 <= heights.length <= 10⁵ 
 0 <= heights[i] <= 10⁴ 
 

 Related Topics 栈 数组 单调栈 👍 2142 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        next_small = self.nextSmall(heights)
        before_small = self.beforeSmall(heights)
        # before_small = [len(before_small) - i - 1 for i in before_small]

        maxi = []
        for i in range(len(heights)):
            start = before_small[i] + 1
            end = next_small[i] - 1
            area = (end - start + 1) * heights[i]
            maxi.append(area)
        return max(maxi)

    def nextSmall(self, nums):
        """ while next is small, go back to search the stack to find how many elements is smaller than current num. """
        result = [len(nums)] * len(nums)  # 若未找到, 返回边界
        stack_idx = [0]
        for i in range(1, len(nums)):
            n, s = nums[i], nums[stack_idx[-1]]
            while len(stack_idx) > 0 and n < nums[stack_idx[-1]]:
                idx_in = stack_idx.pop()
                result[idx_in] = i

            stack_idx.append(i)
        return result

    def beforeSmall(self, nums):
        result = [-1] * len(nums)  # 若未找到, 返回边界
        stack_idx = [len(nums) - 1]
        for i in range(len(nums)-2, -1, -1):
            n, s = nums[i], nums[stack_idx[-1]]
            while len(stack_idx) > 0 and n < nums[stack_idx[-1]]:
                idx_in = stack_idx.pop()
                result[idx_in] = i

            stack_idx.append(i)
        return result
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
