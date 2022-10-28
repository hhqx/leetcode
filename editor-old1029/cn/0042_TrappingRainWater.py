
question_content = """
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it can trap after raining. 

 
 Example 1: 
 
 
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,
1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are 
being trapped.
 

 Example 2: 

 
Input: height = [4,2,0,3,2,5]
Output: 9
 

 
 Constraints: 

 
 n == height.length 
 1 <= n <= 2 * 10⁴ 
 0 <= height[i] <= 10⁵ 
 

 Related Topics 栈 数组 双指针 动态规划 单调栈 👍 3773 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """ 单调栈 """
    def trap(self, height: List[int]) -> int:
        volume = 0
        stack_idx = [0]
        for i in range(1, len(height)):
            h = height[i]
            s = height[stack_idx[-1]]
            if h < s:
                stack_idx.append(i)
            else:
                last_s = s
                while len(stack_idx) > 0 and h >= height[stack_idx[-1]]:
                    s = height[stack_idx[-1]]
                    idx_in = stack_idx.pop()
                    # 纵向累加
                    volume += (i - idx_in - 1) * (s - last_s)
                    last_s = s
                if len(stack_idx) > 0:
                    # 若栈非空, 当前值不是最高点, 需加上额外的条形块
                    volume += (i - stack_idx[-1] - 1) * (h - last_s)
                stack_idx.append(i)
        return volume

class Solution:
    """ 双指针方法 o(n) """
    def trap(self, height: List[int]) -> int:

        ans = 0
        left, right = 0, len(height) - 1
        lmax, rmax = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                if height[left] > lmax:
                    lmax = height[left]
                else:
                    ans += lmax - height[left]
                left += 1
            else:
                if height[right] > rmax:
                    rmax = height[right]
                else:
                    ans += rmax - height[right]
                right -= 1
        return ans

class Solution:
    """ 左右找最大值再去重叠 """
    def trap(self, height: List[int]) -> int:

        volume = 0
        lmax = [height[0]]
        for i in range(1, len(height)):
            lmax.append(max(lmax[-1], height[i]))

        rmax = [height[-1]]
        for i in range(len(height)-1-1, -1, -1):
            rmax.insert(0, max(rmax[0], height[i]))

        for i in range(len(height)):
            volume += min(lmax[i], rmax[i]) - height[i]

        # volume = sum(lmax) + sum(rmax) - lmax[-1] * len(height) - sum(height)
        return volume
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
