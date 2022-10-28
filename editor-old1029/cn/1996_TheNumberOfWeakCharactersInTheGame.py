
question_content = """
You are playing a game that contains multiple characters, and each of the 
characters has two main properties: attack and defense. You are given a 2D integer 
array properties where properties[i] = [attacki, defensei] represents the 
properties of the iᵗʰ character in the game. 

 A character is said to be weak if any other character has both attack and 
defense levels strictly greater than this character's attack and defense levels. 
More formally, a character i is said to be weak if there exists another character j 
where attackj > attacki and defensej > defensei. 

 Return the number of weak characters. 

 
 Example 1: 

 
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the 
other.
 

 Example 2: 

 
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a 
strictly greater attack and defense.
 

 Example 3: 

 
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a 
strictly greater attack and defense.
 

 
 Constraints: 

 
 2 <= properties.length <= 10⁵ 
 properties[i].length == 2 
 1 <= attacki, defensei <= 10⁵ 
 

 Related Topics 栈 贪心 数组 排序 单调栈 👍 157 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
def argsort(seq):
    return [x for x, y in sorted(enumerate(seq), key=lambda x: x[1], reverse=True)]


class Solution:

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # 根据两个属性进行排序
        properties.sort(key=lambda x: (x[0], x[1]))
        nums = [p[1] for p in properties]

        # 计算nums中有多少个元素在其右边能找到比他更大的, o(n^2) 复杂度, 应该有o(nlog(n))的方法查找
        cnt = 0
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i] and properties[j][0] > properties[i][0]:
                    cnt += 1
                    break

        isWeaker = [i for i in range(len(nums))]
        rank = argsort(nums)

        # large = rank[i]
        # small = rank
        # for i in range(len(rank)):
        #     large = rank[i]
        #     for small in isWeaker:
        #         pass
        return cnt


# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
