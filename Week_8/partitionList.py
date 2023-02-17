# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerHead = smallerList = ListNode(0)
        largerHead = largerList = ListNode(0)
        while head:
            if head.val<x:
                smallerList.next=head
                smallerList = smallerList.next  
            else:
                largerList.next = head
                largerList = largerList.next
            head = head.next

        smallerList.next = largerHead.next
        largerList.next = None

        return smallerHead.next   
