
question_content = """
You are given the root of a binary tree with n nodes. Each node is uniquely 
assigned a value from 1 to n. You are also given an integer startValue representing 
the value of the start node s, and a different integer destValue representing 
the value of the destination node t. 

 Find the shortest path starting from node s and ending at node t. Generate 
step-by-step directions of such path as a string consisting of only the uppercase 
letters 'L', 'R', and 'U'. Each letter indicates a specific direction: 

 
 'L' means to go from a node to its left child node. 
 'R' means to go from a node to its right child node. 
 'U' means to go from a node to its parent node. 
 

 Return the step-by-step directions of the shortest path from node s to node t. 


 
 Example 1: 
 
 
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
 

 Example 2: 
 
 
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

 
 Constraints: 

 
 The number of nodes in the tree is n. 
 2 <= n <= 10⁵ 
 1 <= Node.val <= n 
 All the values in the tree are unique. 
 1 <= startValue, destValue <= n 
 startValue != destValue 
 

 Related Topics 树 深度优先搜索 字符串 二叉树 👍 43 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from enum import Enum
class State(Enum):
    NoStartNoEnd = 0
    StartNoEnd = 1
    NoStartEnd = 2
    StartEnd = 3

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start = []
        end = []
        def dfs(node):
            """ 返回值状态含义  0: 无, 1:only has start, 2: only has end, 3: has both start and end"""
            if not node:
                return 0

            # 计算当前节点状态
            val = 0
            if node.val == startValue:
                val += 1
            elif node.val == destValue:
                val += 2

            # 核心算法步骤
            # 调用左右子树, 若子树仅有start则添加'U'返回上一层, 若仅有end则添加左右子树对于的tag, 否则什么也不做
            d = {'L': dfs(node.left), 'R': dfs(node.right)}
            for tag, val_sub in d.items():
                if val_sub == 1:
                    start.append('U')
                elif val_sub == 2:
                    end.append(tag)

            # 等价于对左右子树状态和当前节点状态进行或操作
            return sum(d.values(), val)

        dfs(root)
        # 由于添加路径时是顺序时自底向上, 所以end序列需要reverse操作
        return ''.join(start + end[::-1])


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start = []
        end = []
        def dfs(node):
            """ 返回值状态含义  0: 无, 1:only has start, 2: only has end, 3: has both start and end """
            if not node:
                return 0

            val = 0
            if node.val == startValue:
                val += 1
            elif node.val == destValue:
                val += 2

            # 核心算法步骤
            # 调用左右子树, 若子树仅有start则添加'U'返回上一层, 若仅有end则添加左右子树对于的tag, 否则什么也不做
            l = dfs(node.left)
            r = dfs(node.right)

            if l == 1:
                start.append('U')
            elif l == 2:
                end.append('L')

            if r == 1:
                start.append('U')
            elif r == 2:
                end.append('R')

            # 对左右子树状态和当前节点状态进行或操作, 返回当前子树状态
            return l | r | val

        dfs(root)
        # 由于添加路径时是顺序时自底向上, 所以end序列需要reverse操作
        return ''.join(start + end[::-1])
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
