
question_content = """
There is a room with n bulbs labeled from 1 to n that all are turned on 
initially, and four buttons on the wall. Each of the four buttons has a different 
functionality where: 

 
 Button 1: Flips the status of all the bulbs. 
 Button 2: Flips the status of all the bulbs with even labels (i.e., 2, 4, ...).
 
 Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...). 

 Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k = 0
, 1, 2, ... (i.e., 1, 4, 7, 10, ...). 
 

 You must make exactly presses button presses in total. For each press, you may 
pick any of the four buttons to press. 

 Given the two integers n and presses, return the number of different possible 
statuses after performing all presses button presses. 

 
 Example 1: 

 
Input: n = 1, presses = 1
Output: 2
Explanation: Status can be:
- [off] by pressing button 1
- [on] by pressing button 2
 

 Example 2: 

 
Input: n = 2, presses = 1
Output: 3
Explanation: Status can be:
- [off, off] by pressing button 1
- [on, off] by pressing button 2
- [off, on] by pressing button 3
 

 Example 3: 

 
Input: n = 3, presses = 1
Output: 4
Explanation: Status can be:
- [off, off, off] by pressing button 1
- [off, on, off] by pressing button 2
- [on, off, on] by pressing button 3
- [off, on, on] by pressing button 4
 

 
 Constraints: 

 
 1 <= n <= 1000 
 0 <= presses <= 1000 
 

 Related Topics 位运算 深度优先搜索 广度优先搜索 数学 👍 169 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # 本题中, 取大于等于3个灯泡均可得出正确答案
        max_bulbs = 3
        if n > max_bulbs:
            n = max_bulbs

        def binaryList2int(binary: List):
            """ Binary List to int. For example: [0, 1, 0, 1] -> 0b1010 . """
            a = 0
            for i in range(len(binary)):
                a |= (binary[i] != 0) << i
            return a

        # 用来记录最终的灯泡状态
        allstatus = set()

        # button对灯泡的作用效果, 取4个灯泡
        # buttons = [binaryList2int(btn) for btn in [[1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1]]]  # 此例为了测试
        # buttons = [0b1111, 0b1010, 0b0101, 0b1001]
        func = [lambda x: 1, lambda x: int(x % 2 == 1), lambda x: int(x % 2 == 0), lambda x: int(x % 3 == 0)]
        buttons = [binaryList2int([func[btn](i) for i in range(n)]) for btn in range(len(func))]

        # btn_down_cnt 为按下的button总数, 也就是 state 中为1的bit个数
        def btn_down_cnt(state: int):
            """ 返回state中bit位为1的个数"""
            return sum([(state >> i) & 1 for i in range(len(buttons))])
        # 筛选出可能的按钮状态
        button_state = [
            state for state in range(16) if (btn_down_cnt(state) % 2 == presses % 2) and (btn_down_cnt(state) <= presses)
        ]

        # state用4位表示button是否按下.
        # 由于按钮按下后可以按回, 所以按下的button数量必定小于按动总数: presses
        # 并且其奇偶性应一致:
        #   presses % 2 == btn_down_cnt % 2 and presses <= btn_down_cnt
        #   其中, btn_down_cnt(state) 为按下的button总数,
        #   且 btn_down_cnt(state) = sum([(state >> i) & 1 for i in range(len(button))])

        """ 
        约定按下的按钮总数为k(k=0,1,2,3,4), 按钮状态记为: state[k], 则共有16种情况:
        
        k=0, 1种: state[0] = [0b000]
        k=1, 4种: state[1] = [0b1000, 0b0100, 0b0010, 0b0001]
        k=2, 6种: state[2] = [0b1100, 0b1010, 0b1001, 0b0110, 0b0101, 0b0011]
        k=3, 4种: state[3] = [0b1110, 0b1101, 0b1011, 0b0111]
        k=4, 1种: state[4] = [0b1111]
        
        考虑到按钮按下后可以再按一次恢复原状, 则:
        state'[0] = state[0]
        state'[1] = state[1]
        state'[2] = state[2] + state[0]
        state'[3] = state[3] + state[1]
        state'[4] = state[4] + state[2] + state[0]
        
        综上:
            state'[k] = [(btn_down_cnt % 2 == k % 2) and (btn_down_cnt <= k) for state in range(16)]
            其中, btn_down_cnt 为按下的button总数, 也就是 state 中为1的bit个数
        计算方式为: btn_down_cnt = sum([(state >> i) & 1 for i in range(len(button))])
        """

        # 对于不同中可能的button的按下状态, 计算其作用后的灯泡亮灭结果
        for state in button_state:
            # bulb初始状态全黑
            bulbs = 0  # 0b0000..00
            for i, btn in enumerate(buttons):
                # 若该button按下, 则根据该button的作用效果翻转灯泡
                if (state >> i) & 1:
                    bulbs ^= btn
            # 记录button按过后的灯泡状态
            allstatus.add(bulbs)

        # 返回结果数量
        return len(allstatus)
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
