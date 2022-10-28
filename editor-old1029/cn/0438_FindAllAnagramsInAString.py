
question_content = """
Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order. 

 An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once. 

 
 Example 1: 

 
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
 

 Example 2: 

 
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

 
 Constraints: 

 
 1 <= s.length, p.length <= 3 * 10⁴ 
 s and p consist of lowercase English letters. 
 

 Related Topics 哈希表 字符串 滑动窗口 👍 1024 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """ 双指针法 """

        if len(s) < len(p):
            return []

        ans = []
        left, right = 0, 0
        fp = Counter(p)
        fs = defaultdict(int)
        equal_cnt = 0

        while right < len(s):
            # right右移扩展窗口长度到len(p)
            while right - left < len(p):
                fs[s[right]] += 1
                if fs[s[right]] == fp[s[right]]:
                    equal_cnt += 1
                    if equal_cnt == len(fp):
                        ans.append(left)
                right += 1

            # left右移1格
            if fs[s[left]] == fp[s[left]]:
                equal_cnt -= 1
            fs[s[left]] -= 1
            left += 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
