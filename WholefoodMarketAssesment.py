#Assesment from WholeFoods Market that invloved dealing with queues which have values and prioritys
class PriorityQueue:
    def __init__(self):
        self.size = 0
        self.q = []
        
    def enqueue(self, value, priority):
        if self.size >= 5:
            self.q.sort()
            if self.q[-1] < priority:
                self.q.pop()
                self.q.append((value,priority))
                
        self.q.append((value,priority))
        self.size += 1
        
    def dequeue(self):
        if self.size == 0:
            return
        self.q.pop()
        self.size -= 1
        
    def print(self):
        self.q.sort()
        for tuple in self.q:
            print(tuple)
        
    
        
PQ = PriorityQueue()

PQ.enqueue(5,2)
PQ.enqueue(6,1)
PQ.enqueue(7,-1)
PQ.enqueue(3,0)
PQ.dequeue()
PQ.dequeue()
PQ.enqueue(8,3)
PQ.print()

            
        
    
    