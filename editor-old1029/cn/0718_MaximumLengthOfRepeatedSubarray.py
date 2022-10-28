question_content = """
Given two integer arrays nums1 and nums2, return the maximum length of a 
subarray that appears in both arrays. 

 
 Example 1: 

 
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
 

 Example 2: 

 
Input: nums1 = [1,2,3], nums2 = [1,2]
Output: 2

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0]
# Output: 4
 

 
 Constraints: 

 
 1 <= nums1.length, nums2.length <= 1000 
 0 <= nums1[i], nums2[i] <= 100 
 

 Related Topics 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希 👍 794 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        def cal_max_subSequence(arr1, arr2):
            """ 计算两数组首尾对齐时最长的公共序列长度 """
            length = 0
            start = -1
            for i in range(len(arr1)):
                if arr1[i] == arr2[i]:
                    length = max(length, i - start)
                else:
                    start = i
            return length

        maxAns = 0
        for i in range(1, m+n):
            # nums1: [n-i, m+n-i) - (n-i)
            # nums2: [0, n)
            start, end = max(n-i, 0), min(m+n-i, n)  # 取两个区间的交集
            # if end - start <= maxAns:  # 若窗口长度小于已知最大长度, 终止循环
            #     break
            # 计算滑动窗口的最长公共子序列
            print(nums1[start-(n-i): end-(n-i)], nums2[start: end],)
            common = cal_max_subSequence(nums1[start-(n-i): end-(n-i)], nums2[start: end], )
            maxAns = max(common, maxAns)

        return maxAns


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
