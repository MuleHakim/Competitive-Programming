# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0)
        cur = head
        while cur:
            temp = cur.next
            prev = result
            while prev.next:
                if prev.next.val > cur.val:
                    break
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
            cur = temp
        return result.next