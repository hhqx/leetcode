
question_content = """
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。 

 例如， 

 [2,3,4] 的中位数是 3 

 [2,3] 的中位数是 (2 + 3) / 2 = 2.5 

 设计一个支持以下两种操作的数据结构： 
# 输入: 
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"],
# [[],[1],[2],[],[3],[]]
# 
# 输出: False
 
 void addNum(int num) - 从数据流中添加一个整数到数据结构中。 
 double findMedian() - 返回目前所有元素的中位数。 
 

 示例： 

 addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2 

 进阶: 
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 
 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？ 
 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？ 
 

 Related Topics 设计 双指针 数据流 排序 堆（优先队列） 👍 773 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedList


class MedianFinder:
    """ SortedList 方法.  """
    def __init__(self):
        self.data = SortedList()

    def addNum(self, num: int) -> None:
        self.data.add(num)
        return

    def findMedian(self) -> float:
        # return 0
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2


from sortedcontainers import SortedList

class MedianFinder:
    """ 大顶堆 + 小顶堆 """
    def __init__(self):
        # 左半大顶堆
        self.lheap = []
        # 右半小顶堆
        self.rheap = []

    def addNum(self, num: int) -> None:
        if not self.lheap or num <= -self.lheap[0]:
            # 若左半为空, 或者 num <= max(lheap), 压入左半
            heapq.heappush(self.lheap, -num)
            # 如果左半比右半的长度超过 1 以上, 弹出左半, 压入右半
            if len(self.lheap) > len(self.rheap) + 1:
                val = heapq.heappop(self.lheap)
                heapq.heappush(self.rheap, -val)
        else:
            # 否则压入右半
            heapq.heappush(self.rheap, num)
            # 若右半长度大于左半, 弹出右半, 压入左半
            if len(self.rheap) > len(self.lheap):
                val = heapq.heappop(self.rheap)
                heapq.heappush(self.lheap, -val)
        return

    def findMedian(self) -> float:
        if (len(self.lheap) + len(self.rheap)) % 2 == 1:
            return -self.lheap[0]
        else:
            return (-self.lheap[0] + self.rheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, MedianFinder, isDesignedClass=True)
    TestObj.run_test()
