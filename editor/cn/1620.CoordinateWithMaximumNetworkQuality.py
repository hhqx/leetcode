
question_content = """
You are given an array of network towers towers, where towers[i] = [xi, yi, qi] 
denotes the iᵗʰ network tower with location (xi, yi) and quality factor qi. All 
the coordinates are integral coordinates on the X-Y plane, and the distance 
between the two coordinates is the Euclidean distance. 

 You are also given an integer radius where a tower is reachable if the 
distance is less than or equal to radius. Outside that distance, the signal becomes 
garbled, and the tower is not reachable. 

 The signal quality of the iᵗʰ tower at a coordinate (x, y) is calculated with 
the formula ⌊qi / (1 + d)⌋, where d is the distance between the tower and the 
coordinate. The network quality at a coordinate is the sum of the signal qualities 
from all the reachable towers. 

 Return the array [cx, cy] representing the integral coordinate (cx, cy) where 
the network quality is maximum. If there are multiple coordinates with the same 
network quality, return the lexicographically minimum non-negative coordinate. 

 Note: 

 
 A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either: 
 

 
 x1 < x2, or 
 x1 == x2 and y1 < y2. 
 
 
 ⌊val⌋ is the greatest integer less than or equal to val (the floor function). 

测试用例:[[42,0,0]]
        7
测试结果:[42,0]
期望结果:[0,0]
 
 Example 1: 
 
 
Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
Output: [2,1]
Explanation: At coordinate (2, 1) the total quality is 13.
- Quality of 7 from (2, 1) results in ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
- Quality of 5 from (1, 2) results in ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
- Quality of 9 from (3, 1) results in ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
No other coordinate has a higher network quality. 

 Example 2: 

 
Input: towers = [[23,11,21]], radius = 9
Output: [23,11]
Explanation: Since there is only one tower, the network quality is highest 
right at the tower's location.
 

 Example 3: 

 
Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
Output: [1,2]
Explanation: Coordinate (1, 2) has the highest network quality.
 

 
 Constraints: 

 
 1 <= towers.length <= 50 
 towers[i].length == 3 
 0 <= xi, yi, qi <= 50 
 1 <= radius <= 50 
 

 Related Topics 数组 枚举 👍 60 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # get coords to search
        # coords = [(2, 1)]
        Min = towers[0][:2]
        Max = towers[0][:2]
        for x0, y0, q in towers:
            Min[0] = min(Min[0], x0)
            Min[1] = min(Min[1], y0)
            Max[0] = max(Max[0], x0)
            Max[1] = max(Max[1], y0)
        coords = ((x, y) for x in range(Min[0], Max[0]+1) for y in range(Min[1], Max[1]+1))

        # search all the coords
        ans = (float('inf'), 0, 0)
        for x, y in coords:
            val = 0
            for x0, y0, q in towers:
                r = sqrt((x-x0)**2 + (y-y0)**2)
                val += int(q / (r + 1)) if r <= radius else 0
            ans = min(ans, (-val, x, y))
        return list(ans[1:]) if ans[0] != 0 else [0, 0]
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
