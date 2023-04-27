question_content = """
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 

 求在该柱状图中，能够勾勒出来的矩形的最大面积。 

 

 示例 1: 

 

 
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
 

 示例 2： 

 

 
输入： heights = [2,4]
输出： 4 

 

 提示： 

 
 1 <= heights.length <=10⁵ 
 0 <= heights[i] <= 10⁴ 
 

 Related Topics 栈 数组 单调栈 👍 2403 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        R = [n] * n
        L = [-1] * n
        st = []
        for i, num in enumerate(heights):
            while st and num < heights[st[-1]]:
                idx = st.pop()
                R[idx] = i
            L[i] = st[-1] if st else -1
            st.append(i)
        ans = 0
        for i in range(n):
            val = (R[i] - L[i] - 1) * heights[i]
            ans = max(ans, val)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
