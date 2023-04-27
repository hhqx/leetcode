from acm_tools import *

question_str = """
时间限制： 3000MS
内存限制： 589824KB
题目描述：
       小美爱上了收藏！现在她给自己修建了一排n个收藏夹分别编号为1,2,3,...,n。

       有时小美会改变某一个收藏夹里的内容，例如从中拿入、拿出一些藏品，这样的操作会改变小美对这个收藏夹的欣赏程度，我们记编号为i的收藏夹小美对其的欣赏程度为ai。还有一些时候，小美会欣赏连续编号的一些收藏夹，例如编号为L,L+1,L+2,...,R-1,R的这一些收藏夹，她能从中获得的满足感为这些收藏夹的欣赏程度之和，即 。

       小美想在欣赏之前提前做一些评估，想知道如果她选择编号区间为[L,R]的收藏夹，能给她带来的满足感是多少。小美想请你，最好的朋友，来帮帮她。



输入描述
第一行两个整数n和m，表示小美的收藏夹数量和小美的操作数量。初始时刻收藏夹都是空的，也即ai=0(i∈[1,n])

第二行m个整数op1,op2,...,opm。

第三行m个整数x1,x2,...,xm。

第四行m个整数y1,y2,...,ym，这些共同表示了m次操作。具体而言，对第i次操作，opi=0时表示为一次收藏夹更新操作，会将xi位置的收藏夹欣赏程度更新为yi，即axi=yi；
opi=1时表示为一次查询操作，表示如果小美欣赏编号在区间[xi,yi]的收藏夹，能获得的满足感是多少，也即的值。

对于所有的数据，1≤n,m≤ 50000,opi∈{0,1},当opi=0 时,1≤xi≤n,0≤yi≤10000; 当opi=1 时，1≤xi≤yi≤n。保证至少有一次opi=1 的操作。

输出描述
对每个opi=1的操作，输出一个数表示对应答案。空格隔开所有答案。


输入:
4 7
1 0 1 0 1 0 1
1 1 1 3 1 4 1
3 2 3 5 3 100 3
输出:
0 2 7 7

# 提示
样例解释

操作记录为

0 0 0 0 (初始)

<询问[1,3],结果为0+0+0>

2 0 0 0 <1号更改为2>

<询问[1,3],结果为2+0+0>

2 0 5 0 <3号更改为5>

<询问[1,3],结果为2+0+5>

2 0 5 100 <4号更改为100>

<询问[1,3],结果为2+0+5>
"""
load_test_str(question_str)


#### START ###

from functools import reduce

def func(arr, pair):
    """ 更新和求和, 可以用树状数组写, 先写前缀和暴力 """
    n, m = len(arr), len(pair)
    ans = []
    prefix = [0] * (n+1)
    for num in arr:
        prefix.append(prefix[-1] + num)
    for p, x, y in pair:
        if p == 1:
            val = prefix[y] - prefix[x-1]
            ans.append(val)
        else:
            for j in range(x, len(prefix)):
                prefix[j] += y - arr[x-1]
            arr[x - 1] = y

    return ans
def func(arr, pair):
    """ 更新和求和, 可以用树状数组写, 先写前缀和暴力 """
    n, m = len(arr), len(pair)
    ans = []
    prefix = [0] * (n+1)
    for num in arr:
        prefix.append(prefix[-1] + num)
    for p, x, y in pair:
        if p == 1:
            val = sum(arr[x-1:y])
            ans.append(val)
        else:
            arr[x - 1] = y

    return ans

def main():
    n, m = list(map(int, input().split()))
    arr = [0] * n
    col1 = list(map(int, input().split()))
    col2 = list(map(int, input().split()))
    col3 = list(map(int, input().split()))
    pair = list(zip(col1, col2, col3))
    ret = func(arr, pair)
    print(*ret)

main()
