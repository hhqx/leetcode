#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode.cn/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (79.07%)
# Likes:    1086
# Dislikes: 0
# Total Accepted:    331.1K
# Total Submissions: 418.7K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#

question_content="""


给你一个长度为 n 下标从 0 开始的数组 nums ，数组中所有数字均为非负整数。对于 0 到 n - 1 之间的每一个下标 i ，你需要找出 nums 中一个 最小 非空子数组，它的起始位置为 i （包含这个位置），同时有 最大 的 按位或运算值 。

换言之，令 Bij 表示子数组 nums[i...j] 的按位或运算的结果，你需要找到一个起始位置为 i 的最小子数组，这个子数组的按位或运算的结果等于 max(Bik) ，其中 i <= k <= n - 1 。
一个数组的按位或运算值是这个数组里所有数字按位或运算的结果。

请你返回一个大小为 n 的整数数组 answer，其中 answer[i]是开始位置为 i ，按位或运算结果最大，且 最短 子数组的长度。

子数组 是数组里一段连续非空元素组成的序列。


# 输入：nums = [0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,32,2,0,0,0,0,0,0,28,16,32,0,0,0,0,0,0,0,1,0,8,0,0,0,0,0,0,0,0,0,32,0,0,0,0,0,0,0,0,16,0,0,0,0,2,0,0,32,0,0,0,4,16,0,4,0,32,0,0,8,0,1,1,0,0,0,0,0]
# 输出：[3,3,2,2,1]

输入：nums = [1,0,2,1,3]
输出：[3,3,2,2,1]
解释：
任何位置开始，最大按位或运算的结果都是 3 。
- 下标 0 处，能得到结果 3 的最短子数组是 [1,0,2] 。
- 下标 1 处，能得到结果 3 的最短子数组是 [0,2,1] 。
- 下标 2 处，能得到结果 3 的最短子数组是 [2,1] 。
- 下标 3 处，能得到结果 3 的最短子数组是 [1,3] 。
- 下标 4 处，能得到结果 3 的最短子数组是 [3] 。
所以我们返回 [3,3,2,2,1] 。


输入：nums = [1,2]
输出：[2,1]
解释：
下标 0 处，能得到最大按位或运算值的最短子数组长度为 2 。
下标 1 处，能得到最大按位或运算值的最短子数组长度为 1 。
所以我们返回 [2,1] 。


"""

from posixpath import split
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        def maxThen(a, b):
            """ 判断除零元素外是否 a[i] > b[i] 均成立. """
            for i in range(len(a)):
                if a[i] != 0 and a[i] <= b[i]:
                    return False
            return True
        
        # 后缀和求每个位上bit1的累加数
        bits = [0] * 32
        orResult = [] 
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(bits)):
                if (nums[i] >> j) & 1:
                    bits[j] += 1
            orResult.insert(0, bits[:])
        
        # 双指针判断区间[left,right]内各个bit和: orResult[left]-orResult[right] 是否均大于等于1
        ans = [0] * len(nums)
        right = len(nums) - 1
        for left in range(len(nums)-1, -1, -1):
            while right > left and maxThen(orResult[left], orResult[right]):
                    right -= 1
                    if right < 0:
                        break
            ans[left] = right - left + 1 

        return ans
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

