
question_content = """
You are given an array of words where each word consists of lowercase English 
letters. 

 wordA is a predecessor of wordB if and only if we can insert exactly one 
letter anywhere in wordA without changing the order of the other characters to make 
it equal to wordB. 

 
 For example, "abc" is a predecessor of "abac", while "cba" is not a 
predecessor of "bcad". 
 

 A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, 
where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. 
A single word is trivially a word chain with k == 1. 

 Return the length of the longest possible word chain with words chosen from 
the given list of words. 


Input: words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
Output: 7

Input: words = ["bdca","bda","ca","dca","a"]
Output: 4

 Example 1: 

 
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
 

 Example 2: 

 
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", 
"pcxbc", "pcxbcf"].
 

 Example 3: 

 
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters 
is changed.
 
Input: words = ["a","ab","ac","bd","abc","abd","abdd"]
Output: 4


 Constraints: 

 
 1 <= words.length <= 1000 
 1 <= words[i].length <= 16 
 words[i] only consists of lowercase English letters. 
 
 Related Topics Array Hash Table Two Pointers String Dynamic Programming 👍 3874
 👎 177

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # sort words by words[i].length
        Len = [len(word) for word in words]
        sort_index = sorted(range(len(Len)), key=lambda k: Len[k])
        words = [words[idx] for idx in sort_index]
        Len = [Len[idx] for idx in sort_index]

        # 对于长度为Len的word, 在长度为Len-1的word中搜索, 判断是否组成WordChain
        maxChain = [1 for i in range(len(Len))]
        for i, l in enumerate(Len):
            if i == 0:
                bminmax = [0, 0]
                continue
            if Len[i] != Len[i-1]:
                bminmax = [bminmax[1], i]
            for j in range(bminmax[0], bminmax[1], 1):
                if self.isPredecessor(words[j], words[i]):
                    maxChain[i] = max(maxChain[i], maxChain[j] + 1)
                    # print(f'\n{maxChain[i]}, {maxChain[j]}')
                    # print(f'{words[i]}, {words[j]}')

        # for i, l in enumerate(Len):
        #     if i == 0:
        #         continue
        #     for j in range(i - 1, -1, -1):
        #         # if words[j] is in words[i]:
        #         if Len[j]+1 == Len[i] and self.isPredecessor(words[j], words[i]):
        #             maxChain[i] = maxChain[i-1] + 1
        #             break
        #     if j == 0:
        #         maxChain[i] = maxChain[i - 1]

        # maxChainLength = max(maxChain)
        return max(maxChain)
        pass

    @staticmethod
    def isPredecessor(s1, s2):
        """ Return True if s1 is a predecessor of s2. """
        p2 = 0
        for p1 in range(len(s1)):
            while s2[p2] != s1[p1]:
                p2 = p2 + 1
                if p2 >= len(s2):
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
