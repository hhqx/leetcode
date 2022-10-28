from collections import defaultdict

from sortedcontainers import SortedList

nums = [1,3,5,2,7,5]
minK = 1
maxK = 5

# nums = [1,1,1,1]
# minK = 1
# maxK = 1

# a = SortedList()
# for i in range(len(nums)):
#     a.add(nums[i])
#     if a[0] == minK and a[-1] == maxK:
#         ans += 1

def f(x, min,max):
    if x < min:
        return 1
    elif x == min:
        return 2
    elif x == max:
        return 4
    elif x < max:
        return 3
    elif x > max:
        return 5

digitalized = [f(nums[i],minK,maxK) for i in range(len(nums))]
nums = [f(nums[i],minK,maxK) for i in range(len(nums))]
print(digitalized)

ans = 0
cnt = defaultdict(int)
left, right = 0, 0
mn, mx = float('inf'), float('-inf')

isminmax = lambda x: x[2] > 0 and x[1] == 0 and x[4] > 0 and x[5] == 0
# def isminmax(x):
#     return x[2] > 0 and x[1] == 0 and x[4] > 0 and x[5] == 0
while right < len(nums):


    # while right < len(nums) and nums[right] not in {2, 4}:
    # while right < len(nums) and not(cnt[2] > 0 and cnt[4] > 0):
    while right < len(nums) and not isminmax(cnt):
        cnt[nums[right]] += 1
        right += 1

    while right < len(nums) and isminmax(cnt):
        cnt[nums[right]] += 1
        right += 1

    # if right < len(nums):
    #     cnt[nums[right]] += 1
    #     right += 1

    # if cnt[2] > 0 and cnt[1] == 0 and cnt[4] > 0 and cnt[5] == 0:
    #     ans += 1

    # while left < right < len(nums) and nums[left] not in {2, 4}:
    # while left < right < len(nums) and (cnt[2] > 0 and cnt[4] > 0):
    while left < len(nums) and isminmax(cnt):
        cnt[nums[left]] -= 1
        left += 1
        ans += 1

    # if left < right < len(nums):
    #     cnt[nums[left]] += 1
    #     left += 1

print('ans=', ans)