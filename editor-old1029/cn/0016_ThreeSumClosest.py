
question_content = """
Given an integer array nums of length n and an integer target, find three 
integers in nums such that the sum is closest to target. 

 Return the sum of the three integers. 

 You may assume that each input would have exactly one solution. 

 

Input: nums = [4,0,5,-5,3,3,0,-4,-5],
target = -2

测试结果:-1
Output:-2
 


 Example 1: 

 
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

 Example 2: 

 
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).



 
 Constraints: 

 
 3 <= nums.length <= 1000 
 -1000 <= nums[i] <= 1000 
 -10⁴ <= target <= 10⁴ 
 

 Related Topics 数组 双指针 排序 👍 1261 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        -1, 0, 1, 1
        """
        nums.sort()
        n = len(nums)

        ans = 1e9
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复元素
                continue

            # 双指针查找
            left, right = i + 1, n - 1
            hasLarge, hasSmall = False, False
            while left < right:
                # if left < right - 1:
                #     if nums[left] == nums[left + 1]:
                #         left += 1
                #         continue
                #     elif nums[right] == nums[right - 1]:
                #         right -= 1
                #         continue

                # left += 1
                def update(sum):
                    nonlocal ans
                    if abs(sum-target) < abs(ans-target):
                        ans = sum

                sum = nums[i] + nums[left] + nums[right]
                if sum > target:
                    hasLarge = True
                    right -= 1
                    # ans = min(ans, sum, key=lambda x: abs(x-target))
                    update(sum)

                elif sum < target:
                    hasSmall = True
                    left += 1
                    # ans = min(ans, sum, key=lambda x: abs(x-target))
                    update(sum)
                else:
                    # 相等返回零
                    return target
                # if hasLarge and hasSmall:  # 遍历过了零点则退出
                #     break
        return ans


# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
