import bisect

question_content = """
Given an array of digits which is sorted in non-decreasing order. You can write 
numbers using each digits[i] as many times as we want. For example, if digits = 
['1','3','5'], we may write numbers such as '13', '551', and '1351315'. 

 Return the number of positive integers that can be generated that are less 
than or equal to a given integer n. 

 
 Example 1: 

 
Input: ["5","7","8"],59
Output: 6
 
Input: ["5","6"], 19
Output: 2
 
Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.


 Example 2: 


Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit 
numbers.
In total, this is 29523 integers that can be written using the digits array.
 

 Example 3: 

 
Input: digits = ["7"], n = 8
Output: 1
 
 
Input: digits = ["8"], n = 8
Output: 1
 
 
Input: digits = ["9"], n = 8
Output: 0
 

 
 Constraints: 

 
 1 <= digits.length <= 9 
 digits[i].length == 1 
 digits[i] is a digit from '1' to '9'. 
 All the values in digits are unique. 
 digits is sorted in non-decreasing order. 
 1 <= n <= 10⁹ 
 

 Related Topics 数组 数学 字符串 二分查找 动态规划 👍 180 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 输入数字
        arr = []
        while n > 0:
            arr.append(n % 10)
            n //= 10
        # print(arr)

        # 升序排列的可选数组
        choice_digits = []
        for i in range(len(digits)):
            d = int(digits[i])
            if not choice_digits or d != choice_digits[-1]:
                choice_digits.append(d)

        choice_digits = [int(tmp) for tmp in digits]

        # 递推
        dp = [1] + [0] * len(arr)

        ans = 0

        # for i in range(0, len(arr)):
        #     idx = bisect.bisect_right(choice_digits, arr[i])
        #     print(idx)
        #     no_zeor_leading = idx * (len(choice_digits))**i
        #     zeor_leading = dp[i]

        #     # dp[i] = idx * no_zeor_leading + zeor_leading if arr[i] in choice_digits else 0
        #     dp[i] = idx * (len(choice_digits))**i + dp[i] if arr[i] in choice_digits else 0

        #     cnt_anytail = (len(choice_digits))**i

        #     ans += dp[i] + zeor_leading

        for i in range(0, len(arr)):
            n_less = bisect.bisect_left(choice_digits, arr[i])
            n_equal = arr[i] in choice_digits

            # cnt_any = len(choice_digits)**(i+1)
            dp[i + 1] = n_less * len(choice_digits) ** (i) + n_equal * dp[i]
            # ans += dp[i+1]

        return dp[-1] + sum(len(choice_digits) ** i for i in range(1, len(arr)))

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        choice_digits = [int(tmp) for tmp in digits]

        # 输入数字
        arr = []
        startidx = -1
        for i in range(100):
            if n <= 0: break
            d = n % 10
            arr.append(d)
            n //= 10
            if d not in choice_digits:
                startidx = i

        # arr = [int(c) for c in str(n)]
        choice_digits = [int(tmp) for tmp in digits]

        # 递推
        dp = 1
        for i in range(startidx, len(arr)):
        # for i in range(0, len(arr)):
            arri = arr[i]
            n_less = bisect.bisect_left(choice_digits, arri)
            n_equal = arri in choice_digits
            dp = n_less * len(choice_digits) ** i + n_equal * dp

        return dp + sum(len(choice_digits) ** i for i in range(1, len(arr)))


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 输入数字
        arr = [int(c) for c in str(n)[::-1]]
        digits = [int(tmp) for tmp in digits]

        # 递推
        dp = 1
        for i in range(0, len(arr)):
            dp = bisect.bisect_left(digits, arr[i]) * len(digits) ** i + (arr[i] in digits) * dp

        return dp + sum(len(digits) ** i for i in range(1, len(arr)))

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 输入数字
        digits = [int(tmp) for tmp in digits]
        dset = set(digits)
        arr = [int(c) for c in str(n)[::-1]]

        # 递推
        dp = 1
        for i, arri in enumerate(arr):
            dp = bisect.bisect_left(digits, arri) * len(digits) ** i + (arri in dset) * dp

        return dp + sum(len(digits) ** i for i in range(1, len(arr)))

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """ dfs + 排列组合计算, 和数位dp思路很像 """
        digits = [int(tmp) for tmp in digits]

        def DFS(n, N):
            first_digit, left_n = n // (10 ** (N - 1)), n % (10 ** (N - 1))
            left_cnt = bisect.bisect_left(digits, first_digit) * len(digits) ** (N-1)

            if N == 0:
                return 1
            elif first_digit not in digits:
                return left_cnt
            else:
                return DFS(left_n, N - 1) + left_cnt

        N = len(str(n))
        return DFS(n, N) + sum(len(digits) ** i for i in range(1, N))

# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
