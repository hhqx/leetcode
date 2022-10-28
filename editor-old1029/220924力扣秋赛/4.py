
question_content = """

4. 二叉树灯饰

「力扣嘉年华」的中心广场放置了一个巨型的二叉树形状的装饰树。每个节点上均有一盏灯和三个开关。节点值为 0 表示灯处于「关闭」状态，节点值为 1 表示灯处于「开启」状态。每个节点上的三个开关各自功能如下：

开关 1：切换当前节点的灯的状态；
开关 2：切换 以当前节点为根 的子树中，所有节点上的灯的状态，；
开关 3：切换 当前节点及其左右子节点（若存在的话） 上的灯的状态；
给定该装饰的初始状态 root，请返回最少需要操作多少次开关，可以关闭所有节点的灯。


示例 1：
输入：root = [1,1,0,null,null,null,1]
输出：2


示例 2：
输入：root = [1,1,1,1,null,null,1]
输出：1


输入：root = [0,null,0]
输出：0





"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def closeLampInTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return 0, 0

            zeros, nonzeors = 0, 0
            if node.val == 0:
                zeros += 1
            else:
                nonzeors += 1

            if node.left:
                z, nz = dfs(node.left)
                zeros += z
                nonzeors += nz
            if node.right:
                z, nz = dfs(node.right)
                zeros += z
                nonzeors += nz




        return

# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
