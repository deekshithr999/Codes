

'''
def heapify(heap):
    idx=len(heap)-1
    if len(heap)==1:
        return 0
    
    while idx>=0:
        parent = int((idx-1)/2)
        if heap[parent]<heap[idx]:
            heap[parent],heap[idx]=heap[idx],heap[parent]
            idx=parent
        else:
            break




if __name__=="__main__":
    
    lst=list(map(int,input("Enter the numbers :").split()))

    heap =[]

    for num in lst:
        heap.append(num)
        heapify(heap)
        print ("Heapified : ",heap)
    
    print("Finally ", heap)

'''

#########################################################


class Heap :
    
    def __init__(self):
        self.heap=[]
    
    def __init__(self,lst):
        self.heap=lst
    

    def heapify(self,idx):

        if idx <1:
            return
        
        while idx>0:

            parent = int((idx-1)/2)

            if self.heap[parent]<self.heap[idx]:
                self.heap[parent],self.heap[idx]=self.heap[idx],self.heap[parent]
                idx = parent
            
            else:
                break
    
    def full_heapify(self):
        print("Fully heapifying")
        l =len(self.heap)

        for i in range(l):
            self.heapify(i)
            print("idx : ",i,self.heap)


lst =list(map(int, input("Enter nums : ").split()))

heap_inst = Heap(lst)
heap_inst.full_heapify()
print ("lst : ",lst)



