class Queue:
    def __init__(self):
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
    
    def enque(self, value):
        self.list.append(value)
        return "value enqueued successfully"
    
    def deque(self):
        if self.isEmpty():
            return "Q is empty"
        else:
            return self.list.pop(0)
        
    def delete(self):
        self.list = []
    
    
    def peek(self):
        if self.isEmpty():
            return "Q is Empty"
        else:
            return self.list[len(self.list)-1]
    

customQ = Queue()
print(customQ.isEmpty())
customQ.enque(1)
customQ.enque(2)
customQ.enque(3)
print(customQ)
print("-------")
print(customQ.peek())
print(customQ.deque())
print("--------")
print(customQ)

#True
#3
#2
#1
#-------
#1
#3
#--------
#1
#2