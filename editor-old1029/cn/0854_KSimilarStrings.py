from collections import deque

question_content = """
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can 
swap the positions of two letters in s1 exactly k times so that the resulting 
string equals s2. 

 Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-
similar. 

 
 Example 1: 

 
Input: s1 = "ab", s2 = "ba"
Output: 1
 

 Example 2: 

 
Input: s1 = "abc", s2 = "bca"
Output: 2
 

 
 Constraints: 

 
 1 <= s1.length <= 20 
 s2.length == s1.length 
 s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e',
 'f'}. 
 s2 is an anagram of s1. 
 

 Related Topics 广度优先搜索 字符串 👍 185 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """ 广度优先搜索 """
    def kSimilarity(self, s1: str, s2: str) -> int:
        def next(s):
            i = 0
            while s[i] == s2[i]:
                i += 1
            res = []
            for j in range(i + 1, n):
                if s[j] == s2[i] and s[j] != s2[j]:
                    res.append(s2[: i + 1] + s[i + 1 : j] + s[i] + s[j + 1 :])
            return res

        q = deque([s1])
        vis = {s1}
        ans, n = 0, len(s1)
        while 1:
            for _ in range(len(q)):
                s = q.popleft()
                if s == s2:
                    return ans
                for nxt in next(s):
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)
            ans += 1

class Solution:
    """ 深度优先搜索 """
    def kSimilarity(self, s1: str, s2: str) -> int:
        s, t = [], []
        for x, y in zip(s1, s2):
            if x != y:
                s.append(x)
                t.append(y)
        n = len(s)
        if n == 0:
            return 0

        ans = n - 1
        def dfs(i: int, cost: int) -> None:
            nonlocal ans
            if cost > ans:
                return
            while i < n and s[i] == t[i]:
                i += 1
            if i == n:
                ans = min(ans, cost)
                return
            diff = sum(s[j] != t[j] for j in range(i, len(s)))
            min_swap = (diff + 1) // 2
            if cost + min_swap >= ans:  # 当前状态的交换次数下限大于等于当前的最小交换次数
                return
            for j in range(i + 1, n):
                if s[j] == t[i]:
                    s[i], s[j] = s[j], s[i]
                    dfs(i + 1, cost + 1)
                    s[i], s[j] = s[j], s[i]
        dfs(0, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
