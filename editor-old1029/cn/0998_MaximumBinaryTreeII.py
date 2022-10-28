
question_content = """
A maximum tree is a tree where every node has a value greater than any other 
value in its subtree. 

 You are given the root of a maximum binary tree and an integer val. 

 Just as in the previous problem, the given tree was constructed from a list a (
root = Construct(a)) recursively with the following Construct(a) routine: 

 
 If a is empty, return null. 
 Otherwise, let a[i] be the largest element of a. Create a root node with the 
value a[i]. 
 The left child of root will be Construct([a[0], a[1], ..., a[i - 1]]). 
 The right child of root will be Construct([a[i + 1], a[i + 2], ..., a[a.length 
- 1]]). 
 Return root. 
 

 Note that we were not given a directly, only a root node root = Construct(a). 

 Suppose b is a copy of a with the value val appended to it. It is guaranteed 
that b has unique values. 

 Return Construct(b). 

 
 Example 1: 
 
 
Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: a = [1,4,2,3], b = [1,4,2,3,5]
 

 Example 2: 
 
 
Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: a = [2,1,5,4], b = [2,1,5,4,3]
 

 Example 3: 
 
 
Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: a = [2,1,5,3], b = [2,1,5,3,4]
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 100]. 
 1 <= Node.val <= 100 
 All the values of the tree are unique. 
 1 <= val <= 100 
 

 Related Topics 树 二叉树 👍 138 👎 0

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


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 1
        nums = []
        for val in [True, False]:
            num = 0
            queue = []
            queue.append(root)
            # root.val = False
            root.val = val
            while queue:
                # pop the first node
                node = queue.pop(0)
                # sum node values
                # if node.left is not None or node.right is not None:
                num += node.val

                if node.left != None:
                    node.left.val = not node.val
                    queue.append(node.left)
                if node.right != None:
                    node.right.val = not node.val
                    queue.append(node.right)
            nums.append(num)
            # print(root)
        return min(nums)

    @staticmethod
    def breadth_travel(root):
        """ 利用队列实现树的层次遍历
            Example:
                values = self.breadth_travel(root)
                print(values)
        """
        out = []
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            out.append(node.val)
            # print(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return out
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        root = self.breadth_travel(root, val)
        return root

    def breadth_travel(self, root, value):
        """ 利用队列实现树的层次遍历
            Example:
                values = self.breadth_travel(root)
                print(values)
        """
        # out = []
        queue = []
        pre_root = TreeNode(val=1e9, left=root)
        queue.append(pre_root)
        while queue:
            node = queue.pop(0)
            if value < node.val:
                if node.right is not None and value > node.right.val:
                    new_node = TreeNode(val=value)
                    new_node.left = node.right
                    node.right = new_node
                    break
                    pass
                elif node.left is not None and value > node.left.val:
                    new_node = TreeNode(val=value)
                    new_node.left = node.left
                    node.left = new_node
                    break
                    pass
                elif node.right is None and node.left is None:
                    node.left = TreeNode(val=value)
                    break



            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            # if pre_node is not None:
            #     pre_node.left = TreeNode(val=value)
            #     pre_node.left = node
        # out = root if pre_node.left is not root else pre_root
        return pre_root.left


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        maxx = max(nums)
        i = nums.index(maxx)
        node = TreeNode(maxx)
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return node

    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def a(node):
            if not node: return []
            return a(node.left) + [node.val] + a(node.right)

        b = a(root) + [val]
        return self.constructMaximumBinaryTree(b)

# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content.replace('null', 'None'), Solution)
    TestObj.run_test()
