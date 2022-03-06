import sys
inv_count = 0
def mergeSort(arr,left,right):
    mid = left+int((right-left)/2)
    if(left<right):
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
    merge(arr,left,mid,right)

def merge(arr,left,mid,right):
    global inv_count
    i=left
    j=mid+1
    tlist=[]
    while(i<=mid and j<=right):
        if(arr[i]<arr[j]):
            tlist.append(arr[i])
            i+=1
        else:
            tlist.append(arr[j])
            j+=1
            inv_count+=(mid-i+1)
    while(i<=mid):
        tlist.append(arr[i])
        i+=1
    
    while(j<=right):
        tlist.append(arr[j])
        j+=1
   	
    for k in range(len(tlist)):
        arr[left+k]=tlist[k]
    
    
        
def getInversions(arr, n) :
	# Write your code here.
    global inv_count
    mergeSort(arr,0,n-1)
    return inv_count

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))