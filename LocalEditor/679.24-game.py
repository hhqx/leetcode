#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 Game
#
# https://leetcode.cn/problems/24-game/description/
#
# algorithms
# Hard (53.88%)
# Likes:    400
# Dislikes: 0
# Total Accepted:    36.3K
# Total Submissions: 67.3K
#

question_content="""You are given an integer array cards of length 4. You have four cards, each
containing a number in the range [1, 9]. You should arrange the numbers on
these cards in a mathematical expression using the operators ['+', '-', '*',
'/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:


The division operator '/' represents real division, not integer
division.


For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.


Every operation done is between two numbers. In particular, we cannot use '-'
as a unary operator.

For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not
allowed.


You cannot concatenate numbers together

For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not
valid.




Return true if you can get such expression that evaluates to 24, and false
otherwise.


Example 1:


Input: cards = [4,1,8,7]
Output: True
Explanation: (8-4) * (7-1) = 24


Example 2:


Input: cards = [1,2,1,2]
Output: False



Constraints:


cards.length == 4
1 <= cards[i] <= 9


"""

from typing import *
from RunLeetCodeInPycharm import StartTest

# @lc code=start
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def combine(arr, k):
            results = []
            path = []
            def dfs(startIndex):
                if len(path) == k:
                    results.append(path[:])
                    return
                for i in range(startIndex, len(arr)):
                    path.append(i)
                    dfs(i+1)
                    path.pop()

            dfs(0)
            selected = [[a for i, a in enumerate(arr) if i in idx] for idx in results]
            others = [[a for i, a in enumerate(arr) if i not in idx] for idx in results]
            # others = []
            # print(results)
            # print(selected)
            # print(others)
            return zip(selected, others)
        
        # combine([1,2,3], 2)
        op_dict = {
            'add': lambda x, y: x + y, 'subs': lambda x, y: x - y, 'subs_r': lambda x, y: y - x,
            'multi': lambda x, y: x * y, 'minis': lambda x, y: x / y, 'minis_r': lambda x, y: y / x
        }
        isSuccess = False
        def dfs(arr):
            nonlocal isSuccess
            if len(arr) == 1:
                if abs(arr[0] - 24) < 1e-5:
                    isSuccess = True
                return  
            
            for selected, others in combine(arr, 2):
                for name, op in op_dict.items():
                    if name == 'minis' and selected[1] == 0:
                        continue
                    elif name == 'minis_r' and selected[0] == 0:
                        continue
                    val = op(selected[0], selected[1])
                    dfs([val] + others)
                    if isSuccess:
                        return
        dfs(cards)
        return isSuccess
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()




