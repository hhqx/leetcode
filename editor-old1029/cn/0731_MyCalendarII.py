
question_content = """
You are implementing a program to use as your calendar. We can add a new event 
if adding the event will not cause a triple booking. 

 A triple booking happens when three events have some non-empty intersection (i.
e., some moment is common to all the three events.). 

 The event can be represented as a pair of integers start and end that 
represents a booking on the half-open interval [start, end), the range of real numbers x 
such that start <= x < end. 

 Implement the MyCalendarTwo class: 

 
 MyCalendarTwo() Initializes the calendar object. 
 boolean book(int start, int end) Returns true if the event can be added to the 
calendar successfully without causing a triple booking. Otherwise, return false 
and do not add the event to the calendar. 
 

 
 Example 1: 

 
Input:
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output:
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, 
because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does 
not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the 
time in [25, 40) will be double booked with the third event, the time [40, 50) will 
be single booked, and the time [50, 55) will be double booked with the second 
event.
 

 
 Constraints: 

 
 0 <= start < end <= 10⁹ 
 At most 1000 calls will be made to book. 
 

 Related Topics 设计 线段树 二分查找 有序集合 👍 208 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = self.add = 0


class SegmentTree:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: int) -> None:
        if l <= lc and rc <= r:
            node.add += v
            node.val += v
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)

    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> int:
        if l <= lc and rc <= r:
            return node.val
        # 先确保所有关联的懒标记下沉下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, 0
        if l <= mid:
            ans = SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同样为不同题目中的更新方式
            ans = max(ans, SegmentTree.query(node.rs, mid + 1, rc, l, r))
        return ans

    @staticmethod
    def pushdown(node: Node) -> None:
        # 懒标记, 在需要的时候才开拓节点和赋值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if not node.add:
            return
        node.ls.add += node.add
        node.rs.add += node.add
        node.ls.val += node.add
        node.rs.val += node.add
        node.add = 0

    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为最大值
        node.val = max(node.ls.val, node.rs.val)

MAX = int(1e9)
class MyCalendarTwo:

    def __init__(self):
        self.rt = SegmentTree().root

    def book(self, start: int, end: int) -> bool:
        # if SegmentTree.query(self.rt, 0, MAX, start, end - 1) < 2:
        #     SegmentTree.update(self.rt, 0, MAX, start, end - 1, 1)
        #     return True
        # return False

        SegmentTree.update(self.rt, 0, MAX, start, end - 1, 1)
        if self.rt.val > 2:
            SegmentTree.update(self.rt, 0, MAX, start, end - 1, -1)
            return False
        return True


class MyCalendarTwo1:
    """ 官方题解 """
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val
            p[1] += val
            self.tree[idx] = p
            return
        mid = (l + r) // 2
        self.update(start, end, val, l, mid, 2 * idx)
        self.update(start, end, val, mid + 1, r, 2 * idx + 1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(self.tree.get(2 * idx, (0,))[0], self.tree.get(2 * idx + 1, (0,))[0])
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start, end - 1, 1, 0, 10 ** 9, 1)
        if self.tree[1][0] > 2:
            self.update(start, end - 1, -1, 0, 10 ** 9, 1)
            return False
        return True

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/my-calendar-ii/solution/wo-de-ri-cheng-an-pai-biao-ii-by-leetcod-wo6n/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, MyCalendarTwo, isDesignedClass=True)
    TestObj.run_test()
