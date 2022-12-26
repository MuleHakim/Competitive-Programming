def printList():
    print(listOfCommands)
def appendList(value):
    listOfCommands.append(value)
def removeElement(value):
    listOfCommands.remove(value)
def insertElement(value,index):
    listOfCommands.insert(value,index)
def sortList():
    listOfCommands.sort()
def popLastElement():
    listOfCommands.pop()
def reverse():
    listOfCommands.reverse()
if __name__ == '__main__':
    N = int(input())
    listOfCommands = []
    while N>0:
        command = list(map(str,input().split()))
        if command[0] == "print":
            printList()
        elif command[0] == "append":
            appendList(int(command[1]))
        elif command[0] == "insert":
            insertElement(int(command[1]),int(command[2]))
        elif command[0] == "remove":
            removeElement(int(command[1]))
        elif command[0] == "sort":
            sortList()
        elif command[0] == "pop":
            popLastElement()
        else:
            reverse()
        N -= 1
