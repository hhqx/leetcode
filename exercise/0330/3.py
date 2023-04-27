
n = int(input())
nums = list(map(int, input().split(' ')))

def maxMultiVal(l, r):
    ans = (-inf, 0, 0, 0)
    arr = nums[l:r]
    if not arr:
        return ans
    p = [1]
    for num in arr:
        p.append(num * p[-1])

    for i in range(0, len(p)):
        if p[-1] > 0 and p[i] > 0 or p[-1] < 0 and p[i] < 0:
            ans = (p[-1] // p[i], len(p) -i, i+ 1, len(p))
            break

    for j in range(len(p) - 1, -1, -1):
        if p[j] * p[-1] < 0:
            for i in range(0, j + 1):
                if p[j] > 0 and p[i] > 0 or p[j] < 0 and p[i] < 0:
                    ans = max(ans, (p[j] // p[i], j - i + 1, i + 1, j + 1))
                    break
            break

    return (ans[0], ans[1], ans[2] + l, ans[3] + l)


from math import inf

start = 0
ans = (-inf, 0, 0, 0)
for i in range(n):
    if nums[i] == 0:
        end = i
        val = maxMultiVal(start, end)
        ans = max(ans, val)
        start = i + 1
    elif i == n - 1:
        end = i + 1
        val = maxMultiVal(start, end)
        ans = max(ans, val)

if ans[0] <= 0:
    print(-1)
else:
    print(ans[2] - 1, ans[3] - 2)
