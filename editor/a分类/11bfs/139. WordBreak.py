question_content = """
Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words. 

 Note that the same word in the dictionary may be reused multiple times in the 
segmentation. 

 
 Example 1: 

 
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
 

 Example 2: 

 
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen 
apple".
Note that you are allowed to reuse a dictionary word.
 

 Example 3: 

 
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

 
 Constraints: 

 
 1 <= s.length <= 300 
 1 <= wordDict.length <= 1000 
 1 <= wordDict[i].length <= 20 
 s and wordDict[i] consist of only lowercase English letters. 
 All the strings of wordDict are unique. 
 

 Related Topics 字典树 记忆化搜索 数组 哈希表 字符串 动态规划 👍 2103 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ bfs + 暴力匹配, o(n*n*m) """
        q = deque([0])
        vis = {0}
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == len(s):
                    return True
                for word in wordDict:
                    if cur + len(word) > len(s) or s[cur: cur + len(word)] != word:
                        continue
                    nxt = cur + len(word)
                    vis.add(nxt)
                    q.append(nxt)

        return False


class Trie:
    def __init__(self):
        self.child = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.child[c]
        cur.word = word

    def query(self, s):
        cur = self
        ret = []
        for i, c in enumerate(s):
            if c not in cur.child:
                break
            cur = cur.child[c]
            if cur.word:
                ret.append(i + 1)
        return ret


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ bfs + Trie """
        obj = Trie()
        for word in wordDict:
            obj.insert(word)

        q = deque([0])
        vis = {0}
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == len(s):
                    return True
                for res in obj.query(s[cur:]):
                    nxt = cur + res
                    if nxt in vis:
                        continue
                    vis.add(nxt)
                    q.append(nxt)

        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ dp, o(n*n) """
        wordDict = set(wordDict)

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if dp[i]:
                continue
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = 1

        # print(dp)
        return dp[-1] != 0


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ dp, Trie """
        obj = Trie()
        for word in wordDict:
            obj.insert(word)

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(0, len(s)):
            if not dp[i]:
                continue
            for delta in obj.query(s[i:]):
                dp[i + delta] = True
                if i + delta == len(s):
                    return True

        # print(dp)
        return False


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
