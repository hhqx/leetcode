import collections
import heapq

question_content = """
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. You can only 
see the k numbers in the window. Each time the sliding window moves right by one 
position. 

 Return the max sliding window. 

 
测试用例:[1,-9,8,-6,6,4,0,5]
    4
测试结果:[8,8,8,6,5]
期望结果:[8,8,8,6,6]
 
 Example 1: 
测试用例:[9,10,9,-7,-4,-8,2,-6], 5
测试结果:[-7,-7,-7,-7]
期望结果:[10,10,9,2]


Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
 
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

 Example 2: 

 
Input: nums = [1], k = 1
Output: [1]
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁵ 
 -10⁴ <= nums[i] <= 10⁴ 
 1 <= k <= nums.length 
 

 Related Topics 队列 数组 滑动窗口 单调队列 堆（优先队列） 👍 1915 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ 大顶堆滑动窗口求区间最大值 """
        ans = []
        heap = []
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        for i in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            # 如果最大的元素不在窗口内, 弹出
            while True:
                max, idx = heap[0]
                if idx < i + 1 - k:
                    heapq.heappop(heap)
                else:
                    break
            ans.append(-max)

        return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """单调双端队列滑动窗口求区间最大值 """
        ans = []
        q = collections.deque()


        # 队列值大小随着下标递增
        # 入队
        for i in range(k-1):
            while q and nums[i] >= q[0][0]:  # 清空队列中小于当前元素的值
                q.popleft()
            q.appendleft((nums[i], i))

        # 统计当前窗口的最大值
        for i in range(k-1, len(nums)):
            # 入队
            while q and nums[i] >= q[0][0]:  # 清空队列中小于当前元素的值
                q.popleft()
            q.appendleft((nums[i], i))

            # 出队
            # 如果队头最大的元素不在窗口内, 弹出
            while True:
                max, idx = q[-1]
                if idx < i+1 - k:
                    q.pop()
                else:
                    break
            ans.append(max)

        return ans

class Solution3:
    """ 按大小k分块, 维护块内前帧最大值和后缀最大值"""
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        # 计算块前缀最大值
        m = nums[0]
        for i in range(len(nums)):
            if i % k == 0:
                m = nums[i]
            else:
                m = max(m, nums[i])
            prefix[i] = m
        # 计算块后缀最大值
        m = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            if i % k == k-1:
                m = nums[i]
            else:
                m = max(m, nums[i])
            suffix[i] = m

        # i>=k-1时窗口长度才够, i+1-j = k 时, i处的块前缀和j的块后缀构成大小为k的窗口[j,i]
        ans = [max(prefix[i], suffix[i+1-k]) for i in range(k-1, len(nums))]
        return ans


# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
