'''
TC: O(N^2)
SC: O(1)
'''

class InsertionSort(object):

    def insertion_sort(self, lst):

        for it in range(1,len(lst)):
            exidx = it

            for j in range(exidx-1,-1,-1):
                if lst[exidx]<lst[j]:
                    lst[exidx], lst[j] = lst[j], lst[exidx]
                    exidx = j
                else:
                    break


if __name__ == "__main__":

    lst = list(map(int,input().split()))
    isort = InsertionSort()
    isort.insertion_sort(lst)
    print("Sort : ", lst)