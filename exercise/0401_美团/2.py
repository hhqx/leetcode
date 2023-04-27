from acm_tools import *

question_str = """
时间限制： 3000MS
内存限制： 589824KB
题目描述：
       小美正在整理桌子上的一排装饰品。小美对待装饰品摆放方式的审美角度很奇特，她认为高度相差比较大的装饰品放在相邻位置会很难看，她想对这一排装饰品进行整理，可以交换任意两个装饰品的位置任意多次。假设当前从左到右n个装饰品的高度分别为h1,h2,...,hn，那么当前这一排装饰品的丑陋值为，其中|x|为x的绝对值。小美想最小化她的装饰品的丑陋值，请你帮她排一下顺序。

       形式化地来讲，有一长为n的序列a1,a2,...,an，你可以任意次数地进行交换，每次交换都可以选择任意两个不同的数i,j,交换ai,aj的位置。假设经过若干次交换后，序列变为h1,h2,...,hn，其丑陋值为 ，你需要找出一种交换方式，使得最终序列{hn}的丑陋值最小化。你不需要输出具体交换方式，只需要输出最终的{hn}序列的丑陋值即可。



输入描述
第一行一个整数n，表示小美的装饰品数量。

接下来一行n个整数a1,a2,...,an，依次表示从左到右n个装饰品的高度。

对于所有的数据:2≤N≤50000，0≤ai≤109。

输出描述
输出第一行一个数，为最优方案的最小丑陋值。


输入:
3
3 1 2
输出:
2
# 提示
我们可以将3和1交换，得到

1 3 2

然后再将2和3交换，得到

1 2 3

可以证明，此时有最小丑陋值|1-2|+|2-3|=2
"""
load_test_str(question_str)


#### START ###

from functools import reduce

def func(arr):
    n = len(arr)
    arr.sort()
    ans = sum(abs(arr[i] - arr[i+1]) for i in range(n-1))
    return ans

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    ret = func(arr)
    print(ret)

main()
# while True:
#     try:
#         main()
#     except:
#         break
#### END ###
