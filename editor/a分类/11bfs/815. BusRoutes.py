question_content = """
You are given an array routes representing bus routes where routes[i] is a bus 
route that the iᵗʰ bus repeats forever. 

 
 For example, if routes[0] = [1, 5, 7], this means that the 0ᵗʰ bus travels in 
the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever. 
 

 You will start at the bus stop source (You are not on any bus initially), and 
you want to go to the bus stop target. You can travel between bus stops by buses 
only. 

 Return the least number of buses you must take to travel from source to target.
 Return -1 if it is not possible. 

 
 Example 1: 

 
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then 
take the second bus to the bus stop 6.
 

 Example 2: 

 
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 1
2
Output: -1
 

 
 Constraints: 

 
 1 <= routes.length <= 500. 
 1 <= routes[i].length <= 10⁵ 
 All the values of routes[i] are unique. 
 sum(routes[i].length) <= 10⁵ 
 0 <= routes[i][j] < 10⁶ 
 0 <= source, target < 10⁶ 
 

 Related Topics 广度优先搜索 数组 哈希表 👍 339 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
