from collections import defaultdict

question_content = """


输入：path = [[0,1],[0,3],[1,3],[2,0],[2,3]]
输出：3


输入：path = [[0,3],[1,0],[1,3],[2,0],[3,0],[3,2]]
输出：-1


"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
        node = defaultdict(lambda : [0, 0])
        for i, o in path:
            node[i][0] += 1
            node[o][1] += 1

        ans = -1
        nodeNum = len(node)
        for k, (o, i) in node.items():
            if i == nodeNum-1 and o == 0:
                ans = k
                break
        return ans

# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
