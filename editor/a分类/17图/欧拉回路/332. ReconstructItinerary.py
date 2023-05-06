question_content = """
You are given a list of airline tickets where tickets[i] = [fromi, toi] 
represent the departure and the arrival airports of one flight. Reconstruct the 
itinerary in order and return it. 

 All of the tickets belong to a man who departs from "JFK", thus, the itinerary 
must begin with "JFK". If there are multiple valid itineraries, you should 
return the itinerary that has the smallest lexical order when read as a single 
string. 

 
 For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than [
"JFK", "LGB"]. 
 

 You may assume all tickets form at least one valid itinerary. You must use all 
the tickets once and only once. 

 
 Example 1: 
 
 
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
 

 Example 2: 
 
 
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],[
"ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL",
"SFO"] but it is larger in lexical order.
 

 
 Constraints: 

 
 1 <= tickets.length <= 300 
 tickets[i].length == 2 
 fromi.length == 3 
 toi.length == 3 
 fromi and toi consist of uppercase English letters. 
 fromi != toi 
 

 Related Topics 深度优先搜索 图 欧拉回路 👍 781 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """ 欧拉回路, 求半欧拉图(有向图)的欧拉回路 """
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        满足半欧拉图的有向图,
        欧拉图定义: 一笔画不重复走完所有点
        半欧拉图定义: 一笔画不重复走完所有边

        半欧拉图求解路径思路:  heap + 回溯
            通过 heap 来对图进行遍历, 在回溯的时候添加节点

        欧拉通路充要条件:
            "以节点u为起点的有向图欧拉通路路径" <=> "必须要求节点u的出度>=入度,
                且最多只有各一个节点的入度和出度差值为1, 其余入度出度均相等"

        """
        g = defaultdict(list)
        for u, v in tickets:
            g[u].append(v)

        # 对节点的边进行最小堆排序
        for k in g:
            heapq.heapify(g[k])

        # 因为欧拉通路一定存在, 所有直接 贪心建图+回溯遍历(后序遍历)就行
        path = []
        def dfs(u):
            """ 在回溯的时候添加当前节点 """
            while g[u]:
                v = heappop(g[u])
                dfs(v)
            path.append(u)

        dfs("JFK")
        return path[::-1]

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        求解半欧拉图的有向图的最小欧拉通路:
            节点分支排序 + 后序遍历 + 翻转

        """
        g = defaultdict(list)
        for u, v in tickets:
            g[u].append(v)

        # 对节点的边进行排序
        for k in g:
            g[k].sort(reverse=True)

        # 因为欧拉通路一定存在, 所有直接 贪心排序 + 后序遍历 就行
        path = []
        def dfs(u):
            """ 后序遍历, 在回溯的时候添加当前节点, 遍历的时候不能重复访问边(遍历之后直接删除该边) """
            while g[u]:
                v = g[u].pop()
                dfs(v)
            path.append(u)

        dfs("JFK")
        return path[::-1]
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
