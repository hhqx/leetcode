from acm_tools import *

question_str = """
给定一个字符串，字符串有大写和小写字母。你需要维护以下两种操作:
1.输入 1,1,r，代表将[l,r]区间内所有字母的大小写反转(即大写变小写，小写变大写)
2.输入 2,1,r，代表查询[l,r]子串中大小写连续段的数量

我们定义大小写连续段为极长的、大小写相同的一段连续子串。例如，“abCDefg"有三个连续段:"ab"、"CD"和"efg”。
另外，我们定义字符串的下标从1开始。
输入描述:
第一行输入一个两个正整数n和q，代表字符串长度以及操作次数
第二行输入一个长度为n的、仅包含大小写字母的字符串。
接下来的q行，每行输入三个正整数op,l,r，代表一次操作。其中op代表操作类型。
1 <= n <= 10**3
1 <= l <= r <= n
保证至少有一个2号操作。

输出描述
对于每个2号操作，输出一行一个正整数代表答案。

输入:
5 3
abCdA
2 2 5
1 3 4
2 2 5
输出:
4 2
"""
load_test_str(question_str)


#### START ###

def func(s, pair):
    arr = [c.isupper() for c in s]

    def get_segs(arr, l, r):
        if l >= r:
            return 0
        ans = 1
        for i in range(l, r - 1):
            if arr[i] != arr[i + 1]:
                ans += 1
        return ans

    # print_std(s, pair)
    ans = []
    for op, l, r in pair:
        if op == 1:
            arr[l - 1:r] = map(lambda x: x == 0, arr[l - 1:r])
        else:
            val = get_segs(arr, l-1, r)
            ans.append(val)
        # print_std(arr)
        dprint(arr)
    # print_std(ans)
    return ans


def main():
    n, q = map(int, map(int, input().split()))
    s = input()
    pair = []
    for _ in range(q):
        row = list(map(int, input().split()))
        pair.append(row)
    ret = func(s, pair)
    print(*ret)

main()


#### END ###
