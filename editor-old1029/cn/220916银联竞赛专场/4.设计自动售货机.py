from heapq import heappop
from math import ceil
from heapq import heappush

question_content = """
Related Topics 设计 哈希表 数据流 有序集合 堆（优先队列） 👍 121 👎 0

输入：
op=["VendingMachine","addItem","sell","sell","sell","sell"],
args=[[],[0,3,"Apple",10,10],[1,"Tom","Apple",1],[2,"Tom","Apple",3],[3,"Mary","Banana",2],[11,"Jim","Apple",1]]

输出: [null,null,10,-1,-1,-1]


输入：
op=["VendingMachine","addItem","addItem","sell","addItem","sell","sell","sell","addItem","sell","sell"],
args=[[],[0,1,"Apple",4,3],[1,3,"Apple",4,2],[2,"Mary","Apple",2],[2,1,"Banana",2,5],[4,"Jim","Banana",2],[4,"Mary","Banana",1],[4,"Mary","Apple",1],[6,200,"Apple",2,5],[6,"Jim","Apple",100],[7,"Mary","Apple",100]]

输出: [null,null,null,8,null,-1,2,-1,null,200,196]



"""

from typing import *
from PythonLeetcodeRunner import *


class VendingMachine:

    def __init__(self):
        from collections import defaultdict
        self.items = defaultdict(list)
        self.cnt = defaultdict(lambda: 101)

    def addItem(self, time: int, number: int, item: str, price: int, duration: int) -> None:

        heappush(self.items[item], (price, time + duration, number))

    def sell(self, time: int, customer: str, item: str, number: int) -> int:
        heap = self.items[item]
        total = 0
        for _, t, cnt in heap:
            if t >= time:
                total += cnt
            if total >= number:
                break
        if total < number:
            return -1
        if self.cnt[customer] > 70:
            self.cnt[customer] -= 1
        total = 0
        pay = 0
        while self.items[item]:
            p, t, cnt = heappop(heap)
            if t < time:
                continue
            if total + cnt <= number:
                total += cnt
                pay += cnt * p
            else:
                buy = number - total
                pay += buy * p
                heappush(heap, (p, t, cnt - buy))
                break
        return ceil(pay * self.cnt[customer] / 100)


# Your VendingMachine object will be instantiated and called as such:
# obj = VendingMachine()
# obj.addItem(time,number,item,price,duration)
# param_2 = obj.sell(time,customer,item,number)

if __name__ == "__main__":
    # TestObj = StartTest(question_content, Solution)
    TestObj = StartTest(question_content, VendingMachine, isDesignedClass=True)
    TestObj.run_test()

