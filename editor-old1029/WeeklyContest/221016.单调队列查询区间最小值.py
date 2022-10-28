import random

question_content = """
示例 1：

# # 输入：nums = [1,3,5,2,7,5]
# # 输出：2
# 解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。
# 示例 2：


Input: [2, 7, 3]
Output: [[0, 0, 2], [0, 1, 2], [0, 2, 2], [1, 1, 7], [1, 2, 3], [2, 2, 3]]

Input: [7, 7, 7, 8, 4]
Output: [[0, 0, 7], [0, 1, 7], [0, 2, 7], [0, 3, 7], [0, 4, 4], [1, 1, 7], [1, 2, 7], [1, 3, 7], [1, 4, 4], [2, 2, 7], [2, 3, 7], [2, 4, 4], [3, 3, 8], 
[3, 4, 4], [4, 4, 4]]

Input: [5, 9, 3, 9, 4, 2, 8, 4, 2, 8]
Output: [[0, 0, 5], [0, 1, 5], [0, 2, 3], [0, 3, 3], [0, 4, 3], [0, 5, 2], [0, 6, 2], [0, 7, 2], [0, 8, 2], [0, 9, 2], [1, 1, 9], [1, 2, 3], [1, 3, 3], 
[1, 4, 3], [1, 5, 2], [1, 6, 2], [1, 7, 2], [1, 8, 2], [1, 9, 2], [2, 2, 3], [2, 3, 3], [2, 4, 3], [2, 5, 2], [2, 6, 2], [2, 7, 2], [2, 8, 2], [2, 9, 2]
, [3, 3, 9], [3, 4, 4], [3, 5, 2], [3, 6, 2], [3, 7, 2], [3, 8, 2], [3, 9, 2], [4, 4, 4], [4, 5, 2], [4, 6, 2], [4, 7, 2], [4, 8, 2], [4, 9, 2], [5, 5, 
2], [5, 6, 2], [5, 7, 2], [5, 8, 2], [5, 9, 2], [6, 6, 8], [6, 7, 4], [6, 8, 2], [6, 9, 2], [7, 7, 4], [7, 8, 2], [7, 9, 2], [8, 8, 2], [8, 9, 2], [9, 9
, 8]]




提示：

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106



"""

from typing import *
from PythonLeetcodeRunner import *


def get_testcase() -> List[List[int]]:
    import numpy as np
    for length in [3,5,10]:
        nums = np.random.randint(0, 10, length)
        ans = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                mn = min(nums[i:j + 1])
                ans.append([i, j, mn])
        ans.sort(key=lambda x: (x[0], x[1]))

        print(f'Input: {list(nums)}')
        print(f'Output: {ans}\n')
    return ans
# get_testcase()


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubarrays(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ans = 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
