class Node:
    def __init__(self, value):
        self.value = value
        self.next = None        
        

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next == self.head:
                break
            else:
                result += ' -> '
                temp_node = temp_node.next
                
        return result
        
            
    def append(self, value):
        new_node = Node(value)
        #if self.head is None:   # empty list
        if self.length == 0:    # empty list    
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:   # right most node in the list
            self.tail.next = new_node   # here self.tail means current node
            new_node.next = self.head
            self.tail = new_node
        
        self.length += 1
    

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node    # same as new_node.next = self.head
        else:
            temp_node = self.head
            self.head = new_node
            new_node.next = temp_node
            self.tail.next = new_node
        
        self.length += 1
        
    
    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                #self.head = new_node   bad order
                #new_node.next = self.head
                #self.tail.next = new_node
                
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node      
        elif index == self.length:  # inserting at last position
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
                
            new_node.next = temp_node.next
            temp_node.next = new_node
            
        self.length += 1       
        
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break
        
    
    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return (index, current.value)
            else:
                current = current.next
                index += 1
                
            if current == self.head:
                break
        return False    # if target not found
        
    
    def get(self, index):
        if index == -1:
            return self.tail.value
        if index < -1 or index > self.length:
            return False
        
        current = self.head
        for _ in range(index):
            current = current.next
            if current == self.head:
                break
                 
        return current
                
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            current = self.head
            for _ in range(index):
                current = current.next
            current.value = value
        else:
            return False
            
        return True
        
    
    def pop_first(self):
        if self.length == 0:
            return False
        else:
            popped_node = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            #self.head = popped_node.next
            # or better
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
            
        self.length -= 1
        
        return popped_node
        
    
    def pop(self):
        if self.length == 0:
            return None
        
        popped_node = self.tail
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
                
            current.next = None
            self.tail = current
            self.tail.next = self.head
            popped_node.next = None
        
        self.length -= 1
        
        return popped_node
    
    
    def remove(self, index):
        if self.length == 0:
            return False
        else:
            if index > self.length-1:
                return False
            elif index == 0:
                return self.pop_first()
            elif index  == -1 or index == self.length-1 :
                self.pop()
            else:
                prev_node = self.get(index-1)
                removed_node = prev_node.next
                prev_node.next = removed_node.next
                removed_node.next = None
        
        self.length -= 1
        
        return removed_node
                
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
            
    
    
new_node = CSLinkedList()

#new_node.next = new_node
#new_node.head = new_node
#new_node.tail = new_node
#new_node.length = 1

#print(new_node)
#print(new_node.length)
#print(new_node.head)
#print(new_node.tail)
# at this point there is no value unless you initialize the node with Node class
# so this is an empty linked list where head and tail points to None (you get a poiner to None object)

new_node.append(35)
new_node.append(40)
print(new_node) #35 -> 40

new_node.prepend(99)
print(new_node) #99 -> 35 -> 40

new_node.insert(0,9)
new_node.insert(1,55)
new_node.insert(3,22)   #9 -> 55 -> 99 -> 22 -> 35 -> 40
print(new_node) 

new_node.traverse() # 9
#55
#99
#22
#35
#40

print(new_node.search(45))  #99
print(new_node.search(22))  #22

print(new_node.get(4))  #35
print(new_node.get(-1)) #40
print(new_node.get(20)) #False

new_node.set_value(2, 67)
print(new_node) #9 -> 55 -> 67 -> 22 -> 35 -> 40

new_node.pop_first()
print(new_node) #55 -> 67 -> 22 -> 35 -> 40

new_node.pop()
print(new_node) #55 -> 67 -> 22 -> 35

new_node.pop()
print(new_node) #55 -> 67 -> 22

new_node.remove(1)
print(new_node) # 55 -> 22

new_node.delete_all()
print(new_node) # 

