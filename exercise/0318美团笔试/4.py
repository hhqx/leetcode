n, x, y = map(int, input().split())

# 将每个商品的原价和折扣价存储为元组的形式
prices = []
for i in range(n):
    a, b = map(int, input().split())
    prices.append((a, b))

# 按照折扣价排序，优先购买折扣后价钱最小的商品
prices.sort(key=lambda p: p[1], reverse=True)

# 贪心算法，依次购买商品直到钱不够为止
count = 0
cost = 0
for a, b in prices:
    if x >= b:
        count += 1
        cost += b
        x -= b
    elif y > 0 and x + y >= a:
        count += 1
        cost += a
        y -= a - x
        x = 0
    else:
        break

print(count, cost)
