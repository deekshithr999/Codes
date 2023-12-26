import heapq


class MinHeap:
    def __init__(self):
        self.heap = []
    
    def printHeap(self):
        print("MinHeap :", self.heap)

    def insert(self, val):
        self.heap.append(val)
        idx = len(self.heap)-1
        self.heapify(len(self.heap)-1)
        # self.printHeap()
        
    def heapifyTopToBottom(self, par):
        print("par ", par)

        lc,rc = (2*par+1)//2, (2*par+2)//2
        smallest = par
        if rc < len(self.heap) and self.heap[rc] <self.heap[smallest]:
            smallest = rc
        if lc < len(self.heap) and self.heap[lc]< self.heap[smallest]:
            smallest = lc
        
        if smallest != par:
            self.heap[smallest], self.heap[par]= self.heap[par], self.heap[smallest]
            self.heapifyTopToBottom( smallest)
    
    def heapifyUsingToptoBottom(self,lst):
        self.heap=lst
        print("heree")
        for i in range(len(lst)-1,-1,-1):
            print("i ", i)
            self.heapifyTopToBottom(i)
    


    def heapifyBottomToTop(self, lst):
        self.heap= lst
        for i in range(len(self.heap)):
            self.heapify(i)

    def heapify(self, idx):
        '''
        Assumes array is heapified before the idx
        '''
        if idx == 0:
            return
        while idx >0:
            par = (idx - 1)//2
            if self.heap[idx] < self.heap[par]:
                self.heap[idx], self.heap[par]= self.heap[par], self.heap[idx]
                idx = par

            
if __name__ == "__main__":
    lst =list(map(int, input("Enter nums : ").split()))
    lst_cpy1 = lst[:]
    lst_cpy2 = lst[:]
    
    minheap = MinHeap()
    # minheap.heapify(lst_cpy1)
    for ele in lst_cpy1:
        minheap.insert(ele)
    minheap.printHeap()
    # minheap.heapifyTopToBottom(lst_cpy1[:])
    # minheap.printHeap()
    minheap.heapifyBottomToTop(lst_cpy1[:])
    minheap.printHeap()
    heapq.heapify(lst_cpy2)
    # print("MxHeap  : ", lst_cpy1)
    print("MinHeapq : ", lst_cpy2)


