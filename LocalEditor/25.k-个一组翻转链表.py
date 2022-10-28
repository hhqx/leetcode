#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (67.70%)
# Likes:    1831 
# Dislikes: 0
# Total Accepted:    407.6K
# Total Submissions: 602.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#

question_content="""给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。



示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]


示例 2：




输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]



提示：


链表中的节点数目为 n
1 <= k <= n <= 5000
0 <= Node.val <= 1000




进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？




"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 虚拟头结点
        dummy = ListNode(0, head)
        
        # start是当前周期的开始节点, end是上一个周期的结束节点
        start = head
        end = dummy

        while True:
            # 移动快指针到当前周期末尾后一个节点
            fast = start
            for _ in range(k):
                if not fast:  # 如果当前为空, 直接返回结果
                    return dummy.next
                fast = fast.next

            # reverse当前周期的链表, 对于每个slow, 将它next链接到前一个
            slow = start
            lastslow = fast
            for _ in range(k):

                tmp = slow.next  # 保存下一个节点指针
                slow.next = lastslow  # 链接到上一个
                lastslow = slow  # 更新上一个节点
                slow = tmp  # slow指针右移, 开始下一个循环

                # 不知道为什么不可以使用这种方式
                # slow.fast, lastslow, slow = lastslow, slow, slow.fast
                # slow, slow.fast, lastslow = slow.fast, lastslow, slow

            # 更新end, start
            end.next = lastslow  # 将上一个节点的指向, 更新为指向这个周期的最后一个(reverse后第一个)
            end = start
            start = fast
        
        return dummy.next
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

