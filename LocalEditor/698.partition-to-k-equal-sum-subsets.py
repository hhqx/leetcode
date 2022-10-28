#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (41.37%)
# Likes:    761
# Dislikes: 0
# Total Accepted:    73.8K
# Total Submissions: 176.3K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#

question_content="""Given an integer array nums and an integer k, return true if it is possible
to divide this array into k non-empty subsets whose sums are all equal.


Example 1:


Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3),
(2,3) with equal sums.


Example 2:


Input: nums = [1,2,3,4], k = 3
Output: false



Constraints:


1 <= k <= nums.length <= 16
1 <= nums[i] <= 10^4
The frequency of each element is in the range [1, 4].


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # if sum(nums) % k != 0:
        #     return False
        s, m = 0, 0
        for n in nums:
            m = max(m, n)
            s += n
        if s %k !=0 or n >s/k:
            return False

        nums.sort()
        result_set = []
        result = []
        path = []
        total = 0
        isUsed = [False] * len(nums)

        cnt = 0
        def dfs(startIndex, set_cnt):
            nonlocal total, isUsed, cnt
            
            if set_cnt == k:
                # if len(path) == len(nums):
                result_set.append(path[:])
                return True

            if total % target == 0 and total // target == set_cnt+1:
                
                # result.append(path[:])
                # cnt += 1
                # print(cnt)
                if dfs(0, set_cnt+1):
                    return True
                # result.pop()

                
            
            if total // target != set_cnt:
                return False
            
            if startIndex == len(nums):
                return False
            
            
            for i in range(startIndex, len(nums)):
                # if total + nums[i] > target:
                #     continue
                # if i > startIndex and nums[i] == nums[i-1]:
                #     continue
                # if isUsed[i-1]and nums[i] == nums[i-1]:
                #     continue
                if isUsed[i]:
                    continue
                
                total += nums[i]
                isUsed[i] = True
                path.append(nums[i])
                if dfs(i + 1, set_cnt):
                    return True
                total -= nums[i]
                isUsed[i] = False
                path.pop()
            return False
        
        target = sum(nums) / k
        status = dfs(0, 0)

        # print(result)
        print(len(result_set), result_set)
        return status
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

