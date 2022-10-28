
question_content = """
Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is 
included in the window. If there is no such substring, return the empty string "". 


 The testcases will be generated such that the answer is unique. 

 A substring is a contiguous sequence of characters within the string. 

 
 Example 1: 

 
Input: s = "aaflslflsldkalskaaa", t = "aaa"
Output: "aaa"
 
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' 
from string t.
 

 Example 2: 

 
Input: s = "ab", t = "a"
Output: "a" 

Input: s = "ab", t = "b"
Output: "b"
 
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
 
 Example 3: 
 
Input: s = "a", t = "aa"
Output: "" 
Input: s = "a", t = "aac"
Output: ""

Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

 
 Constraints: 

 
 m == s.length 
 n == t.length 
 1 <= m, n <= 10⁵ 
 s and t consist of uppercase and lowercase English letters. 
 

 
 Follow up: Could you find an algorithm that runs in O(m + n) time? 

 Related Topics 哈希表 字符串 滑动窗口 👍 2141 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """ 不考虑包含字符频率 """
        tdict = dict()
        for c in t:
            tdict[c] = 0

        minAns = [0, len(s)]
        left, right = 0, 0
        while right < len(s):
            while right < len(s) and sum([v != 0 for v in tdict.values()]) != len(tdict):
                if s[right] in tdict:
                    tdict[s[right]] += 1
                right += 1

            minAns = min(minAns, (left, right), key=lambda x: x[1] - x[0])
            while left < right < len(s):
                nonzeros_cnt = sum([v != 0 for v in tdict.values()])
                # print(tdict)
                # print(s[left:right])

                # 循环退出条件, 若当前删去当前字符会导致: tdict非零元素 < len(tdict) -2
                if nonzeros_cnt == len(tdict) - 1 and s[left] in tdict and tdict[s[left]] == 1:
                    break

                # t中字符计数
                if s[left] in tdict:
                    tdict[s[left]] -= 1
                left += 1

        if left == 0:
            if sum([v != 0 for v in tdict.values()]) != len(tdict):
                minAns = [0, 0]

        # ans = s[minAns[0]:minAns[1]] if  else ""
        ans = s[minAns[0]:minAns[1]]
        return ans

    def minWindow(self, s: str, t: str) -> str:
        """ ac版 """
        def hasContained(sdict, tdict):
            for k in tdict:
                if sdict[k] < tdict[k]:
                    return False
            return True
        from collections import defaultdict
        # 统计t中的词频
        tdict = defaultdict(int)
        for c in t:
            tdict[c] += 1

        # 统计s中的词频
        sdict = dict()
        for c in tdict:
            sdict[c] = 0

        minAns = [-1, len(s)]
        left, right = 0, 0
        while right < len(s):
            while right < len(s) and not hasContained(sdict=sdict, tdict=tdict):
                if s[right] in sdict:
                    sdict[s[right]] += 1
                right += 1

            while left < len(s):
                # nonzeros_cnt = sum([v != 0 for v in sdict.values()])
                # print(sdict)
                # print(tdict)
                # print(s[left:right])
                # print(left)

                if hasContained(sdict=sdict, tdict=tdict):
                    minAns = min(minAns, (left, right), key=lambda x: x[1] - x[0])

                # 循环退出条件, 若当前删去当前字符会导致: tdict 与 sdict 的字符总数差达到2
                if not hasContained(sdict=sdict, tdict=tdict) and s[left] in sdict:
                    break

                # t中字符计数
                if s[left] in sdict:
                    sdict[s[left]] -= 1
                left += 1

        if minAns[0] == -1:
            if not hasContained(sdict=sdict, tdict=tdict):
                minAns = [0, 0]
            # else:


        # ans = s[minAns[0]:minAns[1]] if  else ""
        ans = s[minAns[0]:minAns[1]]
        return ans

    def minWindow(self, s: str, t: str) -> str:
        """ ac版, 优化判断s子串是否包含t的代码段 """

        from collections import defaultdict
        # 统计t中的词频
        tdict = defaultdict(int)
        for c in t:
            tdict[c] += 1

        # 统计s中的词频
        sdict = dict()
        for c in tdict:
            sdict[c] = 0

        minAns = [-1, len(s)]
        left, right = 0, 0
        equal_sum = 0  # sdict 和 tdict 有多少个元素值相等, 即s子串和t有多少个字符词频相等
        while right < len(s):
            # 向右搜索至s首次包含t
            while right < len(s) and equal_sum != len(tdict):
                c = s[right]
                # sdict字符计数, 更新equal_sum
                if c in sdict:
                    sdict[c] += 1
                    if sdict[c] == tdict[c]:
                        equal_sum += 1
                right += 1

            # 向左删减值, 至tdict 与 sdict 的字符总数差达到2
            while left < len(s):
                c = s[left]

                # 若子串包含t, 更新最小子串结果
                if equal_sum == len(tdict):
                    minAns = min(minAns, (left, right), key=lambda x: x[1] - x[0])

                # 循环退出条件, 若当前删去当前字符会导致: tdict 与 sdict 的字符总数差达到2
                if equal_sum != len(tdict) and c in sdict and sdict[c] <= tdict[c]:
                    break

                # t中字符计数, 更新equal_sum
                if c in sdict:
                    if sdict[c] == tdict[c]:
                        equal_sum -= 1
                    sdict[c] -= 1
                left += 1

        # 若未找到最小串, 返回 ""
        if minAns[0] == -1:
            return ""

        ans = s[minAns[0]:minAns[1]]
        return ans

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """ ac版, 优化判断s子串是否包含t的代码段, + 优化空间 """

        from collections import defaultdict
        # 统计t中的词频
        sdict = defaultdict(int)
        for c in t:
            sdict[c] -= 1

        minAns = [-1, len(s)]
        left, right = 0, 0
        equal_sum = 0  # sdict 和 tdict 有多少个元素值相等, 即s子串和t有多少个字符词频相等
        while right < len(s):
            # 向右搜索至s首次包含t
            while right < len(s) and equal_sum != len(sdict):
                c = s[right]
                # sdict字符计数, 更新equal_sum
                if c in sdict:
                    sdict[c] += 1
                    if sdict[c] == 0:
                        equal_sum += 1
                right += 1

            # print(s[left:right])
            # 向左删减值, 至tdict 与 sdict 的字符总数差达到2
            while left < len(s):
                c = s[left]

                # 若子串包含t, 更新最小子串结果
                if equal_sum == len(sdict):
                    minAns = min(minAns, (left, right), key=lambda x: x[1] - x[0])

                # 循环退出条件, 若当前删去当前字符会导致: tdict 与 sdict 的字符总数差达到2
                if equal_sum != len(sdict) and c in sdict and sdict[c] <= 0:
                    break

                # t中字符计数, 更新equal_sum
                if c in sdict:
                    if sdict[c] == 0:
                        equal_sum -= 1
                    sdict[c] -= 1
                left += 1

        # 若未找到最小串, 返回 ""
        if minAns[0] == -1:
            return ""

        ans = s[minAns[0]:minAns[1]]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
