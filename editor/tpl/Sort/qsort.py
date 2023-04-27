question_content = """
给你一个整数数组 nums，请你将该数组升序排列。 






 示例 1： 


输入：nums = [5,2,3,1]
输出：[1,2,3,5]


 示例 2： 


输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]




 提示： 


 1 <= nums.length <= 5 * 10⁴ 
 -5 * 10⁴ <= nums[i] <= 5 * 10⁴ 


 Related Topics 数组 分治 桶排序 计数排序 基数排序 排序 堆（优先队列） 归并排序 👍 735 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)

import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ 快速排序 """

        def isascending(i, j):
            for k in range(i + 1, j):
                if nums[k - 1] > nums[k]:
                    return False
            return True

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partion(l, r):
            """ 输入区间[l,r), 返回p, s.t. nums[i] < nums[p] <= nums[j],
            i 属于 [l, p),  j 属于 (p, r)

            """
            # 选取主元, 放到区间最后一个元素
            p = random.randint(0, r - l - 1) + l
            swap(p, r - 1)
            # left 指向第一个大于等于p的点, 若没有则指向当前点
            left = l
            for i in range(l, r - 1):
                # 如果当前的点小于主元, 换到前半部分去, nums[i]一定大于等于pivot
                if nums[i] <= nums[r - 1]:
                    swap(i, left)
                    left += 1
            # 交换主元到正确的位置
            swap(left, r - 1)
            return left

        def quickSort(l, r):
            """ 对区间 [l, r) 内的元素进行快排 """
            if r - l <= 1:
                return
            if isascending(l, r):
                return
            pos = partion(l, r)
            quickSort(l, pos)
            quickSort(pos + 1, r)

        quickSort(0, len(nums))
        return nums



# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
