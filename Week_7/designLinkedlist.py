class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        if self.head==None:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
    
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        newNode = Node(val)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
