import time

class BST:
    # Class BST that holds integers
    
    def __init__(self):
        self.data = []
        
    def appendData(self, item):
        self.data.append(item)
    
    def sort(self):
        self.data.sort()
        
    def timedFind(self, item):
        # measured in nanoseconds
        print(self.data)
        start = time.time_ns()
        index = self.find(item)
        end = time.time_ns()
        print(end - start)
        return index
    
    def find(self, item):
        return self.findNode(item)
            
    def findNode(self, item, startpoint=None, endpoint=None):
        if not startpoint:
            startpoint = 0
        if not endpoint:
            endpoint = len(self.data) - 1
        
        # // divides, then floors the value
        midpoint = (endpoint + startpoint) // 2
        
        if item == self.data[midpoint]:
            # return index of the item found
            return midpoint
        elif item < self.data[midpoint]:
            # item is below the midpoint
            return self.findNode(item, 0, midpoint)
        elif item > self.data[midpoint]:
            # item is above the midpoint
            return self.findNode(item, midpoint, endpoint)
        else:
            print("Comparison is incorrect - I think")
            return None
            
bst = BST()
for x in range(100000):
    bst.appendData(x)
    
bst.sort()
idx = bst.timedFind(2784)
print(idx)