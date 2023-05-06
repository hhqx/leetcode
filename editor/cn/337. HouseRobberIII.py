question_content = """
The thief has found himself a new place for his thievery again. There is only 
one entrance to this area, called root. 

 Besides the root, each house has one and only one parent house. After a tour, 
the smart thief realized that all houses in this place form a binary tree. It 
will automatically contact the police if two directly-linked houses were broken 
into on the same night. 

 Given the root of the binary tree, return the maximum amount of money the 
thief can rob without alerting the police. 

 
 Example 1: 
 
 
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
 

 Example 2: 
 
 
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 10⁴]. 
 0 <= Node.val <= 10⁴ 
 

 Related Topics 树 深度优先搜索 动态规划 二叉树 👍 1660 👎 0

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
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """ 树形打家劫舍, 树形dp """
        cache = dict()

        def dfs(root, s):
            rid = (id(root), s)
            if rid in cache:
                return cache[rid]
            if not root:
                ans = 0
            else:
                if s == 0:
                    ans = max(dfs(root.left, 1), dfs(root.left, 0)) + max(dfs(root.right, 1), dfs(root.right, 0))
                else:
                    ans = root.val + dfs(root.left, 0) + dfs(root.right, 0)

            cache[rid] = ans
            return ans

        ans = max(dfs(root, 0), dfs(root, 1))
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
