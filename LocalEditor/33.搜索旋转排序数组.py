#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.81%)
# Likes:    2366
# Dislikes: 0
# Total Accepted:    641.8K
# Total Submissions: 1.5M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#

question_content="""整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k],
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。



示例 1：


输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4


示例 2：


输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：


输入：nums = [1], target = 0
输出：-1




提示：


1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-10^4 <= target <= 10^4


"""

import bisect
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(arr, i, j, val):
            """ 二分法查找arr[i:j+1]中是否含有target元素, 如果有返回其索引, 否则返回-1 """
            if val > arr[j] or val < arr[i]:
                return -1
            idx = bisect.bisect_left(arr, val, lo=i, hi=j)
            if i<= idx <= j and arr[idx] == val:
                return idx
            else:
                return -1

        # 二分法查找选择点, 最终[left, right]区间内包含了旋转分界点
        left, right = 0, len(nums)-1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:  # 满足此条件分割点在右侧
                # 左侧为有序数组, 可二分查找是否存在target
                if (idx:=find(nums, left, mid, target)) >= 0:
                    return idx
                
                left = mid
            elif nums[mid] < nums[right]: # 满足此条件分割点在左侧
                # 右侧为有序数组, 可二分查找是否存在target
                if (idx:=find(nums, mid, right, target)) >= 0:
                    return idx

                right = mid
            else:  # 进入此条件说明旋转数组非法
                return None
        
        # [left, right] 长度小于等于2, 比较区间端点是否等于target
        for i in [left, right]:
            if target == nums[i]:
                return i
        else:
            return -1
    
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

