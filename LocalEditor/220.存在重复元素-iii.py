#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode.cn/problems/contains-duplicate-iii/description/
#
# algorithms
# Hard (29.35%)
# Likes:    658
# Dislikes: 0
# Total Accepted:    87.8K
# Total Submissions: 299.1K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
from collections import defaultdict

question_content="""给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j])
，同时又满足 abs(i - j)  。

如果存在则返回 true，不存在返回 false。



示例 1：


输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
输出：true

示例 2：


输入：nums = [1,0,1,1], indexDiff = 1, valueDiff = 2
输出：true

示例 3：


输入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
输出：false



提示：


0 
-2^31 
0 
0 


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff: int, valueDiff: int) -> bool:
        """ 有序集合滑动窗口法 """
        from sortedcontainers import SortedSet
        s = SortedSet()

        for i in range(0, len(nums)):
            if nums[i] - valueDiff in s:
                return True
            else:
                idx = s.bisect_left(nums[i]-valueDiff)
                if idx < len(s) and s[idx] <= nums[i] + valueDiff:
                    return True
                s.add(nums[i])

            if i >= indexDiff:
                s.remove(nums[i-indexDiff])

        return False

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff: int, valueDiff: int) -> bool:
        """ 借鉴桶排思想, 根据数值 """
        s = dict()
        for i in range(len(nums)):
            idx = nums[i] // max(valueDiff, 1)
            if idx in s:
                return True
            else:
                if idx + 1 in s and s[idx+1] - nums[i] <= valueDiff:
                    return True
                elif idx - 1 in s and nums[i] - s[idx-1] <= valueDiff:
                    return True
                s[idx] = nums[i]

            if i >= indexDiff:
                s.pop(nums[i-indexDiff] // max(valueDiff, 1))
        return False

# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

