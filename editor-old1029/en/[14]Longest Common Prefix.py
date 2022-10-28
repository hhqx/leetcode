
question_content = """
Write a function to find the longest common prefix string amongst an array of 
strings. 

 If there is no common prefix, return an empty string "". 

 
 Example 1: 

 
Input: strs = ["flower","flow","flight"]
Output: "fl"
 

 Example 2: 

 
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Input: strs = ["","b"]
Output: ""
 
 Constraints: 

 
 1 <= strs.length <= 200 
 0 <= strs[i].length <= 200 
 strs[i] consists of only lowercase English letters. 
 

 Related Topics String 👍 9831 👎 3306

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minLen = len(strs[0])
        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
        if minLen == 0:
            return ""

        for i in range(minLen):
            ch = strs[0][i]
            for j, s in enumerate(strs):
                if s[i] != ch:
                    return strs[0][:i]
        return strs[0][:i + 1]


# leetcode submit region end(Prohibit modification and deletion)

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
