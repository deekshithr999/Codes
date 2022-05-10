'''
Algo to Sort heap in Ascending order

'''

class heapSort :

    def __init__(self,lst):
        self.heap = lst[:]
    
    def swap(self,idx1,idx2):
        self.heap[idx1],self.heap[idx2]= self.heap[idx2],self.heap[idx1]

    def heapify(self,idx):
        if idx <1:
            return
        parent = int((idx-1)/2)

        if self.heap[parent] < self.heap[idx]:
            self.swap(parent,idx)
            self.heapify(parent)
    
    
    def heapify_all(self):
        l =len(self.heap)
        for i in range(l):
            self.heapify(i)
    
    def heapSort (self):
        self.heapify_all()
        for i in range(len(self.heap)-1,0,-1):
            self.swap(0,i)
            self.heapify_top_to_down(i)


    def heapify_top_to_down(self,till):
        '''
            Take Care when there is only one element
            TC : O(nlogn) since iterating over the n elements and 
             Swapping takes O(logn)
        '''
        idx = 0
 
        while idx<till:
            swpwith = till
            print (idx)
            if 2*idx+1 <till:
                if 2*idx+2<till:
                    if self.heap[2*idx+1]<self.heap[2*idx+2]:
                        swpwith = 2*idx+2
                    else :
                        swpwith = 2*idx+1
                else :
                    if self.heap[2*idx+1]>self.heap[idx]:
                        swpwith = 2*idx+1
            
            if swpwith ==till:
                break
            self.swap(swpwith,idx)
            idx = swpwith

    def heapifytill(self,idx):
        for i in range(idx+1):
            self.heapify(i)
        
    def HeapSort2(self):
        print("fckk!!!")
        for i in range(len(self.heap)-1,0,-1):
            self.heapifytill(i)
            self.swap(0,i)

    
    def printHeap(self):
        print(self.heap)


                    
if __name__=="__main__":

    lst = list(map(int,input("Enter numbers").split()))
    hpsort =heapSort(lst)
    #hpsort.heapSort()
    hpsort.HeapSort2()
    hpsort.printHeap()

