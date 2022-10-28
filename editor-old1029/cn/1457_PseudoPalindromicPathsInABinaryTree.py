
question_content = """
Given a binary tree where node values are digits from 1 to 9. A path in the 
binary tree is said to be pseudo-palindromic if at least one permutation of the 
node values in the path is a palindrome. 

 Return the number of pseudo-palindromic paths going from the root node to leaf 
nodes. 

 
 Example 1: 

 

 
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three 
paths going from the root node to leaf nodes: the red path [2,3,3], the green 
path [2,1,1], and the path [2,3,1]. Among these paths only red path and green 
path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3
,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (
palindrome).
 

 Example 2: 

 

 
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three 
paths going from the root node to leaf nodes: the green path [2,1,1], the path [
2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-
palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
 

 Example 3: 

 
Input: root = [9]
Output: 1
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 10⁵]. 
 1 <= Node.val <= 9 
 

 Related Topics 位运算 树 深度优先搜索 广度优先搜索 二叉树 👍 54 👎 0

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
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        path_cnt = 0

        def isPreseduoPalindromic(counter):
            odd_cnt = 0
            for n, freq in counter.items():
                if freq % 2 == 1:
                    odd_cnt += 1
                    if odd_cnt >= 2:
                        return False
            return True

        def dfs(node):
            nonlocal path_cnt
            if node is None:
                return

            cnt[node.val] += 1

            if node.left is None and node.right is None:
                if isPreseduoPalindromic(cnt):
                    path_cnt += 1

            dfs(node.left)
            dfs(node.right)

            cnt[node.val] -= 1
            # if cnt[node.val] == 0:
            #     cnt.pop(node.val)

        dfs(root)
        return path_cnt
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
