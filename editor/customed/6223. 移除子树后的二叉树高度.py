
question_content = """

6223. 移除子树后的二叉树高度:
    https://leetcode.cn/contest/weekly-contest-317/problems/height-of-binary-tree-after-subtree-removal-queries/


输入：root = [1,null,5,3,null,2,4], queries = [3,5,4,2,4]
输出：[1,0,3,3,3]



输入：root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
输出：[2]
解释：上图展示了从树中移除以 4 为根节点的子树。
树的高度是 2（路径为 1 -> 3 -> 2）。
示例 2：



输入：root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
输出：[3,2,3,2]
解释：执行下述查询：
- 移除以 3 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 4）。
- 移除以 2 为根节点的子树。树的高度变为 2（路径为 5 -> 8 -> 1）。
- 移除以 4 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 6）。
- 移除以 8 为根节点的子树。树的高度变为 2（路径为 5 -> 9 -> 3）。
"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries) -> List[int]:
        """ 暴力解法(超时): 对于每个query都dfs一遍. """
        def dfs(node):
            nonlocal target
            if not node or node.val == target:
                return -1
            return max(dfs(node.left), dfs(node.right), ) + 1

        ans = []
        for i, target in enumerate(queries):
            depth = dfs(root)
            ans.append(depth)
        return ans

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries) -> List[int]:
        """
        dfs遍历 + 字典维护每个节点层数 + 小顶堆维护深度最大的两颗子树
        1. dfs遍历一遍二叉树, 保存每个元素的层数, 保存每层最大深度的两颗子树(记录下该层最大两颗子树的根节点值和深度)
        2. 对于每个queries[i], 先找到其对应的层数l, 再找到该层最大的子树深度 subDepth, ans[i] = l + subDepth,
            先找到其对应的层数l, 再去该层最大的两颗子树中找根节点值不等于queries[i]的子树, 记录最大的子树深度, 若不存在, 记录-1
        """
        import heapq

        layer = defaultdict(list)  # 记录层数到该层最大深度两颗子树的映射
        val2layer = dict()  # 字典映射, 记录节点值到节点层数的映射

        def dfs(node, i):
            nonlocal layer, val2layer

            if not node:
                return -1

            # 记录当前节点值的层数
            val2layer[node.val] = i

            # dfs求当前节点深度
            ld, rd = dfs(node.left, i + 1), dfs(node.right, i + 1)
            depth = max(ld, rd) + 1  # 当前子树深度等于左右子树最大深度 + 1

            # 压入当前节点所代表的子树深度
            heapq.heappush(layer[i], (depth, node.val))
            while len(layer[i]) > 2:  # 仅需保存两颗深度最大的子树
                heapq.heappop(layer[i])

            return depth

        # dfs遍历, 维护 layer, val2layer
        dfs(root, 0)

        # 查询每个queries[i]的结果
        ans = []
        for i, target in enumerate(queries):
            l = val2layer[target]  # l为当前查询的节点层数
            subDepth = [subD for subD, val in layer[l] if val != target]  # 筛选该层不等于当前查询值的子树
            # 查询结果 = 节点层数 + 该层最大子树深度; 若子树为空, 最大子树深度为: -1
            depth = l + (max(subDepth) if subDepth else -1)
            ans.append(depth)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
