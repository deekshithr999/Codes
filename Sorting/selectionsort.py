'''
TC: O(n^2)
SC: O(1)
'''
class SelectionSort(object):

    def selection_sort(self,lst):

        for i in range(len(lst)-1):
            min_idx = i
            for j in range(i, len(lst)):
                if lst[j] < lst[min_idx]:
                    min_idx=j
                         
            lst[min_idx], lst[i] = lst[i], lst[min_idx]



if __name__ == "__main__":
    
    lst = list(map(int,input().split()))
    ss = SelectionSort()
    ss.selection_sort(lst)
    print( "Sort: ", lst)
