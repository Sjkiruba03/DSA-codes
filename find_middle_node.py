class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
      
      
    def find_middle_node(self):
        one  = self.head
        two = self.head
        while two is not None and two.next is not None:
            one = one.next
            two = two.next.next
            print(one.value)
            print(two.value,"this\n\n")

        return one    
        
    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ######################################




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value,"middle value\n" )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""