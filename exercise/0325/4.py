


"""

小美因为自己差劲的表达能力而苦恼，小美想制作一个解释器，这样她可以在无法表达的情况下让解释器帮她解释。好巧不巧小美翻开了编译原理的书，找到了解释器的制作方式，她决定先制作一个书上习题中描述的小小解释器试试。

小美需要读入一行字符串，其格式为"key1=val1; key2=val2;  ...; keyn-1=valn-1; keyn=valn;"(不包含引号)这样的n对key,value对，其中keyi和vali为第 i 对key,value对，且均为仅包含大小写英文字母、数字与斜杠的非空字符串。例如对于字符串"SHELL=/bin/bash;HOME=/home/xiaomei;LOGNAME=xiaomei;"，那么其中包含三对key,value对，以(key,value)形式展示，分别为(SHELL,/bin/bash)、(HOME,/home/xiaomei)、(LOGNAME,xiaomei)。

接下来，小美的解释器需要接受q次询问，每次询问给出一个仅包含大小写英文字母、数字与斜杠的非空字符串，如果存在某对key,value对的key值与之相同，那么输出对应的value；如果存在多对key,value对的key值与之相同，那么输出其中编号最大的，也即最后那一对的value值；如果一对也不存在，那么输出EMPTY。

"""




































from collections import defaultdict


S = input().split(';')[:-1]
pair = []
d = defaultdict(lambda: 'EMPTY')
# print(S)
for row in S:
    key, value = row.split('=')
    d[key] = value

N = int(input())
for _ in range(N):
    q = input()
    print(d[q])


