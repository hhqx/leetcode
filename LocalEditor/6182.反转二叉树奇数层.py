#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.cn/problems/two-sum/description/
#
# algorithms
# Easy (52.81%)
# Likes:    15277
# Dislikes: 0
# Total Accepted:    3.8M
# Total Submissions: 7.2M
# Testcase Example:  '[2,7,11,15]\n9'
#

question_content="""

给你一棵 完美 二叉树的根节点 root ，请你反转这棵树中每个 奇数 层的节点值。

例如，假设第 3 层的节点值是 [2,1,3,4,7,11,29,18] ，那么反转后它应该变成 [18,29,11,7,4,3,1,2] 。
反转后，返回树的根节点。

完美 二叉树需满足：二叉树的所有父节点都有两个子节点，且所有叶子节点都在同一层。

节点的 层数 等于该节点到根节点之间的边数。


输入：root = [2,3,5,8,13,21,34]
输出：[2,5,3,8,13,21,34]
解释：
这棵树只有一个奇数层。
在第 1 层的节点分别是 3、5 ，反转后为 5、3 。


输入：root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
输出：[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
解释：奇数层由非零值组成。
在第 1 层的节点分别是 1、2 ，反转后为 2、1 。
在第 3 层的节点分别是 1、1、1、1、2、2、2、2 ，反转后为 2、2、2、2、1、1、1、1 。



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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        q = deque()
        # q = []
        q.append(root)
        depth = 0
        while q:
            stack = []
            qlen = len(q)
            print(qlen)
            for _ in range(qlen):
                node = q.popleft()
                # node = q.pop(0)
                if node is None:
                    break
                
                if depth % 2 == 1:
                    print(node.val)
                    stack.append(node)

                q.append(node.left)
                q.append(node.right)

            if depth % 2 == 1:
                for i in range(len(stack)//2):
                    stack[i].val, stack[len(stack)-1-i].val = stack[len(stack)-1-i].val, stack[i].val
            depth += 1

        return root
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

