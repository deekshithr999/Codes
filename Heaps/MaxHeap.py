
import heapq
class MaxHeap:
    def __init__(self):
        pass

    def get_maxofthree_idx(self, lst, par, lchild = 0, rchild = 0):
        lchild = 2*par + 1
        rchild = 2*par + 2
        if rchild < len(lst):
            if lst[lchild] > lst[rchild]:
                if lst[lchild] > lst[par]:
                    return lchild
            else:
                if lst[rchild] > lst[par]:
                    return rchild
        
        if lchild < len(lst):
            if lst[lchild] > lst[par]:
                return lchild
        return par
    
    def swap(self, lst, idx1, idx2):
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
        return

    def heapify(self, lst):
        for i in range(len(lst)//2, -1, -1):
            mxidx = self.get_maxofthree_idx(lst, i)
            self.swap(lst, i, mxidx)




if __name__ == "__main__":
    lst =list(map(int, input("Enter nums : ").split(',')))
    lst_cpy1 = lst[:]
    lst_cpy2 = lst[:]
    lst_cpy2 = [ele*-1 for ele in lst_cpy2] #invert to get max heap
    mxheap = MaxHeap()
    mxheap.heapify(lst_cpy1)
    heapq.heapify(lst_cpy2)
    lst_cpy2 = [ele*-1 for ele in lst_cpy2] #invert back again
    print("MxHeap  : ", lst_cpy1)
    print("MxHeapq : ", lst_cpy2    )





