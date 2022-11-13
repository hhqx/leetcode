
question_content = """
符合下列属性的数组 arr 称为 山脉数组 ：

 
 arr.length >= 3 
 存在 i（0 < i < arr.length - 1）使得： 
 
 arr[0] < arr[1] < ... arr[i-1] < arr[i] 
 arr[i] > arr[i+1] > ... > arr[arr.length - 1] 
 
 

 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1]
 > ... > arr[arr.length - 1] 的下标 i 。 

 

 示例 1： 

 
输入：arr = [0,1,0]
输出：1
 

 示例 2： 

 
输入：arr = [0,2,1,0]
输出：1
#  

 示例 3： 

 
输入：arr = [0,10,5,2]
输出：1
 

 示例 4： 

 
输入：arr = [3,4,5,1]
输出：2
 

 示例 5： 

 
输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2
 

 

 提示： 

 
 3 <= arr.length <= 10⁴ 
 0 <= arr[i] <= 10⁶ 
 题目数据保证 arr 是一个山脉数组 
 

 

 进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？ 

 Related Topics 数组 二分查找 👍 312 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def triple_search(arr):
            """
            0.618法找极值点, 循环更新原则是更新之后区间[l,r]内必然不单调

            在数轴上, 有这样四个区间端点: l < ll < rr < r, 且 ll-l = r-rr = fix(0.618*(r-l))
            每次循环的目的是为了确定 [l,ll] 和 [rr, r] 哪个区间是严格单调的, 是则删除该区间,
            这样才能保证更新完成之后的 [l', r'] 区间一定包含极值点(非单调)

            假设我们要找区间 [l,r] 内 f(x) 的极大值点(单峰), 即有存在一点 i, s.t. [l, i]单增, [i,r]单减
            我们一共有四个区间端点: l < ll < rr < r, 三个区间: [l, ll], [ll, rr], [rr, r]

            下面讨论不同情况怎么确定 [l,ll] 和 [rr, r] 哪个区间是严格单调的
                (1) 若 f(ll) == f(rr), 由于相邻的 f(i) != f(i+1) 显然峰值应该 [ll, rr] 区间内
                此时更新, l' = ll, r' = rr, 同时删除 [l,ll] 和 [rr, r].

                (2) 若 f(ll) < f(rr), 则 [ll, rr] 不可能属于 [i,r] 单减区间, 且 rr < r, 所以 ll < i;
                此时 [l, ll) 区间必然单调, 可以删去, 即 =>  l' = ll

                (3) 若 f(ll) > f(rr), 则 [ll, rr] 不可能属于 [l,i] 单增区间, 且 l < ll, 所以 i < rr;
                此时更新 r' :  r' = rr

            """
            l, r = 0, len(arr) - 1

            while r - l + 1 > 3:
                delta = int((r - l) * 0.382)
                ll, rr = l + delta, r - delta
                if arr[ll] == arr[rr]:
                    l = ll
                    r = rr
                elif arr[ll] < arr[rr]:
                    # 此时[l, ll]区间单调, 故删去[l, ll)
                    l = ll
                else:
                    r = rr

            return (l + r) // 2

        return triple_search(arr)
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
