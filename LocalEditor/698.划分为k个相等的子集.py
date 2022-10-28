#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (41.36%)
# Likes:    795
# Dislikes: 0
# Total Accepted:    80.5K
# Total Submissions: 191K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#

question_content="""给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。



示例 1：


输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

示例 2:


输入: nums = [1,2,3,4], k = 3
输出: false



提示：


1 <= k <= len(nums) <= 16
0 < nums[i] < 10000
每个元素的频率在 [1,4] 范围内


"""

from functools import cache
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 若部分和非总和的整数倍, 返回False
        s = sum(nums)
        if s % k != 0:
            return False
        
        # 若最大元素比部分和大, 返回False
        target = s // k
        nums.sort()  # 为了方便剪枝
        if nums[-1] > target:
            return False

        total, isUsed = 0, 0
        def dfs():
            nonlocal isUsed, total
            # 若所有标志位均为1, 则所有元素满足遍历条件
            if (1 << len(nums)) - 1 == isUsed:
                return True
            
            # 递归全排列
            for i in range(0, len(nums)):
                
                # 若当前元素已访问, 跳过该分支
                if isUsed & (1 << i):
                    continue

                # 若累加和越过了整数倍的分界线, 跳过该分支
                p = total + nums[i]
                if p // target != total // target and p % target != 0:
                    break
                
                total += nums[i]
                isUsed |= (1 << i)
                if dfs():
                    return True
                total -= nums[i]
                isUsed &= ~(1 << i)
            return False
        
        return dfs()

class Solution1:
    """ 记忆式搜索, 利用cache """
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 若部分和非总和的整数倍, 返回False
        s = sum(nums)
        if s % k != 0:
            return False
        
        # 若最大元素比部分和大, 返回False
        target = s // k
        nums.sort()  # 为了方便剪枝
        if nums[-1] > target:
            return False
        
        cnt = 0
        @cache
        def dfs(isUsed, total):
            nonlocal cnt
            cnt += 1
            # 若所有标志位均为1, 则所有元素满足遍历条件
            if (1 << len(nums)) - 1 == isUsed:
                return True
            
            # 递归全排列
            for i in range(0, len(nums)):
                # 若当前元素已访问, 跳过该分支
                if isUsed & (1 << i):
                    continue
                # 若累加和越过target, 跳过该分支, 及后续, 因为太大了
                p = total + nums[i]
                if p > target:
                    break
                
                if dfs(isUsed | (1 << i),  p % target):
                    return True
                
            return False
        
        status = dfs(0, 0)
        dfs.cache_clear()
        print(f'Total Call: {cnt}')
        return status

# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

