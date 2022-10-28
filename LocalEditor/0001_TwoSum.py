
question_content = """
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target. 

 You may assume that each input would have exactly one solution, and you may 
not use the same element twice. 

 You can return the answer in any order. 

 
 Example 1: 

 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 

 Example 2: 

 
Input: nums = [3,2,4], target = 6
Output: [1,2]
 

 Example 3: 

 
Input: nums = [3,3], target = 6
Output: [0,1]
 

 
 Constraints: 

 
 2 <= nums.length <= 10⁴ 
 -10⁹ <= nums[i] <= 10⁹ 
 -10⁹ <= target <= 10⁹ 
 Only one valid answer exists. 
 

 
Follow-up: Can you come up with an algorithm that is less than 
O(n²) time complexity?

 Related Topics 数组 哈希表 👍 15197 👎 0

"""

from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] + nums[j] == target:
        #             return [j, i]

        nums_index = sorted(range(len(nums)), key=lambda k: nums[k])
        nums = sorted(nums)

        # import numpy as np
        # M = np.array(nums).reshape([1, -1]) + np.array(nums).reshape([-1, 1])

        if nums[0] + nums[1] > target:
            return None

        i, j = 0, 1
        for i in range(len(nums)):
            last_res = 0
            j = i + 1 if j < i + 1 else j
            j = len(nums) - 1 if j >= len(nums) else j
            while j >= i + 1 and j < len(nums):
                res = nums[i] + nums[j] - target
                # print(f'\nsum={nums[i] + nums[j]}')
                # print(f'res={nums[i] + nums[j]}')
                # print(f'i={i}, last_res * res={last_res * res}')

                if res == 0:
                    print(f'res={nums[i] + nums[j]}')
                    print(f'{nums[i]}, {nums[j]}')
                    return [nums_index[i], nums_index[j]]
                elif res < 0:
                    j = j + 1
                elif res > 0:
                    j = j - 1
                if last_res * res < 0:
                    break
                last_res = res
        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = {}
        for i, n in enumerate(nums):
            if n in subs.keys():
                out = [subs[n], i]
                return out
            else:
                subs[target - n] = i
        return None

# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
