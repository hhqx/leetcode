question_content = """
Given the root of a complete binary tree, return the number of the nodes in the 
tree. 

 According to Wikipedia, every level, except possibly the last, is completely 
filled in a complete binary tree, and all nodes in the last level are as far left 
as possible. It can have between 1 and 2ʰ nodes inclusive at the last level h. 

 Design an algorithm that runs in less than O(n) time complexity. 

 
 Example 1: 
 
 
Input: root = [1,2,3,4,5,6]
Output: 6
 

 Example 2: 

 
Input: root = []
Output: 0
 

 Example 3: 

 
Input: root = [1]
Output: 1
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 5 * 10⁴]. 
 0 <= Node.val <= 5 * 10⁴ 
 The tree is guaranteed to be complete. 
 

 Related Topics 树 深度优先搜索 二分查找 二叉树 👍 822 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """ 二分, log(n) * log(n) """
        if not root:
            return 0

        # 计算二叉树深度
        depth = -1
        node = root
        while node:
            node = node.left
            depth += 1
        ldepth = depth

        def existed(root, idx, depth):
            if depth == 0:
                return not not root
            if not root:
                return False
            if idx & (1 << (depth - 1)):
                return existed(root.right, idx, depth - 1)
            else:
                return existed(root.left, idx, depth - 1)

        def existed(root, idx, depth):
            """ idx 为二叉树节点id, 从1开始; depth表示该节点的层数, 从0开始 """
            for i in range(depth-1, -1, -1):
                if not root:
                    return False
                if idx & 1 << i:
                    root = root.right
                else:
                    root = root.left
            return not not root

        # 二分法查找
        left, right = (1 << ldepth), (1 << ldepth + 1)
        while right > left:
            mid = left + right >> 1
            #
            if existed(root, mid, ldepth):
                left = mid + 1
            else:
                right = mid

        # print(existed(root, 6, 2))
        # print(existed(root, 7, 2))

        return right - 1


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
