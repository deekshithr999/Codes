'''
Using Min heap to find the median
SC: O(r*c)
TC: O(nlogn)
'''

def build_list(matrix):
    lst=list()
    lst=[ matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
    return lst

def heap_sort(lst):
    heapify(lst)
    item=lst.pop(0)
    return item

def heapify(lst):

    for i in range(len(lst)-1,-1,-1):
        if 2*i+1 < len(lst):
            if 2*i+2 < len(lst):
                if lst[2*i+1]<lst[2*i+2]:
                    if lst[2*i+1]<lst[i]:
                        lst[i],lst[2*i+1]=lst[2*i+1],lst[i]
                    else:
                        pass # Don't do anything
                else:
                    if lst[2*i+2]<lst[i]:
                        lst[2*i+2],lst[i]=lst[i],lst[2*i+2]
                    else:
                        pass
            else:
                if lst[2*i+1]<lst[i]:
                    lst[i],lst[2*i+1]=lst[2*i+1],lst[i]


def find_median(matrix):
    lst=build_list(matrix)
    iseven = lambda num: True if num%2==0 else False
    if iseven(len(lst)):
        des2= len(lst)//2+1
        prev=0
        cur=0
        while des2!=0:
            prev=cur
            cur=heap_sort(lst)
            des2-=1
        
        desired_val=(prev+cur)/2
        
    else:
        desired= (len(lst)+1)//2
        while desired!=0:
            desired_val = heap_sort(lst)
            print("desired val", desired_val)
            desired-=1
    return desired_val


if __name__=="__main__":
    n,m = list(map(int, input().split()))
    print("n,m ",n," ",m)
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    print("MEDIAN ", find_median(matrix))
