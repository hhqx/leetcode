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
class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def sortArray(self, nums: List[int]) -> List[int]:
        """ 堆排序 """
        self.heap_sort(nums)
        return nums


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ 归并排序 """

        def merge_sort(nums, l, r):
            if l == r:
                return
            mid = (l + r) // 2
            merge_sort(nums, l, mid)
            merge_sort(nums, mid + 1, r)
            tmp = []
            i, j = l, mid + 1
            while i <= mid or j <= r:
                if i > mid or (j <= r and nums[j] < nums[i]):
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[l: r + 1] = tmp

        merge_sort(nums, 0, len(nums) - 1)
        return nums


import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ 快速排序 """
        def isascending(i, j):
            for k in range(i+1, j):
                if nums[k-1] > nums[k]:
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

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
## 堆排

## 归并排

## 快排

## 冒泡排

## 插排

## 选排

## 希尔排

## 桶排

## 基排

## 计数排


# 其他
## 后缀排序


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
