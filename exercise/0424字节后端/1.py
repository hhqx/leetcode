n, k = 5, 4

odd, even = [x for x in range(1, n + 1) if x % 2 == 1], [x for x in range(1, n + 1) if x % 2 == 0]
print(odd, even)
ans = []
for i in range(k//2):
    ans.append(odd.pop())
    ans.append(even.pop())
if k % 2 == 1:
    ans.append(odd.pop())
    while odd:
        ans.append(odd.pop())
    while even:
        ans.append(even.pop())
else:
    while even:
        ans.append(even.pop())
    while odd:
        ans.append(odd.pop())

print(*ans)

## validate
cnt = 0
for i in range(len(ans) - 1):
    if (ans[i] + ans[i + 1]) % 2 == 1:
        cnt += 1
print('cnt', cnt, 'k', k)
assert cnt == k, ""
