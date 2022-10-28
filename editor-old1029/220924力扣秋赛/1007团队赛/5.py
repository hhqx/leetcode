
question_content = """
5. 沙地治理
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Hard
在力扣城的沙漠分会场展示了一种沙柳树，这种沙柳树能够将沙地转化为坚实的绿地。
展示的区域为正三角形，这片区域可以拆分为若干个子区域，每个子区域都是边长为 1 的小三角形，其中第 i 行有 2i - 1 个小三角形。

初始情况下，区域中的所有位置都为沙地，你需要指定一些子区域种植沙柳树成为绿地，以达到转化整片区域为绿地的最终目的，规则如下：

若两个子区域共用一条边，则视为相邻；
如下图所示，(1,1)和(2,2)相邻，(3,2)和(3,3)相邻；(2,2)和(3,3)不相邻，因为它们没有共用边。

若至少有两片绿地与同一片沙地相邻，则这片沙地也会转化为绿地
转化为绿地的区域会影响其相邻的沙地
image.png
现要将一片边长为 size 的沙地全部转化为绿地，请找到任意一种初始指定 最少 数量子区域种植沙柳的方案，并返回所有初始种植沙柳树的绿地坐标。

示例 1：

输入：size = 3
输出：[[1,1],[2,1],[2,3],[3,1],[3,5]]
解释：如下图所示，一种方案为：
指定所示的 5 个子区域为绿地。
相邻至少两片绿地的 (2,2)，(3,2) 和 (3,4) 演变为绿地。
相邻两片绿地的 (3,3) 演变为绿地。
image.png

示例 2：

输入：size = 2
输出：[[1,1],[2,1],[2,3]]
解释：如下图所示：
指定所示的 3 个子区域为绿地。
相邻三片绿地的 (2,2) 演变为绿地。
image.png


输入：size = 4
输出：[[1,1],[2,1],[2,3],[3,1],[3,5]]

输入：size = 5
输出：[[1,1],[2,1],[2,3],[3,1],[3,5]]

提示：

1 <= size <= 1000



"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sandyLandManagement(self, size: int) -> List[List[int]]:
        n = size
        ans = []
        for i in range(n):
            ans.append([i+1, 1])
        for i in range(n-1):
            ans.append([n, i*2+3])

        for Len in range(n-3):
            # p = []
            # print(Len)
            for j in range(Len+1):
                p = [j+3, 2*j+4]
                ans.append(p)

        # ans.sort()
        return ans

# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
