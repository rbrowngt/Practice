class MaxHeap(object):
    """
    
    """
    def __init__(self, values = []):
        super(MaxHeap, self).__init__()
        self.heap = [0]
        for i in values:
            self.heap.append(i)
            self._bubbleUp(len(self.heap) - 1)
        
    def push(self, value):
        # append
        self.heap.append(value)
        # bubble up
        self._bubbleUp(len(self.heap) - 1)

    def pop(self, value):
        if len(self.heap) > 2:
            # swap first and last
            self._swap(1, len(self.heap - 1))
            maxVal = self.heap.pop()
            # bubble down
            self._bubbleDown(1)
        elif len(self.heap) == 2:
            maxVal = self.heap.pop()
        else:
            maxVal = None
        return maxVal
    
    def _bubbleUp(self, index):
        parent = index / 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._bubbleUp(parent)
            
    
    def _bubbleDown(self, index):
        left = index * 2
        right = (index * 2) + 1
        return None
    
    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]