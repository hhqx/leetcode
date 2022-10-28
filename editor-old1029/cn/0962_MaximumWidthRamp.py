import bisect

question_content = """
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= 
nums[j]. The width of such a ramp is j - i. 

 Given an integer array nums, return the maximum width of a ramp in nums. If 
there is no ramp in nums, return 0. 

 
 Example 1: 

 
Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 
and nums[5] = 5.
 

 Example 2: 

 
Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 
and nums[9] = 1.
 

 
 Constraints: 

 
 2 <= nums.length <= 5 * 10⁴ 
 0 <= nums[i] <= 5 * 10⁴ 
 

 Related Topics 栈 数组 单调栈 👍 187 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        def bisect_left_descending(a, idx):
            idx = bisect.bisect_right(a[::-1], idx)
            return len(a) - idx

        a = [1,2,3]
        a = [3,2,1,1,1]
        # idx = bisect.bisect_left(a, 2, key=lambda x: -1 * x)
        idx = bisect.bisect_left(a, 2)
        idx = bisect_left_descending(a, 1)
        print(a)

        return idx

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """ 单调栈 o(nlog(n))"""

        # 从右往左遍历数组, 建立升序单调栈
        idx = []
        num = []
        for i in range(len(nums) - 1, -1, -1):
            if not num or nums[i] > num[-1]:
                num.append(nums[i])
                idx.append(i)

        # 统计宽度最长坡
        ans = 0
        for i in range(len(nums)):
            id = bisect.bisect_left(num, nums[i])
            ans = max(ans, idx[id] - i)

        # 若宽度为负, 返回零
        return max(ans, 0)

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """ 单调栈 o(n)"""
        st = []
        for i in range(len(nums)):
            if not st or nums[i] < nums[st[-1]]:
                st.append(i)

        ans = 0
        for i in range(len(nums)-1, -1, -1):
            while st and nums[i] >= nums[st[-1]]:
                v = st.pop()
                ans = max(ans, i-v)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
