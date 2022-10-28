
question_content = """
You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order, and each of their nodes contains a 
single digit. Add the two numbers and return the sum as a linked list. 

 You may assume the two numbers do not contain any leading zero, except the 
number 0 itself. 

 
 Example 1: 
 
 
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
 

 Example 2: 

 
Input: l1 = [0], l2 = [0]
Output: [0]
 

 Example 3: 

 
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

 
 Constraints: 

 
 The number of nodes in each linked list is in the range [1, 100]. 
 0 <= Node.val <= 9 
 It is guaranteed that the list represents a number that does not have leading 
zeros. 
 

 Related Topics Linked List Math Recursion 👍 20912 👎 4128

"""

from typing import *


class ListNode:
    """ 若定义类内方法 import_from_$Data_Type, 在本地调试时会将$Data_Type表示的输入数据导入到类中. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def import_from(self, val: List):
        self.val = val[0]
        node = self
        for v in val[1:]:
            node.next = ListNode(v)
            node = node.next
        return self

    def export_to(self):
        vals = [self.val]
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
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_val = (l1.val + l2.val)
        carry = sum_val // 10
        lout = ListNode(sum_val % 10)
        l1 = l1.next
        l2 = l2.next

        node = lout
        while l1 is not None and l2 is not None:
            sum_val = l1.val + l2.val + carry
            carry = sum_val // 10
            node.next = ListNode(sum_val % 10)

            l1 = l1.next
            l2 = l2.next
            node = node.next

        node.next = l2 if l2 is not None else l1
        while carry != 0:
            if node.next is None:
                node.next = ListNode(carry)
                break
            else:
                node = node.next
            sum_val = carry + node.val
            node.val = sum_val % 10
            carry = sum_val // 10

        return lout
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
