class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_list(self):
        temp = self.top
        while temp:
            print(temp.value)    
            temp = temp.next

    def push(self, value):
        new_node = Node(value)  
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        Temp = self.top
        self.top = self.top.next
        Temp.next = None
        self.length -= 1
        return Temp
            
              

stack = Stack(7)
stack.push(8)
stack.pop()
stack.print_list()            