question_content = """
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。 

 
输入:
["MinStack","push","push","push","min","pop","top","min"]
[[],[-2],[0],[-3],[],[],[],[]]
输出:
[null,null,null,null,-3,null,0,-2]



 MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

 

 提示： 

 
 各函数的调用总次数不超过 20000 次 
 

 

 注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/ 

 Related Topics 栈 设计 👍 404 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        # 从左往右递减, 保存最小值在栈中的索引, 重复最小值只包含一次
        self.minst = []

    def push(self, x: int) -> None:
        if not self.minst or x < self.st[self.minst[-1]]:
            self.minst.append(len(self.st))
        self.st.append(x)

    def pop(self) -> None:
        if not len(self.st):
            return

        if len(self.st) - 1 == self.minst[-1]:
            self.minst.pop()

        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def min(self) -> int:
        return self.st[self.minst[-1]]


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, MinStack, isDesignedClass=True)
    TestObj.run_test()
