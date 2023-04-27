question_content = """
给你一个链表数组，每个链表都已经按升序排列。 

 请你将所有链表合并到一个升序链表中，返回合并后的链表。 

 

 示例 1： 

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
 

 示例 2： 

输入：lists = []
输出：[]
 

 示例 3： 

输入：lists = [[]]
输出：[]
 

 

 提示： 

 
 k == lists.length 
 0 <= k <= 10^4 
 0 <= lists[i].length <= 500 
 -10^4 <= lists[i][j] <= 10^4 
 lists[i] 按 升序 排列 
 lists[i].length 的总和不超过 10^4 
 

 Related Topics 链表 分治 堆（优先队列） 归并排序 👍 2411 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(l1, l2):
            """ 合并升序链表 """
            dummy = ListNode(None, l2)
            out = dummy
            cur1 = l1
            cur2 = l2
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    out.next = cur1
                    cur1 = cur1.next
                else:
                    out.next = cur2
                    cur2 = cur2.next
                out = out.next
            if cur1:
                out.next = cur1
            else:
                out.next = cur2
            return dummy.next

        def sort_list(li):
            if not li:
                return li
            sort_list(li.next)
            l, r = li, li.next
            l.next = None
            ans = merge(l, r)
            return ans
        def merge_lists(lists):
            ans = lists[0]
            for l in lists[1:]:
                ans = merge(ans, l)
            return ans
        def dfs(l, r):
            if r - l == 1:
                return lists[l]
            mid = l + r >> 1
            rl = dfs(l, mid)
            rr = dfs(mid, r)
            return merge(rl, rr)

        # ans = sort_list(lists)
        # ans = merge_lists(lists)
        ans = dfs(0, len(lists))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
