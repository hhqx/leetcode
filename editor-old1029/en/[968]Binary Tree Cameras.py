
question_content = """
You are given the root of a binary tree. We install cameras on the tree nodes 
where each camera at a node can monitor its parent, itself, and its immediate 
children. 

 Return the minimum number of cameras needed to monitor all nodes of the tree. 

 
 Example 1: 


 
Input: root = [0,0,0,null,0,0,null,null,0]
Output: 2
 
 
Input: root = [0,0,null,null,0,0,null,null,0,0]
Output: 2
 
Input: root = [0,null,0,null,0,0,0]
Output: 2

 
Input: root = [0,null,0,null,0,null,0]
Output: 2

Input: root = [0,1,null,2,3]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
 

 Example 2: 

 
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. 
The above image shows one of the valid configurations of camera placement.
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 1000]. 
 Node.val == 0 
 
 Related Topics Dynamic Programming Tree Depth-First Search Binary Tree 👍 3557 
👎 40

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
class Solution:

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """ 3种状态，子节点状态决定了当前节点是否应该放摄像头，
                如果子节点有没覆盖的就果断加摄像头，
                如果都有覆盖，根据贪心原则，应该给当前节点的母节点加摄像头，
                当前节点状态为无覆盖，留给母节点再判断
            空节点应该为有覆盖但是无摄像头，如果为无覆盖意味着母节点应该放摄像头，但是实际上可以不放，所以设定为有覆盖，并且不放摄像头
        """
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


class Solution:

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        数的最小覆盖问题, 本题应该是数的最小支配集问题

        f[i][0] 表示当前节点不放相机, 子节点i所需的最小相机数
        f[i][1] 表示当前节点放相机, 子节点i所需的最小相机数

        转移方程:
        f[i][0] = sum f[k][1]
        f[i][1] = 1 + sum min( f[k][0], f[k][1] )

        f[leaf][0] = 0
        f[leaf][1] = 1
        """
        from functools import cache
        @cache
        def dfs(node):
            if not node:
                return 0, 0

            fi0, fi1 = 0, 1
            # fk0, fk1 = 0, 0

            for child in [node.left, node.right]:
                if not node:
                    continue
                fk0, fk1 = dfs(child)
                fi0 = fi0 + fk1
                fi1 = fi1 + min(fk0, fk1)

            return fi0, fi1

        return min(dfs(root))

class Solution:
    """ 错误版本, 未考虑儿子对父亲的影响 """
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        数的最小支配集问题

        f[i][0] 表示当前节点放相机, 子节点i所需的最小相机数
        f[i][1] 表示当前节点不放相机, 且被父亲覆盖, 子节点i所需的最小相机数
        f[i][2] 表示当前节点不放相机, 未被父亲覆盖, 子节点i所需的最小相机数

        转移方程:

        f[i][0] = 1 + sum min( f[k][0], f[k][1] )
        f[i][1] = sum min(f[k][0], f[k][2], )
        f[i][2] = sum min(f[k][0])

        输出:
        min(f[root][0], f[root][2])

        边界条件:
        f[leaf][0] = 1
        f[leaf][1] = 0
        f[leaf][2] = inf
        """
        from functools import cache
        @cache
        def dfs(node):
            if node and not node.left and not node.right:
                return 1, 0, float("inf")

            fi0, fi1, fi2 = 1, 0, 0
            for child in [node.left, node.right]:
                if not child:
                    continue
                fk0, fk1, fk2 = dfs(child)
                fi0 = fi0 + min(fk0, fk1)
                fi1 = fi1 + min(fk0, fk2)
                fi2 = fi2 + fk0

            return fi0, fi1, fi2

        return min(dfs(root)[0], dfs(root)[2])

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        数的最小支配集问题


        设 f[i][0] 表示选点 i，且以 i 为根的子树每个点都被覆盖的最少信号塔部署数量；
        f[i][0] 表示当前节点放相机, 子节点i所需的最小相机数
        f[i][1] 表示当前节点不放相机, 且被覆盖, 子节点i所需的最小相机数
        f[i][2] 表示当前节点不放相机, 未被覆盖, 子节点i所需的最小相机数

        转移方程:

        f[i][0] = 1 + sum min( f[k][0], f[k][1], f[k][2],  ) # 当前节点放, 子节点可以任意状态
        f[i][1] = sum min(f[k][0], f[k][1], f[k][2], ) # 当前节点不放, 且至少被一个子节点覆盖, 子节点必须被覆盖
            # 记录下最小值和f[k][0]的差值, 若都大于它, 即没有一个f[k][0]被选中, 则加上它
            f[i][1] = sum min(f[k][0], f[k][1] ) +
                        min(f[k][0] - min(f[k][0], f[k][1] ) )

        f[i][2] = sum min(f[k][1], f[k][2]) # 未被覆盖, 子节点肯定不放

        输出:
        min(f[root][0], f[root][2])

        边界条件:
        f[leaf][0] = 1
        f[leaf][1] = float("inf")
        f[leaf][2] = 0
        """
        from functools import cache
        @cache
        def dfs(node):
            # if node and not node.left and not node.right:
            #     return 0, 0, float('inf')
            if not node:
                return 0, 0, float('inf')

            fi0, fi1, fi2 = 1, 0, 0
            min_fk0_delta = float("inf")
            for child in [node.left, node.right]:
                # if not child:
                #     continue
                fk0, fk1, fk2 = dfs(child)
                fi0 = fi0 + min(fk0, fk1, fk2)
                fi1 = fi1 + min(fk0, fk1)
                min_fk0_delta = min(min_fk0_delta, fk0 - min(fk0, fk1))
                fi2 = fi2 + min(fk0, fk1)

            fi1 = fi1 + min_fk0_delta

            return fi0, fi1, fi2

        # return min(dfs(root)[0]+1, dfs(root)[1])
        return min(dfs(root))
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    question_content = question_content.replace('null', 'None')
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
