
question_content = """
Let's define a function countUniqueChars(s) that returns the number of unique 
characters on s. 

 
 For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", 
"O", "D" are the unique characters since they appear only once in s, therefore 
countUniqueChars(s) = 5. 
 

 Given a string s, return the sum of countUniqueChars(t) where t is a substring 
of s. The test cases are generated such that the answer fits in a 32-bit 
integer. 

 Notice that some substrings can be repeated so in this case you have to count 
the repeated ones too. 

 
 Example 1: 

 
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
 

 Example 2: 

 
Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
 

 Example 3: 

 
Input: s = "LEETCODE"
Output: 92
 

 
 Constraints: 

 
 1 <= s.length <= 10⁵ 
 s consists of uppercase English letters only. 
 

 Related Topics 哈希表 字符串 动态规划 👍 212 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
            对于字符cj, 当它在某个子字符串中仅出现一次时，它会对这个子字符串统计唯一字符时有贡献。只需对每个字符，计算有多少子字符串仅包含该字符一次即可。
            对于字符cj, 其上一次出现位置为ci, 下一次为ck, 则共有 sum((cj-ci)*(ck-cj)) 个子串会仅包含它一次.
        """
        from collections import defaultdict
        d = defaultdict(list)
        ans = 0
        for i, c in enumerate(s):
            d[c].append(i)

        for idxs in d.values():
            idxs = [-1] + idxs + [len(s)]
            for i in range(1, len(idxs) - 1):
                ans += (idxs[i] - idxs[i - 1]) * (idxs[i + 1] - idxs[i])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
