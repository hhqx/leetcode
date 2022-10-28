
question_content = """
Given the head of a linked list and an integer val, remove all the nodes of the 
linked list that has Node.val == val, and return the new head. 

 
 Example 1: 
 
 
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
 

 Example 2: 

 
Input: head = [], val = 1
Output: []
 

 Example 3: 

 
Input: head = [7,7,7,7], val = 7
Output: []
 

 
 Constraints: 

 
 The number of nodes in the list is in the range [0, 10⁴]. 
 1 <= Node.val <= 50 
 0 <= val <= 50 
 

 Related Topics 递归 链表 👍 1008 👎 0

"""

from typing import *

class ListNode:
    """ 若定义类内方法 import_from_$Data_Type, 在本地调试时会将$Data_Type表示的输入数据导入到类中. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def import_from(self, head: List):
        val = head
        self.val = val[0] if len(val) > 0 else None
        node = self
        for v in val[1:]:
            node.next = ListNode(v)
            node = node.next
        return self

    def export_to(self):
        vals = [self.val] if self.val else []
        # if vals[0] is None:
        #     vals = vals[1:]
        node = self.next
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals

    def __str__(self):
        return f'{self.export_to()}'

    def __eq__(self, list_in):
        return list_in == self.export_to()


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
    # 三种思路：分别对应method1,2,3
    # 1.删除节点分为两种情况，删除头节点和非头节点
    # 2.添加一个虚拟头节点，对头节点的删除操作与其他节点一样
    # 3.递归
"""
# method1
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            # 让自head起第一个值不为val的节点作为头节点
            # 退出while循环时，有两种情况
            # 1 head为空(即链表左右节点值均为val，则进入if并return
            # 2 找到了第一个值不为val的节点(是真正的头节点)，那么之后就开始对该节点之后的非头节点的元素进行遍历处理
            head = head.next
        if head is None:
            return head
        node = head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head

# method2
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre_node = ListNode(next=head)
        node = pre_node
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return pre_node.next


# method3
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> ListNode:
        if head is None:
            return head
        head.next = self.removeElements(head.next, val)
        # 利用递归快速到达链表尾端，然后从后往前判断并删除重复元素
        return head.next if head.val == val else head
        # 每次递归返回的为当前递归层的head(若其值不为val)或head.next
        # head.next及之后的链表在深层递归中已经做了删除值为val节点的处理，
        # 因此只需要判断当前递归层的head值是否为val，从而决定head是删是留即可
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
