"""
给定N个字符串，每个字符串全部由小写字母组成，且每个字符串的长度最多为8，请你判断有多少重组字符串，重组字符串有以下规则:1.从每个字符串里面都抽取1个字母组成2.新字符串不能有2个相同的字母请问总共能组成多少个重组字符串

"""




# strs = []
# for _ in range(int(input())):
#     strs.append(input())
strs = ["qwe", "asd"]

n = len(strs)
buffer = [{c} for c in set(list(strs[0]))]
for s in strs[1:]:
    buffer_new = []
    for c in set(list(s)):
        for old in buffer_new:
            if c not in old:
                tmp = old.copy()
                tmp.add(c)
                buffer_new.append(tmp)
    buffer = buffer_new

print(len(buffer), buffer)

