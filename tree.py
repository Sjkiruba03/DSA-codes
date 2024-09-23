class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if temp.value > new_node.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        
        while temp:
            # if temp.value == value:
            #     return temp.value
            # if temp.value > value:
            #     temp = temp.left
            # else:
            #     temp = temp.right  
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return temp          
            
        return False            
            
                     


bst = BinarySearchTree()
bst.insert(47)
bst.insert(40)
bst.insert(60)
print(bst.contains(4))
# print(bst.root.value,"root")
# print(bst.root.left.value,"left")
# print(bst.root.right.value,"right")
