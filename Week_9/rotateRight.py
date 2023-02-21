# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1

        if k == length: return head 
        iterate = 0
        if k > length:
            iterate = length - (k % length)
            if iterate == length: return head
            iterate -= 1 
        else:
            iterate = length - k - 1 

        cur = head
        for _ in range(iterate):
            cur = cur.next

        temp = cur.next
        rotate_ans = temp
        cur.next = None

        while temp.next:
            temp = temp.next
        temp.next = head

        return rotate_ans
