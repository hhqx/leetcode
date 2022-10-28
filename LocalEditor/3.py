#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.cn/problems/two-sum/description/
#
# algorithms
# Easy (52.81%)
# Likes:    15265
# Dislikes: 0
# Total Accepted:    3.8M
# Total Submissions: 7.2M
# Testcase Example:  '[2,7,11,15]\n9'
#

question_content="""Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.


Example 1:
# 输入：nums = [2,1,1,1,3,4,1], k = 2
# 输出：[2,3]


输入：nums = [878724,201541,179099,98437,35765,327555,475851,598885,849470,943442], k=4
输出：[4,5]




Follow-up: Can you come up with an algorithm that is less than O(n^2) time
complexity?
"""

from typing import *
from RunLeetCodeInPycharm import StartTest

# @lc code=start
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # 前k段记录正数, 后记录负数
        pos_cnt = 0
        neg_cnt = 0
        for i in range(0, k-1):
            if nums[i+1] - nums[i] > 0:
                pos_cnt += 1
            if nums[k+i+1] - nums[k+i] < 0:
                neg_cnt += 1
        dir = [nums[i+1]-nums[i] for i in range(len(nums)-1)]

        ans = []
        for i in range(k-1, n-k-1):
            if nums[i+1] - nums[i] > 0:
                pos_cnt += 1
            if i-k>=0 and nums[i+1-k] - nums[i-k] > 0:
                pos_cnt -= 1
                
            if nums[k+i+1] - nums[k+i] < 0:
                neg_cnt += 1
            if i-k>=0 and nums[i+1] - nums[i] < 0:
                neg_cnt -= 1
            
            if neg_cnt == 0 and pos_cnt == 0:
                ans.append(i+1)
        return ans

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        dir = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
        
        # 前k段记录正数, 后记录负数
        pos_cnt = 0
        neg_cnt = 0
        
        # 双指针
        ans = []
        left, right = 0, 2*k-1
        while right < n-1:
            lin, lout = left+k-2, left-1
            rin, rout = right, right-(k-1)
            if left == 0:
                for i in range(lout+1, lin+1):
                    pos_cnt += dir[i] > 0
                for i in range(rout+1, rin+1):
                    neg_cnt += dir[i] < 0
            else:
                pos_cnt += dir[lin] > 0
                pos_cnt -= dir[lout] > 0
                neg_cnt += dir[rin] < 0
                neg_cnt -= dir[rout] < 0

            if neg_cnt == 0 and pos_cnt == 0:
                ans.append(left+k)
            
            right += 1
            left += 1

        return ans   
             
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()




