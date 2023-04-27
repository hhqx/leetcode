

from acm_tools import *

question_str = """
时间限制： 3000MS
内存限制： 589824KB
题目描述：
       小美最近在魔法课中掌握了倒水魔法：可以运用法力隔空倒水。最近魔法课考试临近，小美早早地来到了魔法训练室训练难以掌握的倒水魔法。

       魔法训练室里有n个神奇的杯子，有着不同的大小，假设第i个杯子已满，向其倒水，多余的水会正正好好流向第i+1个杯子（如果i=n时没有下一个杯子，不会有杯子接住此时多余的水而溢出到魔法训练室的水池）。

       这些杯子有着初始固定的水量，每次练习后杯子里的水都会还原到最初状态。每次练习时，魔法黑板会告诉小美需要将哪一个杯子倒满水。因为每个杯子的材质和形状有所不同，所以对其释放倒水魔法需要消耗的魔法值不同。小美想尽可能多练习，所以需要最小化每次消耗的魔法值的总量。



输入描述
第一行一个整数n，表示杯子数量。

第二行n个整数x1,x2,...,xn，依次表示第 i 个杯子能容纳水的量（单位为毫升）。

第三行n个整数y1,y2,...,yn，依次表示第 i 个杯子初始有的水量（单位为毫升）。

第四行n个整数z1,z2,...,zn，依次表示对第 i 个杯子每添加1毫升水需要消耗的法力值。

第五行一个整数m，表示练习的数量。

第六行m个整数q1,q2,...,qm，依次表示第i次练习时需要将第qi个杯子倒满。（每次练习过后，杯子里的水量都会还原为初始状态，不会影响到下一次练习）

1≤n,m≤3000 , 1≤yi≤xi≤109, 1≤zi≤300,1≤qi≤n

输出描述
输出第一行m个数，依次表示每次训练时需要消耗的最小法力值。如果杯子初始本身就是满的，则需要消耗的法力值为0。


输入:
3
1 2 3
1 1 2
1 2 5
2
3 1
输出:
2 0

# 提示
样例解释

第一次训练，最优方案如下：

初始时杯子的水量和最大容量分别为

1/1 1/2 2/3

1. 给1号杯子（本身已满）倒水1毫升，消耗1点法力，水溢出转移到2号杯子，当前状态为

1/1 2/2 2/3

2. 继续给1号杯子（本身已满）倒水1毫升，消耗1点法力，水溢出到2号杯子（也已满），继续溢出到3号杯子,此时3号杯子也被成功注满水，状态为：

1/1 2/2 3/3

共消耗2点法力。可以证明没有更优方案。

 

第二次训练时， 

初始时杯子的水量和最大容量分别为（注意不同训练互不影响，因为训练结束后魔法会让水杯还原为初始状态）

1/1 1/2 2/3

可以发现1号杯子已满，不用注水，消耗法力为0。
"""
load_test_str(question_str)


#### START ###

from functools import reduce
from math import inf
def func(pair, arr):

    n, m = len(pair), len(arr)
    ans = []
    left = [cap - init for cap, init, cost in pair]
    cost = [cost for cap, init, cost in pair]
    prefix = [0]
    for num in left:
        prefix.append(prefix[-1] + num)

    def sum_ij(i, j):
        # return sum(left[i:j])
        return prefix[j] - prefix[i]

    for end in arr:
        val = inf
        for i in range(0, end):
            tmp = sum_ij(i, end) * cost[i]
            val = min(val, tmp)
        ans.append(val)

    return ans

from math import inf
from itertools import accumulate


def func(pair, nums):
    left = [x - y for x, y, z in pair]
    cost = [z for x, y, z in pair]
    p = list(accumulate(left, initial=0))
    return [min((p[i] - p[j]) * cost[j] for j in range(0, i)) for i in nums]

def main():
    n = int(input())
    col1 = list(map(int, input().split()))
    col2 = list(map(int, input().split()))
    col3 = list(map(int, input().split()))
    pair = list(zip(col1, col2, col3))
    m = int(input())
    arr = list(map(int, input().split()))
    ret = func(pair, arr)
    print(*ret)

main()
