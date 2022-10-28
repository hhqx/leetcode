question_content = """
Given a string s, reverse the order of characters in each word within a 
sentence while still preserving whitespace and initial word order. 

 
Example 1: 
Input: s = "Let's take  LeetCode contest"
Output: "s'teL ekat  edoCteeL tsetnoc"
 
 Example 2: 
Input: s = "God Ding"
Output: "doG gniD"
 
 
 Constraints: 

 
 1 <= s.length <= 5 * 10⁴ 
 s contains printable ASCII characters. 
 s does not contain any leading or trailing spaces. 
 There is at least one word in s. 
 All the words in s are separated by a single space. 
 

 Related Topics 双指针 字符串 👍 484 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(i, j):
            nonlocal s
            def swap(i, j):
                # s[i], s[j] = s[j], s[i]
                # s[i] ^= s[j]
                # s[j] ^= s[i]
                # s[i] ^= s[j]
                tmp = s[i]
                s[i] = s[j]
                s[j] = s[i]
                s[i] = tmp

            # for k in range((j-i+1)//2):
                # swap(i+k, j-k)
            if i == 0:
                s = s[:i] + s[j::-1] + s[j + 1:]
            else:
                s = s[:i] + s[j:i - 1:-1] + s[j + 1:]
            # print(s)

        # def isSpace(i):
        #     if 0 <= i <= len(s) - 1:
        #         return s[i] == ' '
        #     else:
        #         return True

        start = 0 if s[0] != ' ' else -1
        for i in range(1, len(s)):
            if s[i - 1] == ' ' and s[i] != ' ':
                start = i
            elif s[i - 1] != ' ' and s[i] == ' ':
                reverse(start, i - 1)
        if s[len(s) - 1] != ' ':
            reverse(start, len(s) - 1)

        return s

    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split(' ')])
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
