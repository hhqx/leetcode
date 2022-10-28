
question_content = """
A k-booking happens when k events have some non-empty intersection (i.e., there 
is some time that is common to all k events.) 

 You are given some events [start, end), after each given event, return an 
integer k representing the maximum k-booking between all the previous events. 

 Implement the MyCalendarThree class: 

 
 MyCalendarThree() Initializes the object. 
 int book(int start, int end) Returns an integer k representing the largest 
integer such that there exists a k-booking in the calendar. 
 

 
 Example 1: 

 
Input:
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output:
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is 
disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and 
is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects 
the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the 
maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3
 

 
 Constraints: 

 
 0 <= start < end <= 10⁹ 
 At most 400 calls will be made to book. 
 

 Related Topics 设计 线段树 二分查找 有序集合 👍 186 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class MyCalendarThree:
    def __init__(self):
        from collections import defaultdict
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)
            self.tree[idx] = self.lazy[idx] + max(self.tree[idx * 2], self.tree[idx * 2 + 1])  # 懒惰标记回收

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        # self.update(start, end - 1, 0, 64, 1)
        return self.tree[1]


from sortedcontainers import SortedDict

class MyCalendarThree1:
    """ 差分数组 """
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1

        ans = maxBook = 0
        for freq in self.d.values():
            maxBook += freq
            ans = max(ans, maxBook)
        return ans





# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, MyCalendarThree, isDesignedClass=True)
    TestObj.run_test()
