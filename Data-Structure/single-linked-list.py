class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:  # Not used
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail - new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        

class EmptyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
            
        return result
        
        
    # TC = O(1), SC = O(1)
    def append(self, value):  
        new_node = Node(value) 
        if self.head is None: 
            self.head = new_node 
            self.tail = new_node  
        else:
            self.tail.next = new_node  
            self.tail = new_node   
                
        self.length += 1
    
    
    # TC = O(1), SC = O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        
    
    #
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False  # designed by choisce to return False
        elif self.length == 0:  ## ccovers emplty link list
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            
        self.length += 1
        return True
         
         
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


    def search(self, target):
        current = self.head # we are starting from first node
        index = 0
        while current:
            if current.value == target:
                index += 1
                return (index,current.value)
            current = current.next
        
        return False
    
    
    def get(self, index): # this is get the value at index
        if index == -1: # let's say want to return the tail for index=-1
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.value
    
    def set_value(self, index, value):
        temp = self.get(index) # retrieving the value at index, not used 
        if temp:
            #print(temp)
            current = self.head
            for _ in range(index):
                current = current.next
                
            current.value = value
            # temp.value = value  ## not working
            return True
        
        return False  # just to return false we used temp
        
    def pop_first(self):
        if self.length == 0:
            return None
        
        popped_node = self.head
        if self.length == 1: # if there is one element
            self.head = None
            self.tail = None   
        else:            
            self.head = self.head.next
            popped_node.next = None
            
        self.length -= 1
          
        return popped_node
        
    
    def pop(self):
        if self.length == 0:
            return None
        
        popped_node = self.tail
        
        if self.length == 1:
            self.head = self.tail = None

        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        
        self.length -= 1
        return popped_node
        
    def remove(self, index):
        if index >= self.length or index <  -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1 or index == -1:
            return self.pop()
        
        prev_node = self.get(index -1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        
        return popped_node
        
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
#new_linnked_list = LinkedList(10)
#print(new_linnked_list.head.value)
#print(new_linnked_list.tail.value)
#print(new_linnked_list.length)


empty_new_linked_list = EmptyLinkedList()
empty_new_linked_list.append(10)
empty_new_linked_list.append(20)
empty_new_linked_list.prepend(50) 
# Inserting at the begining
empty_new_linked_list.insert(1,100) # 50 -> 100 -> 10 -> 20
print(empty_new_linked_list)
# Inserting at negetive index ignores insertion request
empty_new_linked_list.insert(-1,900) # 50 -> 100 -> 10 -> 20

##
print(empty_new_linked_list)
empty_new_linked_list.traverse()

(i,v) = empty_new_linked_list.search(10)
if v:
    print("Found target %s at index %s" %(v,i))


print(empty_new_linked_list.get(3))
#print(empty_new_linked_list.get(-1))
print(empty_new_linked_list.get(20))  ## Prints None

empty_new_linked_list.set_value(1,99)
print(empty_new_linked_list)  # 50 -> 99 -> 10 -> 20

empty_new_linked_list.pop_first()
print(empty_new_linked_list)  # 99 -> 10 -> 20

empty_new_linked_list.pop()
print(empty_new_linked_list) # 99 -> 10

empty_new_linked_list.remove(1)
print(empty_new_linked_list) # 99

empty_new_linked_list.delete_all()
print(empty_new_linked_list)
