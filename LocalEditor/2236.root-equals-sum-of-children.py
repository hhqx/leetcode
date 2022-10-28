#
# @lc app=leetcode.cn id=2236 lang=python3
#
# [2236] Root Equals Sum of Children
#
# https://leetcode.cn/problems/root-equals-sum-of-children/description/
#
# algorithms
# Easy (86.92%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 10.9K
# Testcase Example:  '[10,4,6]'
#

question_content="""You are given the root of a binary tree that consists of exactly 3 nodes: the
root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its
two children, or false otherwise.


Example 1:


Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are
10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.


Example 2:


Input: root = [5,3,1]
Output: false
Explanation: The values of the root, its left child, and its right child are
5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.



Constraints:


The tree consists only of the root, its left child, and its right child.
-100 <= Node.val <= 100


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

