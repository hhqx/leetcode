
question_content = """
Given a binary tree root, a node X in the tree is named good if in the path 
from root to X there are no nodes with a value greater than X. 

 Return the number of good nodes in the binary tree. 

 
 Example 1: 

 

 
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path. 

 Example 2: 

 

 
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it. 

 Example 3: 

 
Input: root = [1]
Output: 1
Explanation: Root is considered as good. 

 
 Constraints: 

 
 The number of nodes in the binary tree is in the range [1, 10^5]. 
 Each node's value is between [-10^4, 10^4]. 
 

 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 61 👎 0

"""

from typing import *
from binarytree import build, build2, Node, _build_tree_string
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def import_from(self, l_values):
        """ Build a tree from a list of values and return its root node. """
        self.build2(l_values)
        return self

        # tree2 = build2(l_values)
        # print(tree2)
        # return tree2

    def __str__(self):

        lines = _build_tree_string(self, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

    def values2(self) -> List:
        """Return the list representation (version 2) of the binary tree.

        :return: List of node values like those from :func:`binarytree.Node.values`,
            but with a slightly different representation which associates two adjacent
            child values with the first parent value that has not been associated yet.
            This representation does not provide the same indexing properties where if
            a node is at index i, its left child is always at 2i + 1, right child at
            2i + 2, and parent at floor((i - 1) / 2), but it allows for more compact
            lists as it does not hold "None"s between nodes in each level. See example
            below for an illustration.
        :rtype: [float | int | None]
        """
        current_nodes: List[TreeNode] = [self]
        has_more_nodes = True
        node_values: List = [self.val]

        while has_more_nodes:
            has_more_nodes = False
            next_nodes: List[Node] = []

            for node in current_nodes:
                for child in node.left, node.right:
                    if child is None:
                        node_values.append(None)
                    else:
                        has_more_nodes = True
                        node_values.append(child.val)
                        next_nodes.append(child)

            current_nodes = next_nodes

        # Get rid of trailing None values
        while node_values and node_values[-1] is None:
            node_values.pop()

        return node_values

    def __eq__(self, val):
        out = self.values2()
        return out == val

    def build2(self, values: List[int]):
        """Build a tree from a list of values and return its root node.

        :param values: List of node values like those for :func:`binarytree.build`, but
            with a slightly different representation which associates two adjacent child
            values with the first parent value that has not been associated yet. This
            representation does not provide the same indexing properties where if a node
            is at index i, its left child is always at 2i + 1, right child at 2i + 2, and
            parent at floor((i - 1) / 2), but it allows for more compact lists as it
            does not hold "None"s between nodes in each level. See example below for an
            illustration.
        :type values: [float | int | str | None]
        :return: Root node of the binary tree.
        """
        queue: Deque[TreeNode] = deque()
        root: Optional[TreeNode] = None

        if values:
            # root = TreeNode(values[0])
            self.val = values[0]
            root = self
            queue.append(root)

        index = 1
        while index < len(values):
            node = queue.popleft()

            if values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)
            index += 1

            if index < len(values) and values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)
            index += 1

        return root


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, maxVal):
            if root is None:
                return

            if root.val >= maxVal:
                maxVal = root.val
                self.cnt += 1

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
            return

        self.cnt = 0
        dfs(root, -1e9)
        return self.cnt
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
