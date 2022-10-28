
question_content = """
Given the root of a binary tree, calculate the vertical order traversal of the 
binary tree. 

 For each node at position (row, col), its left and right children will be at 
positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the 
tree is at (0, 0). 

 The vertical order traversal of a binary tree is a list of top-to-bottom 
orderings for each column index starting from the leftmost column and ending on the 
rightmost column. There may be multiple nodes in the same row and same column. In 
such a case, sort these nodes by their values. 

 Return the vertical order traversal of the binary tree. 

 
 Example 1: 
 
 
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column. 

 Example 2: 
 
 
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their 
value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
 

 Example 3: 
 
 
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location 
and should be ordered by their values.
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 1000]. 
 0 <= Node.val <= 1000 
 

 Related Topics 树 深度优先搜索 广度优先搜索 哈希表 二叉树 👍 212 👎 0

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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def findIndexLessThan(nums: list, target):
            """ 二分法查找 """
            left, right = -1, len(nums)
            while right - left > 1:
                mid = (left + right) // 2
                if nums[mid][0] < target[0] or (nums[mid][0] == target[0] and nums[mid][1] < target[1]):
                    left = mid
                else:
                    right = mid
            return left

        left = []
        right = []
        def dfs(root: Optional[TreeNode], posi, layer):
            if root is None:
                return
            # 保存当前节点的值
            if posi >= 0:
                if posi >= len(right):
                    right.append([])
                arr = right[posi]
            elif posi < 0:
                if -1 - posi >= len(left):
                    left.append([])
                arr = left[-1 - posi]
            idx = findIndexLessThan(arr, [layer, root.val]) + 1
            arr.insert(idx, [layer, root.val])

            if root.left is not None:
                dfs(root.left, posi - 1, layer + 1)
            if root.right is not None:
                dfs(root.right, posi + 1, layer + 1)

        dfs(root, 0, 0)
        result = left[::-1] + right
        result = [[col[1] for col in row] for row in result]
        return result
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
