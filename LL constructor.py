class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.value = value
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node  
        self.length += 1
        return True 
    
    def pop(self):
        if self.length == 0:
            return None 
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1 
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp 
     
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp 
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        # temp = self.head
        # for _ in range(index-1):
        #     temp = temp.next
        temp = self.get(index-1)
        new_node.next = temp.next    
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()

        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        

            

            




my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
# my_linked_list.print_list()
# print(my_linked_list.pop())
my_linked_list.prepend(5)
# print(my_linked_list.pop_first())          
# print(my_linked_list.get(2))
# my_linked_list.set_value(0,3)
# my_linked_list.insert(3,25)
# my_linked_list.remove(3)
my_linked_list.reverse()
my_linked_list.print_list()

