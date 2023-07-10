import heapq

class MinHeap:
    def __init__(self):
        pass

    def swap(self, lst, i1, i2):
        lst[i1], lst[i2] = lst[i2], lst[i1]
    def find_min_and_swp1(self, lst, par):
        lc = 2*par + 1
        rc = 2*par + 2

        if rc < len(lst):
            if lst[lc] < lst[rc]:
                if lst[lc] < lst[par]:
                    self.swap(lst, par, lc)
            else:
                if lst[rc] < lst[par]:
                    self.swap(lst, par, rc)
            return
        
        if lc < len(lst):
            if lst[lc] < lst[par]:
                self.swap(lst,lc,rc)
            return
    
    def find_min_and_swp2(self, lst, par):
        lc = 2*par + 1
        rc = 2*par + 2

        if lc < len(lst):
            if rc < len(lst) and lst[rc] < lst[lc]:
                if lst[rc] < lst[par]:
                    self.swap(lst, rc, par)
            elif lst[lc] < lst[par]:
                self.swap(lst, lc, par)
        return

        
    def heapify(self, lst):

        for i in range(len(lst)//2 - 1,-1,-1): #-1 for getting the index
            self.find_min_and_swp2(lst, i)

        
if __name__ == "__main__":
    lst =list(map(int, input("Enter nums : ").split(',')))
    lst_cpy1 = lst[:]
    lst_cpy2 = lst[:]
    
    minheap = MinHeap()
    minheap.heapify(lst_cpy1)
    heapq.heapify(lst_cpy2)
    print("MxHeap  : ", lst_cpy1)
    print("MxHeapq : ", lst_cpy2)


