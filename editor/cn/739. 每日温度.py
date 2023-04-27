question_content = """
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几
天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。 

 

 示例 1: 

 
输入: temperatures = [73,74,75,71,69,72,76,73]
输出:[1,1,4,2,1,1,0,0]
 

 示例 2: 

 
输入: temperatures = [30,40,50,60]
输出:[1,1,1,0]
 

 示例 3: 

 
输入: temperatures = [30,60,90]
输出: [1,1,0] 

 

 提示： 

 
 1 <= temperatures.length <= 10⁵ 
 30 <= temperatures[i] <= 100 
 

 Related Topics 栈 数组 单调栈 👍 1464 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        R = [n] * n
        st = []
        for i, num in enumerate(temperatures):
            while st and num > temperatures[st[-1]]:
                idx = st.pop()
                R[idx] = i
            st.append(i)
        ans = [x - i if x != n else 0 for i, x in enumerate(R)]
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
