
'''
https://leetcode.com/problems/kth-largest-element-in-an-array/

'''

class KthLargestElementInAnArray_Heap:

    def __init__(self):
        pass

    def swap(self, arr, idx1,idx2):
        arr[idx1],arr[idx2] = arr[idx2],arr[idx1]
        return
    
    def max_heapify(self, arr :list):
        i = len(arr)-1
        while i > 0:
            parent = (i-1)//2
            if i%2 == 0:
                if arr[i] > arr[i-1]:
                    if arr[i]>arr[parent]:
                        self.swap(arr, i, parent)
                else:
                    if arr[i-1] > arr[parent]:
                        self.swap(arr, parent, i-1)
                i -=2
            else:
                if arr[i]>arr[parent]:
                    self.swap(arr, i, parent)
                i -=1
    
    def max_element(self, arr):
        self.max_heapify(arr)
        return arr.pop(0)
    
    def kthlargest(self, arr, k):
        large = 0
        for i in range(k):
            large = self.max_element(arr)
        return large



class KthLargestElementInAnArray_QuickSelectAlgo:

    def __init__(self):
        pass

    def swap(self, arr, idx1,idx2):
        arr[idx1],arr[idx2] = arr[idx2],arr[idx1]
        return
    
    def kthlargest(self, arr, k):
        self.quickselect(0,len(arr)-1, arr, k)

    def quickselect(self, left, right, arr, kth):
        if left > right:
            return
        pivot_idx = self.quick_partition(left, right, arr)
        if right -pivot_idx+1 == kth:
            #print(arr[pivot_idx])
            return #arr[pivot_idx]
        elif right - pivot_idx+1 > kth:
            self.quickselect(pivot_idx+1, right, arr,kth)
        elif right - pivot_idx+1 < kth:
            kth -= (right - pivot_idx+1)
            self.quickselect(left, pivot_idx-1, arr,kth)
    
    def quick_partition(self, left, right, arr):

        pivot = left
        i,j = left, right

        while i < j:
            while arr[i] <= arr[pivot] and i < len(arr)-1: #mind the edge case for stop
                #print("pivot ",pivot)
                #print("i ",i)
                i += 1
            while arr[j] > arr[pivot]:
                j -= 1 
            if i < j :
                arr[i], arr[j] = arr[j], arr[i]
                #i += 1
                #j -= 1
        arr[j], arr[pivot] = arr[pivot], arr[j]
        return j
        

if __name__ == "__main__":
    klarge = KthLargestElementInAnArray_Heap()
    klarge_quick = KthLargestElementInAnArray_QuickSelectAlgo()
    kth = int(input())
    arr = list(map(int, input().split()))
    #print(klarge.kthlargest(arr,kth))
    klarge_quick.kthlargest(arr, kth)




                    
        

