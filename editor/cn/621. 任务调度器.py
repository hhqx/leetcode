
question_content = """
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位
时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。 

 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。 

 你需要计算完成所有任务所需要的 最短时间 。 

 

 示例 1： 

 
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 

 示例 2： 

 
# 输入：tasks = ["A","A","A","B","B","B"], n = 0
# 输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类
 

 示例 3： 

 
输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命)
 -> (待命) -> A
 

 

 提示： 

 
 1 <= task.length <= 10⁴ 
 tasks[i] 是大写英文字母 
 n 的取值范围为 [0, 100] 
 

 Related Topics 贪心 数组 哈希表 计数 排序 堆（优先队列） 👍 1052 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """ 策略, 从当前冷却完成的任务中选择频次最高的执行, """
        from sortedcontainers import SortedList
        INF = float('inf')
        d = Counter(tasks)
        heap = []
        for k, freq in d.items():
            heapq.heappush(heap, (-freq, -INF, k))

        q = SortedList((-INF, freq, k) for k, freq in d.items())
        # q = [(-INF, freq, k) for k, freq in d.items()]

        # 用大顶堆每次筛选出频次最高的执行, 相同频次选取上次一执行时间小的
        # 错误
        # 若冷却不满足, 等待
        cool = deque([None] * n)
        t = 0
        cnt = 0
        while cnt != len(d):
            if heap:
                freq, last_t, task = heapq.heappop(heap)
                freq = -freq

                # t += 1
                print(task)
                if t - last_t - 1 >= n:

                    pass
                else:
                    # print('error', last_t, t, n)
                    # t = last_t + n + 1
                    pass

                freq -= 1
                if freq > 0:
                    cool.append((-freq, t, task))
                else:
                    cnt += 1
                    cool.append(None)
            else:
                print('cool')
                # t += 1
                cool.append(None)
            t += 1
            if cool:
                item = cool.popleft()
                if item:
                    heapq.heappush(heap, item)

        return t

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        策略, 从当前冷却完成的任务中选择频次最高的执行,
        实现方式: 冷却缓冲区 + 优先队列
        """
        d = Counter(tasks)
        heap = []
        for k, freq in d.items():
            heapq.heappush(heap, (-freq, k))

        # 用大顶堆每次筛选出频次最高的执行, 相同频次选取上次一执行时间小的
        # 若冷却不满足, 等待
        cool = deque([None] * n)
        t = 0
        cnt = 0
        while cnt != len(d):
            if heap:
                freq, task = heapq.heappop(heap)
                freq = -freq

                # print(task)

                freq -= 1
                if freq > 0:
                    cool.append((-freq, task))
                else:
                    cnt += 1
                    cool.append(None)
            else:
                # print('cool')
                cool.append(None)

            t += 1

            item = cool.popleft()
            if item:
                heapq.heappush(heap, item)

        return t
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
