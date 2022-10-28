#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (71.14%)
# Likes:    1603
# Dislikes: 0
# Total Accepted:    533K
# Total Submissions: 749.3K
# Testcase Example:  '[1,2,3,4]'
#

question_content="""给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。



示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]


示例 2：


# 输入：head = []
# 输出：[]


示例 3：


输入：head = [1]
输出：[1]




提示：


链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100


"""

from tkinter import N
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy

        while True:
            if not node.next or not node.next.next:
                return dummy.next
            # next 为node下一个节点
            next = node.next
            node.next = next.next  # node跳过下一个节点

            # print(next.next)
            next.next = node.next.next  # 让下一个节点指向另一个周期开头
            node.next.next = next  # 让node.next指回被跳过的节点

            node = next  # node移到下一个节点(由于已经reverse, 实则为移动到下一个周期的前一个节点)

        return dummy.next
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

