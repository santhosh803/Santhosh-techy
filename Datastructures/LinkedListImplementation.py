class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data, None)
        node.next = self.head
        self.head = node
        
    def insertAt(self, index, data):
        if(self.head == None):
            self.insertAtBeginning(data)
            return
        
        node = Node(data, None);
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next
            count += 1

    def deleteAtBeginning(self):
        if(self.getLength() == 0):
            print('Linkedlist is empty, so nothing is there to delete')
            return
        
        self.head = self.head.next

    def deleteData(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if data == itr.next.data:
                itr.next = itr.next.next
                break
                
            itr = itr.next


    def deleteAt(self, index):
        if index >= self.getLength()-1 or index < 0:
            print('Invalid index')
            return
        
        if index == 0:
            self.deleteAtBeginning()

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def print(self):
        if(self.head == None):
            print('LinkedList is empty')
        
        itr = self.head
        while(itr):
            print(itr.data, '--->', end=" ")
            itr = itr.next
        
        print()

    def getLength(self):
        itr = self.head
        length = 0
        while(itr):
            length += 1
            itr = itr.next

        return length

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBeginning(5)
    ll.insertAtBeginning(4)
    ll.insertAtBeginning(3)
    ll.insertAtBeginning(2)
    ll.insertAtBeginning(1)
    ll.insertAt(2, 45)
    ll.insertAt(1, 100)
    ll.print()
    print(ll.getLength())
    ll.deleteAt(1)
    ll.print()
    ll.deleteData(4)
    ll.print()
    
