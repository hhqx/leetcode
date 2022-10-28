
question_content = """
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and 
lefti < righti. 

 A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can 
be formed in this fashion. 

 Return the length longest chain which can be formed. 

 You do not need to use up all the given intervals. You can select pairs in any 
order. 

 
 Example 1: 

 
Input: pairs = [[3,4], [2,3], [1,2]]
Output: 2
 
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
 

 Example 2: 

 
Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

 
 Constraints: 

 
 n == pairs.length 
 1 <= n <= 1000 
 -1000 <= lefti < righti <= 1000 
 

 Related Topics 贪心 数组 动态规划 排序 👍 295 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """ 贪心策略，和单处理器调度的最早截止时间算法(EDF)原理一致, 都是在一个区间范围内尽可能的多容纳区间个数 """
        pairs.sort(key=lambda x: x[1])
        # print(pairs)
        L = 1
        start = pairs[0][1]
        for p in pairs[1:]:
            if p[0] > start:
                start = p[1]
                L += 1
        return L

# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
