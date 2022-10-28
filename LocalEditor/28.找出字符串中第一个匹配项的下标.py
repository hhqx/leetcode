#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Medium (41.65%)
# Likes:    1623
# Dislikes: 0
# Total Accepted:    755K
# Total Submissions: 1.8M
# Testcase Example:  '"sadbutsad"\n"sad"'
#

question_content = """给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。



示例 1：

输入：haystack = "adcadcaddcadde", needle = "adcadde"
输出：-1


输入：haystack = "aabaafaabaab", needle = "aabaab"
输出：6
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。


# 示例 2：


输入：haystack = "leeleetcode", needle = "leetco"
输出：3
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。




提示：


1 <= haystack.length, needle.length <= 10^4
haystack 和 needle 仅由小写英文字符组成


"""

from typing import *
from PythonLeetcodeRunner import *


def get_func(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(arg.__class__.__name__, arg, '\t', end='')
        print('\n')
        return

    return wrapper


dprint = get_func(print)

def getnext(q):
    next = [-1] * len(q)
    j = -1
    next[1] = 0
    for i in range(1, len(q)):
        while j >= 0 and q[j] != q[i-1]:
            j = next[j]
        j += 1
        next[i] = j
    return next
# next = getnext("aabaa")
# print(next)
# def getnext(q):
#     next = [-1] * len(q)
#     for i in range(1, len(q)):

def getnext(q):
    next = [-1] * len(q)
    j = -1
    next[0] = j
    for i in range(1, len(q)):
        while j >= 0 and q[j+1] != q[i]:
            j = next[j]
        if q[j+1] == q[i]:
            j += 1
        next[i] = j
    return next
next = getnext('abc'*5)
print(next)

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP算法

        # 计算next数组, 求解最长相同前后缀
        s = needle
        next = [0] * len(s)
        j = 0
        for i in range(1, len(next)):
            while j >= 0 and s[j] != s[i]:
                j -= 1
            next[i] = j + 1
            j += 1
        # return next
        # dprint(next)
        next = [-1] + next

        def getnext(q):
            next = [-1] * len(q)
            j = -1
            for i in range(1, len(q)):
                while j >= 0 and q[j] != q[i-1]:
                    j = next[j]
                j += 1
                next[i] = j
            return next
        next = getnext(needle)

        # KMP算法进行匹配
        j = 0
        for i in range(0, len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j]
            if j == -1 or haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1

        return -1



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        i = j = 0
        next = self.getnext(a, needle)

        while (i < b and j < a):
            if j == -1 or needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == a:
            return i - j
        else:
            return -1

    def getnext(self, a, needle):
        next = ['' for i in range(a)]
        j, k = 0, -1
        next[0] = k
        while (j < a - 1):
            if k == -1 or needle[k] == needle[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP算法

        # 计算next数组, 求解最长相同前后缀
        def getnext(q):
            next = [-1] * len(q)
            j = -1
            next[0] = j
            for i in range(1, len(q)):
                while j >= 0 and q[j + 1] != q[i]:
                    j = next[j]
                if q[j + 1] == q[i]:
                    j += 1
                next[i] = j
            return next
        next = getnext(needle)

        # KMP算法进行匹配
        j = -1
        for i in range(0, len(haystack)):
            while j >= 0 and haystack[i] != needle[j+1]:  # 直到字符匹配上为止, 或者已经回退到第一个字符
                j = next[j]
            if haystack[i] == needle[j+1]:  # 若当前字符匹配, 则右移两个指针
                j += 1
            if j+1 == len(needle):  # 若所有字符均已匹配完毕
                return i - len(needle) + 1

        return -1

# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
