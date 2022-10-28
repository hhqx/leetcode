
question_content = """
You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[i]). 

 Find two lines that together with the x-axis form a container, such that the 
container contains the most water. 

 Return the maximum amount of water a container can store. 

 Notice that you may not slant the container. 

 
 Example 1: 
 
 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,
7]. In this case, the max area of water (blue section) the container can 
contain is 49.
 

 Example 2: 

 
Input: height = [1,1]
Output: 1
 

 
 Constraints: 

 
 n == height.length 
 2 <= n <= 10⁵ 
 0 <= height[i] <= 10⁴ 
 

 Related Topics 贪心 数组 双指针 👍 3825 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """ 双指针法 """
        maxS = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] > height[right]:
                maxS = max(maxS, (right-left) * height[right])
                right -= 1
            else:
                maxS = max(maxS, (right-left) * height[left])
                left += 1
        return maxS
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
