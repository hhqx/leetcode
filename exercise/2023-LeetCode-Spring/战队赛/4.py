question_content = """
4. 生物进化录
通过的用户数76
尝试过的用户数116
用户总通过次数76
用户总提交次数175
题目难度Hard
在永恒之森中，存在着一本生物进化录，以 一个树形结构 记载了所有生物的演化过程。经过观察并整理了各节点间的关系，parents[i] 表示编号 i 节点的父节点编号(根节点的父节点为 -1)。

为了探索和记录其中的演化规律，队伍中的炼金术师提出了一种方法，可以以字符串的形式将其复刻下来，规则如下：

初始只有一个根节点，表示演化的起点，依次记录 01 字符串中的字符，
如果记录 0，则在当前节点下添加一个子节点，并将指针指向新添加的子节点；
如果记录 1，则将指针回退到当前节点的父节点处。
现在需要应用上述的记录方法，复刻下它的演化过程。请返回能够复刻演化过程的字符串中， 字典序最小 的 01 字符串。

注意：

节点指针最终可以停在任何节点上，不一定要回到根节点。
示例 1：

输入：parents = [-1,0,0,2]

输出："00110"

解释：树结构如下图所示，共存在 2 种记录方案：
第 1 种方案为：0(记录编号 1 的节点) -> 1(回退至节点 0) -> 0(记录编号 2 的节点) -> 0((记录编号 3 的节点))
第 2 种方案为：0(记录编号 2 的节点) -> 0(记录编号 3 的节点) -> 1(回退至节点 2) -> 1(回退至节点 0) -> 0(记录编号 1 的节点)
返回字典序更小的 "00110"
image.png进化 (3).gif

示例 2：
输入：parents = [-1]

输出：""

输入：parents = [-1,0,0,1,2,2]

输出："00101100"

输入：
[-1,0,1,0,3,1,5,1,4,1,2,0,0,11,5,4,4,6,16,2]
输出：
"0000110101110000110110010110101100110"

提示：

1 <= parents.length <= 10^4
-1 <= parents[i] < i (即父节点编号小于子节点)
"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evolutionaryRecord(self, parents: List[int]) -> str:
        n = len(parents)
        g = [[] for _ in range(n)]
        for i, par in enumerate(parents):
            if i == 0:
                continue
            g[par].append(i)
        if n == 1: return ""

        depth = [0] * n
        max_cnt = [0] * n
        def dfs_collect(u):
            if not g[u]:
                # 叶子节点
                return 0, 0
            r = 0
            c = 0
            for v in g[u]:
                dep, cnt = dfs_collect(v)
                r = max(r, dep+1)
                c = max(c, cnt)

            depth[u] = r
            if r == 1:
                c = len(g[u])
            max_cnt[u] = c
            return r, c

        dfs_collect(0)
        # print(depth)

        # sort
        for u in range(n):
            g[u].sort(key=lambda u: (-depth[u], -max_cnt[u]))

        # get result
        result = []
        def dfs(u):
            result.append("0")
            for v in g[u]:
                dfs(v)
            result.append("1")

        dfs(0)
        while result and result[-1] == '1':
            result.pop()
        ans = "".join(result[1:])
        return ans

class Solution:
    def evolutionaryRecord(self, parents: List[int]) -> str:
        n = len(parents)
        g = [[] for _ in range(n)]
        for i, par in enumerate(parents):
            if i == 0:
                continue
            g[par].append(i)
        if n == 1: return ""

        # get result
        def dfs(u):
            if not g[u]:
                # 叶子节点
                return "01"
            r = []
            for v in g[u]:
                r.append(dfs(v))
            ret = "0{}1".format("".join(sorted(r)))
            return ret
        result = list(dfs(0))
        while result and result[-1] == '1':
            result.pop()
        ans = "".join(result[1:])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
