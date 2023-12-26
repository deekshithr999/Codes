def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

# Example usage:
arr = [5, 2, 9, 1, 7, 6, 3]
quicksort(arr, 0, len(arr) - 1)
print(arr)







'''

TC: O(nlogn)
WorstCase: O(n^2)
SC: O(1)
'''




class QuickSort1:
    def quicksort(self,lst, left, right):

        if left> right:
            return

        l =left
        r = right
        pivot = l

        while l < r:
            while l<=right:
                if lst[l]>lst[pivot]:
                    break
                l+=1
            
            while r >= left:
                if lst[r]<=lst[pivot]: #see the == here
                    break
                r-=1   
            if l < r:
                lst[l],lst[r] = lst[r],lst[l]
        lst[r],lst[pivot] = lst[pivot],lst[r]
        
        self.quicksort(lst, left, r-1)
        self.quicksort(lst, r+1, right)
        return





if __name__ == "__main__":

    lst= list(map(int,input().split(',')))
    lst2=lst[:]
    qc1 = QuickSort1()
    qc1.quicksort(lst, 0, len(lst)-1)
    print ("sorted list ", lst)

    clsc_qc2 =Classic_Code_QuickSort()
    clsc_qc2.quicksort(lst2,0,len(lst)-1)
    print ("sorted list ", lst2)