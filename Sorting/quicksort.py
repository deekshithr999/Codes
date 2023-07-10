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



class Classic_Code_QuickSort(object):

    def quicksort(self,lst,left,right):
        if left <right: #handling left & right edge case 
            partition1 = self.partition(lst,left,right)
        
            self.quicksort(lst,left,partition1-1)
            self.quicksort(lst,partition1+1,right)
    
    def partition(self,lst,left,right):

        pivot = left
        l=left
        r=right

        while l<r:
            while l<=right: #see this = Edge Case
                if lst[l]>lst[pivot]:
                    break
                l+=1
            
            while r>left: #see this, removed = from here to compensate the below stmt
                if lst[r]< lst[pivot]:
                    break
                r-=1
            
            if l<r:
                lst[l],lst[r] = lst[r],lst[l]
        
        lst[r],lst[pivot] = lst[pivot],lst[r]

        return r



if __name__ == "__main__":

    lst= list(map(int,input().split(',')))
    lst2=lst[:]
    qc1 = QuickSort1()
    qc1.quicksort(lst, 0, len(lst)-1)
    print ("sorted list ", lst)

    clsc_qc2 =Classic_Code_QuickSort()
    clsc_qc2.quicksort(lst2,0,len(lst)-1)
    print ("sorted list ", lst2)