
question_content = """
给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 
。 

 

 示例 1: 

 
输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
 

 示例 2: 

 
输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
 

 示例 3: 

 
输入: intervals = [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
 

 

 提示: 

 
 1 <= intervals.length <= 10⁵ 
 intervals[i].length == 2 
 -5 * 10⁴ <= starti < endi <= 5 * 10⁴ 
 

 Related Topics 贪心 数组 动态规划 排序 👍 949 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """ 贪心法 """
        intervals.sort(key=lambda x: x[1])
        coverd = -inf
        selected = 0
        for l, r in intervals:
            if l >= coverd:
                coverd = r
                selected += 1

        return len(intervals) - selected

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
