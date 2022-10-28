
question_content = """
Given the root of a binary tree, return the length of the longest path, where 
each node in the path has the same value. This path may or may not pass through 
the root. 

 The length of the path between two nodes is represented by the number of edges 
between them. 

 
 Example 1: 
 
 
Input: root = [1,null,1,1,1,1,1,1]
Output: 4
 
Input: root = [1,4,5,4,4,null,5]
Output: 2 
 
Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e.
 5).
 

 Example 2: 
 
 
Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e.
 4).
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 10⁴]. 
 -1000 <= Node.val <= 1000 
 The depth of the tree will not exceed 1000. 
 

 Related Topics 树 深度优先搜索 二叉树 👍 667 👎 0

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
        self.maxLen = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]):
        def dfs(root: Optional[TreeNode], val):
            if root is None:
                return 0
            llen = dfs(root.left, root.val)
            rlen = dfs(root.right, root.val)
            if root.val == val:
                length = max(llen, rlen) + 1
            else:
                length = 0
            if llen + rlen > self.maxLen:
                self.maxLen = llen + rlen
            return length
        self.maxLen = 0
        # self.longestPath(root)
        dfs(root, None)
        return self.maxLen

    def longestGraph(self, node: Optional[TreeNode]):
        root = node
        if root is None:
            return 0

        length = 0
        len_left = self.longestGraph(root.left)
        len_right = self.longestGraph(root.right)
        if root.left is not None and root.left.val == root.val:
            length += len_left + 1
        if root.right is not None and root.right.val == root.val:
            length += len_right + 1

        if length > self.maxLen:
            self.maxLen = length
        return length

    def longestPath(self, node: Optional[TreeNode]):
        root = node
        if root is None:
            return 0

        len_left = self.longestPath(root.left)
        len_right = self.longestPath(root.right)
        if root.left is not None and root.left.val == root.val:
            len_left += 1
        else:
            len_left = 0
        if root.right is not None and root.right.val == root.val:
            len_right += 1
        else:
            len_right = 0
        length = max(len_left, len_right)

        if len_left + len_right > self.maxLen:
            self.maxLen = len_left + len_right
        return length
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content.replace('null', 'None'), Solution)
    TestObj.run_test()
