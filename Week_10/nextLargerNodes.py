# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next

        stack = []
        for idx, val in enumerate(res):
            while stack and res[stack[-1]] < val:
                res[stack.pop()] = val
            stack.append(idx)

        while stack:
            res[stack.pop()] = 0
        
        return res