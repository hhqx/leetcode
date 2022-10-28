
question_content = """
输入：
temperatureA = [21,18,18,18,31],
temperatureB = [34,32,16,16,17]

输出：2

输入：
temperatureA = [5,10,16,-6,15,11,3],
temperatureB = [16,22,23,23,25,3,-16]
输出：3



输入：
temperatureA = [24,23,14,21,26,-20,-9,12,-9,-2],
temperatureB = [39,-2,32,29,24,27,16,14,22,10]
输出：1



"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        def getTrend(d1, d2):
            if d1 > d2:
                return 0
            elif d1 == d2:
                return 1
            elif d1 < d2:
                return 2

        ans = 0
        start = -1
        for i in range(len(temperatureA)-1):
            if getTrend(temperatureA[i], temperatureA[i+1]) == getTrend(temperatureB[i], temperatureB[i+1]):
                ans = max(ans, i-start)
            else:
                start = i

        return ans

# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
