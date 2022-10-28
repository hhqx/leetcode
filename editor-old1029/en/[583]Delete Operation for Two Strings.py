
question_content = """
Given two strings word1 and word2, return the minimum number of steps required 
to make word1 and word2 the same. 

 In one step, you can delete exactly one character in either string. 

 
 Example 1: 

 
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make 
"eat" to "ea".
 

 Example 2: 

 
Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

 
 Constraints: 

 
 1 <= word1.length, word2.length <= 500 
 word1 and word2 consist of only lowercase English letters. 
 
 Related Topics String Dynamic Programming 👍 4044 👎 59

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        self.mat = [[i+1] + [-1] * len(word2) for i in range(len(word1))]
        self.mat = [[i for i in range(len(word2)+1)]] + self.mat
        minDis = self.D(word1, word2)
        print(self.mat)
        return minDis

    def D(self, w1: str, w2: str) -> int:
        l1, l2 = len(w1), len(w2)
        if self.mat[l1][l2] >= 0:
            return self.mat[l1][l2]

        if w1[-1] == w2[-1]:
            d1 = self.D(w1[:-1], w2[:-1])
            d = d1
        else:
            d2 = self.D(w1[:-1], w2) + 1
            d3 = self.D(w1, w2[:-1]) + 1
            d = min(d2, d3)
        self.mat[l1][l2] = d
        return d
        pass
# leetcode submit region end(Prohibit modification and deletion)
 
def minDistance(self, word1: str, word2: str) -> int:
    l1, l2 = len(word1), len(word2)
    w1, w2 = word1, word2
    if l1 == 0:
        return l2
    elif l2 == 0:
        return l1

    if w1[-1] == w2[-1]:
        d1 = self.minDistance(w1[:-1], w2[:-1])
        d = d1
    else:
        d2 = self.minDistance(w1[:-1], w2) + 1
        d3 = self.minDistance(w1, w2[:-1]) + 1
        d = min(d2, d3)
    return d

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
