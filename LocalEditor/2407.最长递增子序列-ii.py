#
# @lc app=leetcode.cn id=2407 lang=python3
#
# [2407] 最长递增子序列 II
#
# https://leetcode.cn/problems/longest-increasing-subsequence-ii/description/
#
# algorithms
# Hard (24.56%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 12.8K
# Testcase Example:  '[4,2,1,4,3,4,5,8,15]\n3'
#

question_content="""给你一个整数数组 nums 和一个整数 k 。

找到 nums 中满足以下要求的最长子序列：


子序列 严格递增
子序列中相邻元素的差值 不超过 k 。


请你返回满足上述要求的 最长子序列 的长度。

子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。



示例 1：

输入：nums = [4,2,1,4,3,4,5,8,15], k = 3
输出：5
解释：
满足要求的最长子序列是 [1,3,4,5,8] 。
子序列长度为 5 ，所以我们返回 5 。
注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。


示例 2：

输入：nums = [7,4,5,1,8,12,4,7], k = 5
输出：4
解释：
满足要求的最长子序列是 [4,5,8,12] 。
子序列长度为 4 ，所以我们返回 4 。


示例 3：

输入：nums = [1,5], k = 1
输出：1
解释：
满足要求的最长子序列是 [1] 。
子序列长度为 1 ，所以我们返回 1 。




提示：


1 <= nums.length <= 10^5
1 <= nums[i], k <= 10^5


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        return
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

