import bisect

question_content = """
An integer x is a good if after rotating each digit individually by 180 degrees,
 we get a valid number that is different from x. Each digit must be rotated - 
we cannot choose to leave it alone. 

 A number is valid if each digit remains a digit after rotation. For example: 

 
 0, 1, and 8 rotate to themselves, 
 2 and 5 rotate to each other (in this case they are rotated in a different 
direction, in other words, 2 or 5 gets mirrored), 
 6 and 9 rotate to each other, and 
 the rest of the numbers do not rotate to any other number and become invalid. 
 

 Given an integer n, return the number of good integers in the range [1, n]. 

 
 Example 1: 

 
Input: n = 10987654321
Output: 321691283
 
Input: n = 747757575
Output: 28810883
 
# Input: n = 747
# Output: 227
 
Input: n = 857
Output: 247
 
Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after 
rotating.
 

 Example 2: 


Input: n = 1
Output: 0


 Example 3: 


Input: n = 2
Output: 1
 

 
 Constraints: 

 
 1 <= n <= 10⁴ 
 

 Related Topics 数学 动态规划 👍 152 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    """ dfs回溯选出符合题意的数字(模拟法), 除此之外还可以用组合直接算一部分 """

    def rotatedDigits(self, n: int) -> int:
        digit_rotate = [2, 5, 6, 9]
        digit_nochang = [0, 1, 8]

        # n = 2

        table = digit_rotate + digit_nochang
        table.sort()
        isRotate = [(n in digit_rotate) for n in table]

        # n = 123
        # n = 10
        N = len(str(n))
        # result = []
        # ans = set()
        cnt = 0

        def dfs(i, sum, rotate_cnt=0):
            nonlocal cnt
            if i == N:
                if sum <= n and rotate_cnt > 0:
                    # result.append(sum)
                    # ans.add(sum)
                    cnt += 1
                return

            for j in range(len(table)):
                digit = table[j]
                # dfs(i + 1, sum * 10 + digit, rotate_cnt + isRotate[j])
                sum_next = sum + digit * (10 ** (N - 1 - i))
                if sum_next > n:
                    continue
                dfs(i + 1, sum_next, rotate_cnt + isRotate[j])

        dfs(0, 0)
        # print(ans)
        # print(result)

        # print(cnt)

        return cnt


class Solution:
    """ 排列组合 + 递归 """

    def rotatedDigits(self, n: int) -> int:
        digit_must = [2, 5, 6, 9]
        digit_optional = [0, 1, 8]
        digit_all = [0, 1, 2, 5, 6, 8, 9]

        """ 尝试一个方法直接用排列组合算 """

        def DFS(n, N, hasrotate=False):

            first_digit, left_n = n // (10 ** (N - 1)), n % (10 ** (N - 1))
            N_must = bisect.bisect_right(digit_must, first_digit - 1)
            N_optional = bisect.bisect_right(digit_optional, first_digit - 1)

            if not hasrotate:
                left_cnt = (N_must + N_optional) * len(digit_all) ** (N - 1) - N_optional * len(digit_optional) ** (
                            N - 1)
            else:
                left_cnt = (N_must + N_optional) * len(digit_all) ** (N - 1)

            if N == 0:
                return int(hasrotate)
            elif first_digit not in digit_all:
                return left_cnt
            else:
                return DFS(left_n, N - 1,
                           hasrotate or (first_digit in digit_must)) + left_cnt

        return DFS(n, len(str(n)))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
