question_content = """
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 

 Notice that the solution set must not contain duplicate triplets. 

 
 Example 1: 

 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not 
matter.
 

 Example 2: 

 
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
 

 Example 3: 

 
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

 
 Constraints: 

 
 3 <= nums.length <= 3000 
 -10⁵ <= nums[i] <= 10⁵ 
 

 Related Topics 数组 双指针 排序 👍 5294 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -1, 0, 1, 1
        """
        nums.sort()
        n = len(nums)

        ans = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复元素
                continue

            # 双指针查找
            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 跳过相同的数
                    while left < right - 1:
                        if nums[left] == nums[left + 1]:
                            left += 1
                        elif nums[right] == nums[right - 1]:
                            right -= 1
                        else:
                            break
                    left += 1
        return list(ans)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
