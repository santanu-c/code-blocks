class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []
        
    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list:
            return False
        else:
            return True
    
    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
        
    def push(self, value):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(value)
            return "Element pushed successfully"
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[len(self.list) - 1]
            

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)



    

        