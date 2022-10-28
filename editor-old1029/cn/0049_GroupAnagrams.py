
question_content = """
Given an array of strings strs, group the anagrams together. You can return the 
answer in any order. 

 An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once. 

 
 Example 1: 
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 
 Example 2: 
Input: strs = [""]
Output: [[""]]
 
 Example 3: 
Input: strs = ["a"]
Output: [["a"]]
 
 
 Constraints: 

 
 1 <= strs.length <= 10⁴ 
 0 <= strs[i].length <= 100 
 strs[i] consists of lowercase English letters. 
 

 Related Topics 数组 哈希表 字符串 排序 👍 1284 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def SortedDict_test():
            from sortedcontainers import SortedDict

            d = SortedDict()
            d = {'alpha': 1, 'beta': 2}
            SortedDict([('alpha', 1), ('beta', 2)]) == d
            # True
            s = SortedDict({'beta': 2, 'alpha': 1}) == d
            s = SortedDict(Counter("sdfsfdsf"))
            print(s)
            # True
            SortedDict(alpha=1, beta=2) == d
            # True
            return True

        return SortedDict_test()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from sortedcontainers import SortedDict

        def count(s) -> dict:
            d = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
            for c in s:
                d[c] += 1
            return d

        def counter(s) -> tuple:
            t = [0] * 26
            for c in s:
                t[ord(c) - ord('a')] += 1
            return tuple(t)

        ans = defaultdict(list)
        for s in strs:
            # hashcode = tuple((k, v) for k, v in SortedDict(Counter(s)).items())
            # hashcode = ''.join([str(k)+str(v) for k, v in count(s).items()])
            hashcode = "".join(sorted(s))
            # hashcode = counter(s)
            ans[hashcode].append(s)
        return list(ans.values())
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
