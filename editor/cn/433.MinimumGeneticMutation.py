question_content = """
A gene string can be represented by an 8-character long string, with choices 
from 'A', 'C', 'G', and 'T'. 

 Suppose we need to investigate a mutation from a gene string start to a gene 
string end where one mutation is defined as one single character changed in the 
gene string. 

 
 For example, "AACCGGTT" --> "AACCGGTA" is one mutation. 
 

 There is also a gene bank bank that records all the valid gene mutations. A 
gene must be in bank to make it a valid gene string. 

 Given the two gene strings start and end and the gene bank bank, return the 
minimum number of mutations needed to mutate from start to end. If there is no 
such a mutation, return -1. 

 Note that the starting point is assumed to be valid, so it might not be 
included in the bank. 

 
 Example 1: 

 
Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
 

 Example 2: 

 
Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA",
"AAACGGTA"]
Output: 2
 

 Example 3: 

 
Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC",
"AACCCCCC"]
Output: 3
 

 
 Constraints: 

 
 start.length == 8 
 end.length == 8 
 0 <= bank.length <= 10 
 bank[i].length == 8 
 start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T']. 
 

 Related Topics 广度优先搜索 哈希表 字符串 👍 230 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """ 根据编辑距离建立状态转移图, bfs求出最小状态转移次数. """
        if end not in bank:
            return -1
        if start == end:
            return 0
        def get_dis(a, b):
            """ 判断a,b之间是否可以在1个字符以内替换, 是返回替换次数, 否则返回2. """
            cnt = 0
            for c1, c2 in zip(a, b):
                cnt += c1 != c2
                if cnt >= 2:
                    return 2
            return cnt

        # 建立状态转移图
        bank = [start] + bank + [end]
        edge = []
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                eds = get_dis(bank[i], bank[j])
                if eds <= 1:
                    edge.append((i, j, eds))

        # bfs 求起始状态到结束状态的最短路径
        q = deque([0])
        visited = set([0])
        cnt = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == len(bank) - 1:
                    return cnt
                for i, j, e in edge:
                    if i == node and j not in visited:
                        visited.add(j)
                        q.append(j)
                    if j == node and i not in visited:
                        visited.add(i)
                        q.append(i)
            cnt += 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
