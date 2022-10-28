question_content = """
Given an integer array nums, return the length of the longest strictly 
increasing subsequence. 

 A subsequence is a sequence that can be derived from an array by deleting some 
or no elements without changing the order of the remaining elements. For 
example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]. 

 
 Example 1: 

 
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
length is 4.
 

 Example 2: 

 
Input: nums = [0,1,0,3,2,3]
Output: 4
 

 Example 3: 

 
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

 
 Constraints: 

 
 1 <= nums.length <= 2500 
 -10⁴ <= nums[i] <= 10⁴ 
 

 
 Follow up: Can you come up with an algorithm that runs in O(n log(n)) time 
complexity? 

 Related Topics 数组 二分查找 动态规划 👍 2826 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *




# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedDict
NUM_MIN, NUM_MAX = int(-1e4), int(1e5)

class class_dp:
    def __init__(self):
        self.dp = SortedDict()

    def find_dp_between_xy(self, x, y):
        ans = -1
        for k, v in self.dp.items():
            if x <= k <= y:
                ans = max(ans, v)
        return ans

    def update(self, k, v):
        self.dp[k] = v
        return True

    def query(self, k):
        return self.dp.get(k, -1)

    def max(self):
        return max(self.dp.values())


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = class_dp()

        for i in range(len(nums)):
            max_dp_before_x = dp.find_dp_between_xy(NUM_MIN, nums[i]-1)

            if max_dp_before_x == -1:
                dp.update(nums[i], 1)
            else:
                v = max(max_dp_before_x + 1, dp.query(nums[i]))
                dp.update(nums[i], v)

        return dp.max()


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
