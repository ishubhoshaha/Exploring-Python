class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinearLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def addNode(self,data):
        newNode = Node(data)
        if self.head==None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
    def removeFromFront(self):
        try:
            temp = self.head
            self.head = temp.next
            self.size-=1
            del temp
        except Exception:
            print "List already empty"

    def getSize(self):
        return self.size

    def Traverse(self):
        temp = self.head
        while temp!=None:
            print temp.data,
            temp = temp.next

linkedlist = LinearLinkedList()
linkedlist.addNode(5)
linkedlist.addNode(8)
linkedlist.addNode(3)

print "Size of Current List: ",
print linkedlist.getSize()
print "Linked List contains: ",
linkedlist.Traverse()

linkedlist.removeFromFront()
# linkedlist.removeFromFront()
# linkedlist.removeFromFront()
# linkedlist.removeFromFront()
print "\nLinked List contains after removing",
linkedlist.Traverse()
print "\nSize of Current List: ",
print linkedlist.getSize()

