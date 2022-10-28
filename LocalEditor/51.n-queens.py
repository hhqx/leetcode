#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.cn/problems/n-queens/description/
#
# algorithms
# Hard (74.12%)
# Likes:    1505
# Dislikes: 0
# Total Accepted:    251.1K
# Total Submissions: 338.7K
# Testcase Example:  '4'
#

question_content="""The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You
may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space,
respectively.


Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as
shown above


Example 2:


Input: n = 1
Output: [["Q"]]



Constraints:


1 <= n <= 9


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def convertToString(row):
            string = [['.'] * n for i in range(n)]
            for i, j in enumerate(row):
                string[i][j] = 'Q'
            return [''.join(row) for row in string]

        result = []
        path = []
        isUsed = [False] * n
        def dfs(startIndex):
            if startIndex == n:
                result.append(path[:])
                return
            
            for i in range(0, n):
                if isUsed[i]:
                    continue
                
                isContinue = False
                for idx, ii in enumerate(path):
                    if abs(startIndex-idx) == abs(i-ii):
                        isContinue = True
                        break
                if isContinue:
                    continue

                isUsed[i] = True
                path.append(i)
                dfs(startIndex + 1)
                path.pop()
                isUsed[i] = False
            
        dfs(0)
        # print(len(result))
            
        return [convertToString(row) for row in result]
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

