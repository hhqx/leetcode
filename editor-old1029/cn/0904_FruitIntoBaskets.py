
question_content = """
You are visiting a farm that has a single row of fruit trees arranged from left 
to right. The trees are represented by an integer array fruits where fruits[i] 
is the type of fruit the iᵗʰ tree produces. 

 You want to collect as much fruit as possible. However, the owner has some 
strict rules that you must follow: 

 
 You only have two baskets, and each basket can only hold a single type of 
fruit. There is no limit on the amount of fruit each basket can hold. 
 Starting from any tree of your choice, you must pick exactly one fruit from 
every tree (including the start tree) while moving to the right. The picked fruits 
must fit in one of your baskets. 
 Once you reach a tree with fruit that cannot fit in your baskets, you must 
stop. 
 

 Given the integer array fruits, return the maximum number of fruits you can 
pick. 

 
 Example 1: 

 
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
 

 Example 2: 

 
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
 

 Example 3: 

 
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

 
 Constraints: 

 
 1 <= fruits.length <= 10⁵ 
 0 <= fruits[i] < fruits.length 
 

 Related Topics 数组 哈希表 滑动窗口 👍 272 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        basket = defaultdict(int)

        cnt = 0
        ansMax = float('-inf')
        left, right = 0, 0
        while right < len(fruits):
            if len(basket.keys()) < 2 or fruits[right] in basket.keys():
                basket[fruits[right]] += 1
                right += 1
                cnt += 1
                ansMax = max(ansMax, cnt)
                continue

            if len(basket.keys()) == 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1
                cnt -= 1
                continue

            right += 1

        return ansMax

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        basket = defaultdict(int)

        cnt = 0
        ansMax = float('-inf')
        left, right = 0, 0
        while right < len(fruits):
            if len(basket.keys()) < 2 or fruits[right] in basket.keys():
                basket[fruits[right]] += 1
                right += 1
                cnt += 1
                ansMax = max(ansMax, cnt)
                continue

            if len(basket.keys()) == 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1
                cnt -= 1
                continue

            right += 1

        return ansMax
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
