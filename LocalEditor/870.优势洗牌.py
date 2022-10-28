#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#
# https://leetcode.cn/problems/advantage-shuffle/description/
#
# algorithms
# Medium (47.95%)
# Likes:    214
# Dislikes: 0
# Total Accepted:    30.8K
# Total Submissions: 64.1K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#

question_content="""给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums 的优势可以用满足 nums1[i] > nums2[i] 的索引 i
的数目来描述。

返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。



示例 1：


输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
输出：[2,11,7,15]


示例 2：


输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
输出：[24,32,8,12]




提示：


1 <= nums1.length <= 10^5
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 10^9


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def argsort(seq):
            return sorted(range(len(seq)), key=seq.__getitem__)
        def get_reverse_idx(idx_arr):
            reverse_idx = [0] * len(nums2)
            for i, id in enumerate(idx_arr):
                reverse_idx[id] = i
            return reverse_idx
       
        sort2_idx = argsort(nums2)  # 排序索引映射
        reverse_idx = get_reverse_idx(sort2_idx)  # 逆映射

        # nums2.sort()
        nums1.sort()
        """
        [0,0,2,7,11,15]
        [1,1,1,4,10,16]
        """
        # 双指针法, 若 nums1[right] > nums2_sorted[i], 加入右侧元素到ans[i], 否则加入左侧
        ans = [0] * len(nums1)
        left, right = 0, len(nums1)-1
        for i in range(len(nums1)-1,-1,-1):
            if nums1[right] > nums2[sort2_idx[i]]:
                ans[i] = nums1[right]
                right -= 1
            else:
                ans[i] = nums1[left]
                left += 1
        
        ans = [ans[reverse_idx[i]] for i in range(len(nums1))]
        # print(reverse_idx)
        return ans
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

