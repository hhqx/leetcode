#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (41.57%)
# Likes:    5860
# Dislikes: 0
# Total Accepted:    808.9K
# Total Submissions: 1.9M
# Testcase Example:  '[1,3]\n[2]'
#

question_content="""Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:


Input: nums1 = [1,2,4,5], nums2 = [1,2,3,4,5]
Output: 3


Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:


Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



Constraints:


nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6


"""

from turtle import right
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 选择较短的数组命名为a, 长度为m, 另一个为b, 长度为n
        if len(nums1) <= len(nums2):
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1
        m, n = len(a), len(b)

        # 二分法查找一对(i,j), 使得
        # a[i] < b[j], a[i+1] >= b[j-1], 其中 j = (m+n-1)//2 - i, 
        # 此时
        #   左集合: {a[0]-a[i], b[0]-b[j-1]} 中每个元素都小于等于
        #   右集合: {a[i+1]-a[m-1], b[j]-b[n-1]}
        # 
        # 计算可知左集合元素个数为: 
        #   i-0+1 + j-1-0+1 = i+1+j = i+1 + (m+n-1)//2 - i = (m+n+1)//2
        # 
        # 因此
        #       当m+n为奇数时左右元素个数分别为: (m+n+1)/2, (m+n-1)/2, 左边多一个
        #       当m+n为偶数时左右元素个数分别为: (m+n)/2, (m+n)/2, 左右一样多


        # 二分法查找一对(i,j), 使得
        # a[i] < b[j], a[i+1] >= b[j-1], 其中 j = (m+n-1)//2 - i,
        # 为了方便边界处理引入了ElementAtIndex(arr: List, idx: int)函数, 
        # 最终若是i等于-1则左集合:{a[0]-a[i], b[0]-b[j-1]} 只剩{b[0]-b[j-1]}
        #     若是i等于m-1则右集合: {a[i+1]-a[m-1], b[j]-b[n-1]} 只剩{b[j]-b[n-1]}
        def ElementAtIndex(arr: List, idx: int):
            """ 为了辅助数组索引, idx在0的左边时返回-inf, 在len(arr)-1右边时返回inf """
            if idx < 0:
                return float('-inf')
            elif idx >= len(arr):
                return float('inf')
            else:
                return arr[idx]
        
        # 开区间二分法查找, 循环不变量
        left, right = -1, m
        while right - left > 1:
            mid = (left + right) // 2
            j = (m + n - 1) // 2 - mid
            if a[mid] < ElementAtIndex(b, j):
                left = mid
            else:
                right = mid
        # 得到所求的i,j
        i = left
        j = (m + n - 1) // 2 - i
        
        # 根据左右部分的最大最小值计算中位数
        if (m+n) % 2 == 1:  # 奇数, 返回左边的最大值
            return max(ElementAtIndex(b, j-1), ElementAtIndex(a, i))
        else:  # 偶数, 返回左边最大值和右边最小值的平均值
            return (
                max(ElementAtIndex(b, j-1), ElementAtIndex(a, i)) + 
                min(ElementAtIndex(b, j), ElementAtIndex(a, i+1))
                ) / 2
    
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

