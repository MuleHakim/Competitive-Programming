# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(left - 1):
            p = p.next
        cur, prev = p.next, None

        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        p.next.next = cur
        p.next = prev

        return dummy.next
