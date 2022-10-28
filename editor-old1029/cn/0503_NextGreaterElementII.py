
question_content = """
Given a circular integer array nums (i.e., the next element of nums[nums.length 
- 1] is nums[0]), return the next greater number for every element in nums. 

 The next greater number of a number x is the first greater number to its 
traversing-order next in the array, which means you could search circularly to find 
its next greater number. If it doesn't exist, return -1 for this number. 

 
 Example 1: 

 
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
 

 Example 2: 

 
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁴ 
 -10⁹ <= nums[i] <= 10⁹ 
 

 Related Topics 栈 数组 单调栈 👍 703 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return self.dailyTemperatures(nums)


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]  # 升序栈
        result = [-1] * len(temperatures)
        for idx in range(1, 2*len(temperatures)):
            i = idx % len(temperatures)
            temp, s = temperatures[i], temperatures[stack[-1]]
            # 若当前温度小于等于之前温度, 则继续往后面找
            if temp <= s:
                stack.append(i)
            elif temp > s:
                # 把以前温度比当前温度小的值pop出去
                cnt = len(temperatures) - 1
                while len(stack) > 0 and temp > temperatures[stack[-1]] and cnt > 0:
                    idx_in = stack.pop()
                    result[idx_in] = temperatures[i]
                    cnt -= 1
                stack.append(i)
        return result

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)

        nums2 = nums + nums
        delta_idx = self.dailyTemperatures(nums2)
        for i, didx in enumerate(nums):
            didx = delta_idx[i]
            if didx >= len(nums) or didx <= 0:
                pass
            else:
                result[i] = nums2[didx + i]

        return result
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]  # 升序栈
        result = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            temp, s = temperatures[i], temperatures[stack[-1]]
            # 若当前温度小于等于之前温度, 则继续往后面找
            if temp <= s:
                stack.append(i)
            elif temp > s:
                # 把以前温度比当前温度小的值pop出去
                while len(stack) > 0 and temp > temperatures[stack[-1]]:
                    idx_in = stack.pop()
                    result[idx_in] = i - idx_in
                stack.append(i)
        return result
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
