# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        res = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur, prev = slow, None
        while cur: 
            temp = cur 
            cur = cur.next
            temp.next = prev
            prev = temp

        left, right = head, prev
        while right:
            res = max(res, left.val + right.val)  
            right = right.next 
            left = left.next

        return res