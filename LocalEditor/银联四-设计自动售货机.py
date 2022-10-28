
"""

银联-4. 设计自动售货机

https://leetcode.cn/contest/cnunionpay2022/problems/NyZD2B/


「银联二维码」支付可以提供简便、顺畅的消费服务，通过出示二维码或扫描二维码即可完成支付。
现有一台使用银联二维码进行支付的自动售货机，并对使用 银联 支付的用户提供额外的优惠服务。


"""



from collections import defaultdict
from sortedcontainers import SortedList

d = defaultdict(SortedList)


class VendingMachine:

    def __init__(self):
        from sortedcontainers import SortedList
        self.d = defaultdict(SortedList)

    def addItem(self, time: int, number: int, item: str, price: int, duration: int) -> None:
        self.d[item].add([price, time+duration, number])
        return


    def sell(self, time: int, customer: str, item: str, number: int) -> int:
        if len(self.d[item]) == 0:
            return -1
        if number == 0:
            return 0
        
        p = 0
        for i, (price, ddl, n) in enumerate(self.d[item]):
            if time >= ddl:
                continue
            if n > number:
                # n -= number
                self.d[item][i][-1] -= number
                p += number * price
                number = 0
                break
            elif n <= number:
                p += n * price
                n=0
                self.d[item][i][-1] -= 0
                number -= n
                
                # self.pop() # 删除无效商品
        
        return p if number == 0 else -1



# Your VendingMachine object will be instantiated and called as such:
# obj = VendingMachine()
# obj.addItem(time,number,item,price,duration)
# param_2 = obj.sell(time,customer,item,number)


class VendingMachine:

    def __init__(self):
        self.d = collections.defaultdict(list)
        self.c = collections.defaultdict(int)


    def addItem(self, time: int, number: int, item: str, price: int, duration: int) -> None:
        heapq.heappush(self.d[item], [price, time + duration, number])


    def sell(self, time: int, customer: str, item: str, number: int) -> int:
        c = 0
        pp = 0
        tmp = []
        while self.d[item]:
            p, t, n = heapq.heappop(self.d[item])
            if t < time:
                continue
            if n > number - c:
                n -= number - c
                pp += (number - c) * p
                c = number
                heapq.heappush(self.d[item], [p, t, n])
                break
            else:
                c += n
                pp += p * n
                if number == c:
                    break
                tmp.append([p, t, n])
        if c == number:
            self.c[customer] += 1
            if (pp * max(70, 101 - self.c[customer])) % 100 == 0:
                return int((pp * max(70, 101 - self.c[customer])) / 100)
            else:
                return int((pp * max(70, 101 - self.c[customer])) / 100) + 1
        else:
            for p, t, n in tmp:
                heapq.heappush(self.d[item], [p, t, n])
            return -1
            



# Your VendingMachine object will be instantiated and called as such:
# obj = VendingMachine()
# obj.addItem(time,number,item,price,duration)
# param_2 = obj.sell(time,customer,item,number)