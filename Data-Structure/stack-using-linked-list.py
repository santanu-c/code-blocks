class Node:
    def __init__(self, value):
        self.value = value
        self.next = next
        
   
class LinkedList:
    def __init__(self):
        self.head = None   
    
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
            

class Stack:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)
           
    def isEmpty(self):
        if self.linkedList.head:
            return False
        else: 
            return True
    
    def push(self, value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue =  self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodeValue
            
    def peek(self):
       if self.isEmpty():
           return "Stack is empty"
       else:
           return self.linkedList.head.value

    def delete(self):
        self.linkedList.head = None
        
            

customStack = Stack()
print(customStack.isEmpty())    #True

customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)  # 
#3
#2
#1

print("-------")    # -------
customStack.peek()  #2
customStack.pop()   #1
print(customStack) #
#2
#1




    