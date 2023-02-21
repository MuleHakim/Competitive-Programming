# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1 = l1
        cur_l2 = l2
        extra = 0
        while cur_l1 and cur_l2:
            total = cur_l1.val + cur_l2.val + extra
            extra = total // 10
            rem = total % 10
            cur_l1.val = rem
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
            
        cur = l1
        while cur.next:
            cur = cur.next
            
        while cur_l2:
            rem = (cur_l2.val + extra) % 10
            extra = (cur_l2.val + extra) // 10
            cur.next = ListNode(rem)
            cur = cur.next
            cur_l2 = cur_l2.next

        while cur_l1:
            cur_l1.val += extra
            extra = cur_l1.val // 10
            rem = cur_l1.val % 10
            cur_l1.val = rem
            cur_l1 = cur_l1.next
            
        extra_node = ListNode(extra)
        cur = l1
        if extra != 0:
            while cur.next:
                cur = cur.next
            cur.next = extra_node
            return l1
            
        return l1
