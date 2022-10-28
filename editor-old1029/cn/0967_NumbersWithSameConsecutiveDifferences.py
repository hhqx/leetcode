
question_content = """
Return all non-negative integers of length n such that the absolute difference 
between every two consecutive digits is k. 

 Note that every number in the answer must not have leading zeros. For example, 
01 has one leading zero and is invalid. 

 You may return the answer in any order. 

 
 Example 1: 

 
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

 

 Example 2: 

 
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

 
 Constraints: 

 
 2 <= n <= 9 
 0 <= k <= 9 
 

 Related Topics 广度优先搜索 回溯 👍 82 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def getDigits(n, delta):
            if delta == 0:
                return [n]
            out = []
            if n - delta >= 0:
                out.append(n - delta)
            if n + delta < 10:
                out.append(n + delta)
            return out
        # print(getDigits(2, 2))

        start = [i+1 for i in range(9)]
        nowNums = start
        nextNums = []
        for delta in range(n - 1):
            for num in nowNums:
                digits = getDigits(num % 10, k)
                nextNums += [num * 10 + d for d in digits]
            nowNums = nextNums
            nextNums = []
        return nowNums
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
