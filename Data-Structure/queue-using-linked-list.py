class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
            
class Queue:
    def __init__(self):
        self.LinkList = Linkedlist()
    
    def __str__(self):
        values = [ str(x.value) for x in self.LinkList]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.LinkList.head:
            return False
        else:
            return True
        
    def enque(self, value):
        node = Node(value)
        if self.LinkList.head is None:  #first entry
            self.LinkList.head = node
            self.LinkList.tail = node
        else:
            #last_node = self.LinkList.tail
            #node.next = last_node
            #node.next = self.LinkList.tail
            self.LinkList.tail.next = node
            self.LinkList.tail = node
            
    
    def deque(self):
        if self.isEmpty():
            return "Q is empty"
        else:
            if self.LinkList.head == self.LinkList.tail:
                self.LinkList.head = None
                self.LinkList.tail = None
            else:              
                temp_node = self.LinkList.head
                self.LinkList.head = temp_node.next
                # OR  self.LinkList.head =  self.LinkList.head.next
                
            return temp_node    # no need to add .value as __str__ fun handles it
        
    
    def peek(self):
        if self.isEmpty():
            return "Q is full"
        else:
            return self.LinkList.head   # no need to add .value as __str__ fun handles it
    
    
    def delete(self):
        if self.LinkList.head:
            self.LinkList.head = None
            self.LinkList.tail = None
    
    
    
    
custQueue = Queue()
custQueue.enque(1)
custQueue.enque(2)
custQueue.enque(3)
print(custQueue)
print(custQueue.peek())
print(custQueue)

#1 2 3
#1
#1 2 3
        