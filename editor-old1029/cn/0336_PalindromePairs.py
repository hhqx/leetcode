question_content = """
Given a list of unique words, return all the pairs of the distinct indices (i, 
j) in the given list, so that the concatenation of the two words words[i] + 
words[j] is a palindrome. 

 
 Example 1: 

 
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
 

 Example 2: 

 
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
 

 Example 3: 

 
Input: words = ["a",""]
Output: [[0,1],[1,0]]
 

 
 Constraints: 

 
 1 <= words.length <= 5000 
 0 <= words[i].length <= 300 
 words[i] consists of lower-case English letters. 
 

 Related Topics 字典树 数组 哈希表 字符串 👍 337 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(string):
            # if not string:
            #     return False
            for i in range(len(string) // 2):
                if string[i] != string[len(string) - 1 - i]:
                    return False
            return True

        d = {w[::-1]: i for i, w in enumerate(words)}

        result = []
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                prefix, suffix = words[i][:j], words[i][j:]
                if j and isPalindrome(prefix):
                    if suffix in d:
                        if d[suffix] != i:
                            result.append([d[suffix], i])

                if isPalindrome(suffix):
                    if prefix in d:
                        if d[prefix] != i:
                            result.append([i, d[prefix]])

        return result


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
