class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child_(self, index):
        return 2 * index + 2  

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            pos = self._parent(current)
            # if self.heap[pos] > value:
            #     return False
            
            self._swap(pos,current)
            current = pos

    def sinkdown(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child_(index)

            if (left_index < len(self.heap)) and self.heap[max_index] < self.heap[left_index]:
                max_index = left_index

            if (right_index < len(self.heap)) and self.heap[max_index] < self.heap[right_index]:
                max_index = right_index

            
            if max_index != index:
                self._swap(max_index, index)  
                index = max_index

            else:
                 return    

            
       

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max = self.heap[0]
        self.heap[0] = self.heap.pop()        
        self.sinkdown(0)


myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)

myheap.remove()

print(myheap.heap)