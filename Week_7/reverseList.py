class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        while head != None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

