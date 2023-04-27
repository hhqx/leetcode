from acm_tools import *

question_str = """
时间限制： 3000MS
内存限制： 589824KB
题目描述：
       小美在数学课上学会了加减乘除，现在她想多进行一些算数训练来加强自己的计算能力。为了不重复出题，她想出一个好方法。
       她先写下了一排n个数(n≥2)，依次用加号连接。举例来说，小美可能写下了如下的式子1+4+7+4+2+3+1共7个数以及6个加号。
       接着小美以一种全新的方式进行出题：她每次选择一个加号，将它改变成加减乘除中的一个（虽然很奇怪，但小美认为加号也可以被改成加号，尽管不会产生任何影响），
       然后计算整个式子的结果。值得注意的是，小美认为每次操作不对后续操作产生影响，详见样例解释。

       小美认真做了很多次算数训练，现在她想让作为她好朋友的你帮她用程序计算一次，方便她核对答案。



输入描述
第一行一个整数n，合义见题面。

接下来一行n个整数a1,a2,..,an，依次表示小美初始写下的连加算式中的每一个数。

接下来一个整数m，表示小美做了m次算数训练

接下来2m个以空格分开数字或符号 t1,o1, t2,o2, ... tm,om，其中ti为数字，oi是'+','-','*','/'(即加减乘除符号，不含引号)中的一个符号，表示第 i 次操作选定了第ti个加号，将其改变为了oi。

对于所有的的数据,2≤N≤50000，1≤M≤50000,1≤ai≤500,1≤ti<N,oi∈{+,-,*,/}

输出描述
输出一行m个整数，分别表示每次操作的答案，结果四舍五入到一位小数。


样例输入
5
1 2 4 2 5
3
1 - 2 * 4 /
样例输出
10.0 16.0 7.4

# 提示
样例解释

第一次操作后算数式为1-2+4+2+5 = 10.0

第二次操作后算数式为1+2*4+2+5 = 16.0

第三次操作后算数式为1+2+4+2/5 = 7.4

值得注意的是，每次操作都认为对初始的全加号式子(此处为1+2+4+2+5)进行操作，操作之间互不影响。
"""
load_test_str(question_str)


#### START ###

from functools import reduce

def func(arr, pair):
    n, m = len(arr), len(pair)
    op = ['+'] * (n-1)
    ans = []
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)

    for i, o in pair:
        op[i-1] = o
        s = [str(arr[0])]
        for j in range(1, len(arr)):
            s.append(str(op[j-1]))
            s.append(str(arr[j]))
        string = "".join(s)
        val = eval(string)
        # print_std(f'{string}={val}')
        op[i - 1] = '+'
        ans.append("%.1f" % round(val, 1))
    return ans

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    op = list(map(str, input().split()))
    pair = [[int(op[2*i]), op[2*i+1]] for i in range(m)]
    ret = func(arr, pair)
    print(*ret)

main()
# while True:
#     try:
#         main()
#     except:
#         break
#### END ###
