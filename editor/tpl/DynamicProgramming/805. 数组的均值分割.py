question_content = """
给定你一个整数数组
 nums 

 我们要将
 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和
 B 数组不为空，并且
 average(A) == average(B) 。 

 如果可以完成则返回true ， 否则返回 false 。 

 注意：对于数组
 arr , 
 average(arr) 是
 arr 的所有元素的和除以
 arr 长度。 

# 输入: nums = [5,3,11,19,2]
# 输出: true
# 
# 输入: nums = [3,1]
# 输出: false

测试用例:[60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
测试结果:true
期望结果:false


 示例 1: 
测试用例:[18,10,5,3]

# 测试结果: false
期望结果:false

输入: nums = [5,3,11,19,2]
输出: true

输入: nums = [1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。


 示例 2: 






 提示: 


 1 <= nums.length <= 30 
 0 <= nums[i] <= 10⁴ 


 Related Topics 位运算 数组 数学 动态规划 状态压缩 👍 213 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """ 记忆化搜索式dp, 参考别人的题解 """

        @cache
        def dp(i, cnt, x):
            """ dp(i, cnt, x) 表示 nums[:i+1] 中是否存在长度为 cnt 和为 x 的子集 """
            if cnt == 0:
                return x == 0
            if x < 0 or cnt > i + 1:  # 可选数组中长度不足 cnt, 或 x < 0, 返回 False
                return False
            return dp(i - 1, cnt - 1, x - nums[i]) or dp(i - 1, cnt, x)

        n = len(nums)
        total = sum(nums)
        for cnt in range(1, n // 2 + 1):
            # 枚举长度在 [1, n // 2] 内的所有子集
            if total * cnt % n == 0 and dp(len(nums) - 1, cnt, total * cnt // n):
                return True
        return False


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """
        状压dp原始版, TLE, 过78个case
        """
        n = len(nums)
        total = sum(nums)

        # dp[i][cnt][x] 为True 表示数组nums[:i+1]中存在长度为cnt和为x的子集
        dp = [[[False] * (total + 1) for _ in range(n + 1)] for __ in range(n + 1)]
        # 设定初值, 长度为零时, 只有 0 存在
        for i in range(n):
            dp[i][0][0] = True

        # 状压dp
        # 如果 dp[i][cnt][x] 或 dp[i][cnt-1][x-num] 存在, 则 dp[i+1][cnt][x] 也一定存在
        for i in range(len(nums)):
            num = nums[i]
            for cnt in range(1, n, 1):
                for x in range(0, total + 1):
                    dp[i + 1][cnt][x] = dp[i][cnt][x] | (dp[i][cnt - 1][x - num] if x - num >= 0 else False)

        for cnt in range(1, n // 2 + 1):
            # 枚举长度在 [1, n // 2] 内的所有子集
            if total * cnt % n == 0 and dp[len(nums)][cnt][total * cnt // n]:
                return True
        return False


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """
        状压dp滚动数组优化第一维版, TLE, 过83个case
        相比上一个原始版:
        1. 滚动数组优化了第一个维度,
        2. 子集长度那维可以减小到 n//2, 因为任何一个分划中必然存在一个子集小于等于 n//2
        """
        n = len(nums)
        total = sum(nums)

        # dp[cnt][x] 为True 表示数组nums[:i+1]中存在长度为cnt和为x的子集
        dp = [[False] * (total + 1) for _ in range(n // 2 + 1)]
        # 设定初值, 长度为零时, 只有 0 存在
        dp[0][0] = True

        # 状压dp
        # 如果 dp[cnt-1][x-num] 存在, 则 dp[cnt][x] 也一定存在
        for i in range(len(nums)):
            num = nums[i]
            for cnt in range(n // 2, 1 - 1, -1):  # 需要逆序长度更新, 否则当前元素nums[i]可能被使用多次
                for x in range(0, total + 1):
                    if x - num >= 0:
                        dp[cnt][x] |= dp[cnt - 1][x - num]

        for cnt in range(1, n // 2 + 1):
            # 枚举长度在 [1, n // 2] 内的所有子集
            if total * cnt % n == 0 and dp[cnt][total * cnt // n]:
                return True
        return False


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """
        状压dp滚动数组优化第一维版 + 哈希表, 类似官解二的dp做法, 耗时: 200ms
        相比上一个dp滚动数组优化第一维版:
        1. 把x的维度换成哈希表,
        2. 在状态递推过程中, 如果找到某个集合满足条件, 可直接返回 True
        3. 提前剪枝排除不成立的情况, 若找不到 0 < cnt <= n//2, s.t. total * cnt % n == 0, 返回 False
        """
        n = len(nums)
        total = sum(nums)

        # 提前剪枝排除不成立的情况
        if all(total * i % n != 0 for i in range(1, n // 2 + 1)):
            return False

        # 若集合 dp[cnt] 中存在 x,  表示数组nums[:i+1]中存在长度为cnt和为x的子集
        dp = [set() for _ in range(n // 2 + 1)]
        # 设定初值, 长度为零时, 只有 0 存在
        dp[0].add(0)

        # 状压dp
        # 如果 x 存在于 dp[cnt-1] 中, 则 x+num 也一定存在于 dp[cnt] 中
        for i in range(len(nums)):
            num = nums[i]
            for cnt in range(n // 2, 1 - 1, -1):  # 需要逆序长度更新, 否则当前元素nums[i]可能被使用多次
                for x in dp[cnt - 1]:
                    dp[cnt].add(x + num)

                # 如果存在长度为 cnt 的子集和为 total * cnt / n, 返回 True
                if total * cnt % n == 0 and total * cnt // n in dp[cnt]:
                    return True

        return False


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """
        状压dp滚动数组优化第一维版 + 整型位数组,  耗时: 50ms
        相比上一个哈希表优化x维版, 这个版本:
        1. 用一个整数(因为python整型无限长,可以看成一个位数组)代替一个哈希表, 第
        2. 这个版本和上一个哈希表的版本都是对上上一个版本: "状压dp滚动数组优化第一维版" 的优化, 对于上上版本更好理解此版本
        """
        n = len(nums)
        total = sum(nums)

        # 提前剪枝排除不成立的情况
        if all(total * i % n != 0 for i in range(1, n // 2 + 1)):
            return False

        # 若集合 dp[cnt] 中的第 x 位为真 ,  表示数组nums[:i+1]中存在长度为cnt和为x的子集
        dp = [0 for _ in range(n // 2 + 1)]
        # 设定初值, 长度为零时, 只有第 0 位存在
        dp[0] |= 0b001

        # 状压dp
        # 如果 dp[cnt-1] 的第 x 位存在(为1), 则 dp[cnt] 的第 x+num 位也为1
        for i in range(len(nums)):
            num = nums[i]
            for cnt in range(n // 2, 1 - 1, -1):
                # for x in range(0, total + 1):  # 需要逆序长度更新, 否则当前元素nums[i]可能被使用多次
                #     if x - num >= 0 and dp[cnt - 1] & (1 << (x - num)):
                #         dp[cnt] |= (1 << x)

                # 这个语句等价于上面三行
                dp[cnt] = dp[cnt] | (dp[cnt - 1] << num)

                # 如果存在长度为 cnt 的子集和为 total * cnt / n, 返回 True
                if total * cnt % n == 0 and dp[cnt] >> (total * cnt // n) & 1:
                    return True

        return False


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """
        状压dp + 整型位数组 + 滚动数组优化,  最佳耗时: 25ms
        相比上一个整型位数组优化x维版, 这个版本:
        1. 观察上一个版本的递归过程发现, 每次递推只用到了前后两项, 可用滚动数组优化,

        2. 但是滚动数组优化之后无法知道集合的长度, 故先像官解一那样对均值做一个归一化, 这样问题就等价于找和为零的非空子集, 再把归一化的数组按逆序排序

        3. 在 2. 的基础上, 我们要找一个和为零的非空子集, 可以在官解一对数组做均值归一化的基础上除以一个公共因子, 把这个数组尽可能地化小

        4. 同时在滚动更新 dp位数组(在python里本质是一个无限长的整数)时,
            如果 num < 0, 等价于 dp |= dp >> abs(num), 若 dp 中第 x 位为 1 (也即存在集合的和为x)
                1) 若 x+num >= 0, 步骤:"dp |= dp >> abs(num)" 对第 x 位的更新显然正确,
                2) 若 x+num < 0, 则加上当前的 num 会得到一个第'负数'位, 这个位对我们的结果没影响(逆序排序后之后的操作一定都是右移, '负数'位永远不可能作用到第 0 位)
                    故 x+num < 0 情况下舍去该位即可

        注:
        此版本代码主要参考原本某个大佬的代码:
            class Solution:
                def splitArraySameAverage(self, nums: List[int]) -> bool:
                    n, s = len(nums), sum(nums)
                    mul = n // gcd(n, s)
                    A = [num * mul - mul * s // n for num in nums]
                    st = 0
                    for x in sorted(A[:-1], reverse=True):
                        st |= (st | 1) << x if x >= 0 else st >> (-x)
                        if st & 1:
                            return True
                    return False

        """
        n = len(nums)
        total = sum(nums)

        # 提前剪枝排除不成立的情况
        if all(total * i % n != 0 for i in range(1, n // 2 + 1)):
            return False

        # 均值归零
        # 把数组化成均值为零的最简式(数组最大公约数为1)
        for i in range(n):
            nums[i] = (nums[i] * n - total)
        # 找数组的最大公约数
        factor = nums[0]
        for i in range(len(nums)):
            if nums[i] == 0:
                return True
            factor = gcd(factor, nums[i])
        # 化成最简式
        nums = [n // factor for n in nums]

        # 降序排序数组, 前半部分为正, 后半为负
        nums.sort(reverse=True)

        # 若集合 dp 中的第 x 位为真 ,  表示数组nums[:i+1]中存在长度为cnt和为x的子集
        # dp = [0 for _ in range(n // 2 + 1)]
        # 设定初值, 长度为零时, 只有第 0 位存在
        dp = 0b000

        # 状压dp
        # 如果 dp[cnt-1] 的第 x 位存在(为1), 则 dp[cnt] 的第 x+num 位也为1
        for i in range(len(nums) - 1):
            num = nums[i]
            # 滚动更新
            if num >= 0:
                dp |= ((dp | 0b001) << num)
            else:
                dp |= (dp >> -num)

            # 如果存在长度为非空子集和为 0, 返回 True
            if dp & 1:
                return True

        return False

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """ 折半枚举, 时间复杂度: n*2^(n/2), 空间复杂度: 2^(n/2) """
        if len(nums) <= 1:
            return False
        n = len(nums)
        total = sum(nums)

        dcnt_tol = defaultdict(set)
        # 枚举前 2 ** (n/2), 记录所有的 (lcnt, ltol) 对
        nl = n // 2
        for i in range(1 << (nl)):
            cnt, tol = 0, 0
            for k in range(nl):
                if i >> k & 1:
                    tol += nums[k]
                    cnt += 1
            dcnt_tol[cnt].add(n * tol)

        # 枚举后一半数组的 (tol, cnt)
        # nl = n//2
        for i in range(1 << (n - nl)):
            cnt, tol = 0, 0
            for k in range(n - nl):
                if i >> k & 1:
                    tol += nums[nl + k]
                    cnt += 1
            rcnt, rtol = cnt, tol
            # if i == 0b001:
            #     print(i)

            # 枚举查找是否存在: (ltotal + rtotal) / (lcnt + rcnt) = total / n
            # 等价于: (ltotal + rtotal) * n = total * (lcnt + rcnt)
            #        ltotal * n = total * (lcnt + rcnt) - rtotal * n
            for lcnt in dcnt_tol:
                if total * (lcnt + rcnt) - rtol * n in dcnt_tol[lcnt]:
                    if (lcnt + rcnt) in {0, n}:  # 所选元素不可全选, 不可不选
                        # print(cnt, cnt1)
                        pass
                    else:
                        return True

        return False


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """ 回溯 + 剪枝, 卡时间ac, 时空复杂度爆炸高 """
        n = len(nums)
        total = sum(nums)
        nums.sort(reverse=True)

        # 利用结论剪枝, psum 一定是整数, 若不存在, 直接返回 False
        if all(total * i % n != 0 for i in range(1, n // 2 + 1)):
            return False

        @cache
        def dfs(i, psum, cnt):

            if 0 < cnt < n and psum * (n - cnt) == (total - psum) * cnt:
                return True

            elif cnt > n // 2:
                return False

            if i >= n:
                return False

            for j in range(i, n):
                if dfs(j + 1, psum + nums[j], cnt + 1):
                    return True

            return False

        return dfs(0, 0, 0)

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """
        状压dp + 整型位数组 + 滚动数组优化 + 折半查找,  最佳耗时: 30ms
        相比之前的: "状压dp + 整型位数组 + 滚动数组优化"(以下称做上一个版本), 这个版本:
        1. 借鉴了折半查找的思想, 在上一个版本中, 我们用一个很长的 dp 滚动数组来标识子集合的和有哪些值
        2. 在这个版本中同样采用之前的 dp 滚动数组表示方式, 数组均值归零化简操作, 和降序排列操作
        3. 不同的是, 针对数组的前 n//2 个元素, 我们用状压滚动位数组的方式得到一个很长的位数组, 里面标识了前半部分的子集合的和有哪些取值,
            可以知道的是, 左半数组的子集合的和一定是大于等于零的, 若左半出现了和小于零的子集合(则右半一定全是小于零的), 丢弃该位即可.
            这样我们得到了左半的子集合的和的可能取值: dpl, 若 dpl 的第 x 位为 1, 则存在和为 x 的子集合.

            同样的, 对右半数组也采用同样的方式(逆序遍历)用状压滚动位数组的方式得到一个很长的位数组, 不过这里面的位标识的全部是子集合的和的相反数,
            同样如果右半出现了大于零的子集合(左半子集合一定全大于零), 丢弃即可.
            这样也得到了右半的子集合的和的可能取值: dpr, 若 dpr 的第 x 位为 1, 则存在和为 -x 的子集合.

        4. 最终, 比较 dpl & dpr 的值, 若为真, 则至少存在一对相反数(x,-x), 返回 True, 否则 False

        """
        n = len(nums)
        total = sum(nums)

        # 提前剪枝排除不成立的情况
        if all(total * i % n != 0 for i in range(1, n // 2 + 1)):
            return False

        # 均值归零
        # 把数组化成均值为零的最简式(数组最大公约数为1)
        for i in range(n):
            nums[i] = (nums[i] * n - total)
        # 找数组的最大公约数
        factor = nums[0]
        for i in range(len(nums)):
            if nums[i] == 0:
                return True
            factor = gcd(factor, nums[i])
        # 化成最简式
        nums = [n // factor for n in nums]

        # 降序排序数组, 前半部分为正, 后半为负
        nums.sort(reverse=True)

        # 若集合 dp 中的第 x 位为真 ,  表示数组nums[:i+1]中存在长度为cnt和为x的子集
        # dp = [0 for _ in range(n // 2 + 1)]
        # 设定初值, 长度为零时, 只有第 0 位存在
        dp = 0b000

        # 状压dp
        # 如果 dp[cnt-1] 的第 x 位存在(为1), 则 dp[cnt] 的第 x+num 位也为1
        for i in range(len(nums) // 2):
            num = nums[i]
            # 滚动更新
            if num >= 0:
                dp |= ((dp | 0b001) << num)
            else:
                dp |= (dp >> -num)
            # 如果存在长度为非空子集和为 0, 返回 True
            if dp & 1:
                return True
        dpl = dp

        dpr = 0b000
        for i in range(len(nums)-1, len(nums) // 2 -1, -1):
            num = nums[i]
            if num <= 0:
                dpr |= ((dpr | 0b001) << -num)
            else:
                dpr |= (dpr >> num)
            # 如果存在长度为非空子集和为 0, 返回 True
            if dpr & 1:
                return True

            # 提前判断是否成功找到均值分划
            # state = (dpl & dpr)
            # if i == len(nums) // 2:  # 若遍历完右半整个数组, 必须至少两位相同, 因为有1位一定相同
            #     # 清除一位
            #     state &= (state - 1)
            # if state:  # 可检测是否存在相反数从而提前退出
            #     return True

        state = (dpl & dpr)
        return bool(state & state-1)
        # return False

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
