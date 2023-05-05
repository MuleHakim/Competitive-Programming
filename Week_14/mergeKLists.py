# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap,node.val)
                node = node.next

        ans = []
        while heap:
            ans.append(heapq.heappop(heap))

        head = ListNode(0)
        cur = head
        for i in range(len(ans)):
            cur.next = ListNode(ans[i]) 
            cur = cur.next
            
        return head.next