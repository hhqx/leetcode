"""

假设李明的密码为5464640701,为了好记，他设计一个变换规则把这个码变换成LIming0701
他设计的变换规则为，
1、小写字母按如下映射关系，进行映射(a、b''c) >2, (d,e、") ->3, (g、h、") --4 (7、k、") ->5.('m'、'n'、'o') 6
pg、"s) ->7.(、"u、 v) ->8 , (wx、y、'z') ->9.
2、大写字母变成小写后前跳一位，如:"B，先变成小写，再往前跳一个字母，变成a，然后参照第一条转换规则转换特殊说明:"a往前移动变成Z3、其他字符不做变化限制:客码字符串中不合空格

输入描述
输入是一个明文，密码长度不超过100个字符，输入的字符串在文件首行
输出描述
输出转换后的密码
示例1
输入输出示例仅供调试，
输入:
LIming070
输出:
5464640701
复抽
"""

import itertools


def func(s="LIming0701"):
    """ n个人, m个房间 """

    map = {}
    for i, chrs in enumerate("abc def ghi jkl mno pqrs tuv wxyz".split()):
        for c in chrs:
            map[c] = str(i + 2)
    for i in range(26):
        upper = chr(ord('A') + i)
        lower = chr(ord('a') + (i - 1) % 26)
        map[upper] = lower

    ans = []
    for c in s:
        rep = c
        if c in map:
            if c.isupper():
                rep = map[map[c]]
            else:
                rep = map[c]
        ans.append(rep)

    print("".join(ans))


for s in ("LIming0701",):
    print("s={}, 的结果为: ".format(s))
    func(s)
