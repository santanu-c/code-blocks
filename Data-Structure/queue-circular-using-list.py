class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def enque(self, value):
        if self.isFull():
            return "Q is full"
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return "Enqueu waqs successfull"
    

    def deque(self):
        if self.isEmpty():
            return "Q is empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return "Q is empty"
        else:
            return self.items[self.start]
            
    
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1
        
            
            

customQ = Queue(3)
customQ.enque(1)
customQ.enque(2)
customQ.enque(3)
print(customQ)
print(customQ.delete())
print(customQ.peek())
#1
#2
#3
#None
#Q is empty



                
                
        
    
            
    
    
        
    