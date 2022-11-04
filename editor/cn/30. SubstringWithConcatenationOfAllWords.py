
question_content = """
You are given a string s and an array of strings words. All the strings of 
words are of the same length. 

 A concatenated substring in s is a substring that contains all the strings of 
any permutation of words concatenated. 

 
 For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", 
"cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a 
concatenated substring because it is not the concatenation of any permutation of 
words. 
 

 Return the starting indices of all the concatenated substrings in s. You can 
return the answer in any order. 

测试用例:"bcabbcaabbccacacbabccacaababcbb"
        ["c","b","a","c","a","a","a","b","c"]
测试结果:[]
期望结果:[6,16,17,18,19,20]

输入：
"wordgoodgoodgoodbestword"
["word","good","best","good"]

输出：
[8]

 
 Example 1: 

 
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated 
substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar",
"foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo",
"bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
 

 Example 2: 

 
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated 
substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of 
any permutation of words.
We return an empty array.
 

 Example 3: 

 
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated 
substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo",
"bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar",
"the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the",
"foo","bar"] which is a permutation of words.
 

 
 Constraints: 

 
 1 <= s.length <= 10⁴ 
 1 <= words.length <= 5000 
 1 <= words[i].length <= 30 
 s and words[i] consist of lowercase English letters. 
 

 Related Topics 哈希表 字符串 滑动窗口 👍 842 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        因为 words[i] 的长度均相同, 所以可以根据 words[i] 的长度来划分 s 字符串.

        1. 把 s 划分为长度为 words[i] 的连续子串, 根据起始偏移不同, 共有 words[i] 种划分方式

        2. 对于每种划分方式, 用双指针法, 统计该划分下长度为 len(words) 的子串词频和 words 相等的所有情况.

        3. 字符串 s 中与 words 完全相等词频的子串  是  字符串 s 中完全包含 words 词频的子串  的一个子集.

        """
        nw = len(words[0])
        n = len(s)
        dfreq = Counter(words)

        ans = []

        for start in range(nw):
            # 计算 [start, len(s)) 里面有多少组长度为 nw 的字符串
            nwords = (n - start) // nw

            # 双指针(可以看成是双端队列)统计窗口 [left, right] 的词频
            d = defaultdict(int)
            cnt = 0
            left = 0
            for right in range(nwords):
                # 添加字符进入窗口
                rword = s[start + right * nw: start + right * nw + nw]
                if rword in dfreq:
                    d[rword] += 1
                    if d[rword] == dfreq[rword]:
                        cnt += 1

                # 字符出队直至不满足条件
                while left <= right and cnt == len(dfreq):
                    # 划重点, 本题情况要求窗口内的词频和查询词的词频完全相等, 不是仅包含的关系
                    # 词频完全相等 <=> 窗口词频包含查询词频 && 窗口长度==查询长度
                    if cnt == len(dfreq) and right - left + 1 == len(words):  # 如果满足条件, 记录该结果
                        # 添加字符串起点, 计算方式为: 终点 - 长度
                        ans.append(start + right * nw + nw - nw * len(words))

                    lword = s[start + left * nw: start + left * nw + nw]
                    if lword in dfreq:
                        d[lword] -= 1
                        if d[lword] == dfreq[lword] - 1:
                            cnt -= 1
                    left += 1

        return ans


class Solution1:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        因为 words[i] 的长度均相同, 所以可以根据 words[i] 的长度来划分 s 字符串.

        1. 把 s 划分为长度为 words[i] 的连续子串, 根据起始偏移不同, 共有 words[i] 种划分方式

        2. 对于每种划分方式, 用双指针法, 统计该划分下长度为 len(words) 的子串词频和 words 相等的所有情况.

        """
        nw = len(words[0])
        n = len(s)
        dfreq = Counter(words)

        ans = []

        def isEqual(d1, d2):
            for k, v in d1.items():
                if v != d2[k]:
                    return False
            return True

        for start in range(nw):
            # 计算 [start, len(s)) 里面有多少组长度为 nw 的字符串
            nwords = (n - start) // nw

            # 双指针(可以看成是双端队列)统计窗口 [left, right] 的词频
            d = defaultdict(int)
            # 此题中, cnt 在词频跳变沿出变换, 复制记录词频相等的字符数
            cnt = 0
            left = 0
            for right in range(nwords):
                # 添加字符进入窗口
                rword = s[start + right * nw: start + right * nw + nw]
                if rword in dfreq:
                    d[rword] += 1
                    if d[rword] == dfreq[rword]:
                        cnt += 1

                # 字符出队直至不满足条件, 在这里实际上是为了移动 left 保持窗口长度为 nw
                while left < right + 1 - len(words):
                    lword = s[start + left * nw: start + left * nw + nw]
                    if lword in dfreq:
                        d[lword] -= 1
                        if d[lword] == dfreq[lword]-1:
                            cnt -= 1
                    left += 1

                # cnt 在这里只是为了先过滤一下, 避免字典 d 频繁比较,
                # 后面发现原来是 cnt 的更新方式错了, 原来的方法没错, 小丑竟是我自己
                if cnt == len(dfreq) and isEqual(dfreq, d):
                # if isEqual(dfreq, d):
                    # print(cnt, len(dfreq))
                    ans.append(start + right * nw + nw - nw * len(words))

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
