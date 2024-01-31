class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' -> '
                
            temp_node = temp_node.next
        return result
        #return f"{self.prev}<-{self.value}->{self.next}"
        
    def append(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = None    # not needed, coming from Node definition
            new_node.prev = None    # not needed, coming from Node definition
        else:
            #current = self.head
            #while current:
            #    current = current.next
            #self.tail = new_node
            
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None
        
        self.length += 1
        
            
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
        else:
            current = self.head
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node                 
            self.head = new_node
            
        self.length += 1
          
            
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
                 
    def reverse(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
        
    
    def search(self, target):
        if self.length == 0:
            return False
        else:
            index = 0
            current = self.head
            while current:
                if target == current.value:
                    break
                else:
                    current = current.next
                    index += 1
                
            return (index, current.value)
         
    
    def get(self, index):
        if index == -1:
            return self.tail
        
        if self.length == 0:
            return self.head
        
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
            
        return current_node
             
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            current = self.head
            for _ in range(index):
                current = current.next
            current.value = value
            
        return True

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
    
        #    if self.length == 0:             
        #        self.head = new_node
        #        self.tail = new_node
        #        new_node.next = None
        #        new_node.prev = None
        #    else:
        #        new_node.next = self.head
        #        new_node.prev = None
        #        self.head = new_node
        #else:
        prev_node = self.get(index-1)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
            
        self.length += 1
        
        return 
                            
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next.prev = None
            popped_node.next = None
        
        self.length -= 1
        
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.pop_first()
        else: 
            popped_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
            popped_node.next = None
            
        return popped_node
    
    
    def remove(self, index):
        if self.length == 0:
            return False
        elif index == 0 and self.length == 1:
            self.pop()
            return
        elif index == 0 and self.length > 1:
            self.pop_first()
        else:
            prev_node = self.get(index -1)
            removed_node =  prev_node.next
            prev_node.next = removed_node.next
            removed_node.next.prev = prev_node
            removed_node.next = None
            removed_node.prev = None
        
        self.length -= 1
        
        return True
        
    
new_node = DoublyLinkedList()
print(new_node) #<class '__main__.DoublyLinkedList'>

new_node.append(10)
new_node.append(22)
new_node.append(34)

print(new_node) #10 -> 22 -> 34

new_node.prepend(21)
new_node.prepend(90)
print(new_node) #90 -> 21 -> 10 -> 22 -> 34

new_node.traverse()    
#90
#21
#10
#22
#34         

print("Printing the list in reverse direction")
new_node.reverse()       
#34
#22
#10
#21
#90

print(new_node.search(21))  #(1, 21)

print(new_node.get(3).value)  # 22
print(new_node.get(0).value)  # 90
print(new_node.get(1).value)  # 21

new_node.set_value(2, 45)
print(new_node)

new_node.insert(0,31)
new_node.insert(5,55)
print(new_node) #31 -> 90 -> 21 -> 45 -> 22 -> 55 -> 34

new_node.pop_first()
print(new_node) #90 -> 21 -> 45 -> 22 -> 55 -> 34
new_node.pop_first()
print(new_node) #90 -> 21 -> 45 -> 22 -> 55 -> 34

new_node.pop()
print(new_node) #21 -> 45 -> 22 -> 55
new_node.pop()
print(new_node) #21 -> 45 -> 22

new_node.remove(1)
print(new_node) #21 -> 22

new_node.remove(0)
print(new_node) #22














    
    