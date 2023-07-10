'''
https://www.codingninjas.com/codestudio/problems/873378?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
Matrix Median

Problem Statement
Detailed explanation ( Input/output format, Notes, Constraints, Images )
Sample Input 1:
2
1 3
1 2 3
3 3
2 6 9
1 5 11
3 7 8
Sample Output 1:
2
6
Explanation Of Sample Input 1:
In the first test case, the overall median of the matrix is 2.

In the second test case, the overall median of the matrix is 6.
Sample Input 2:
2
3 3
2 6 8
1 4 7
6 8 9
3 5
1 2 6 6 10
2 4 4 5 7
2 5 5 6 6
Sample Output 2:
2
5
Explanation For Sample Input 2:
In the first test case, the overall median of the matrix is 2.

In the second test case, the overall median of the matrix is 5.

'''


'''
TC: O(log(r*c)) # since in python dictionaries are ordered like a stored set
SC: O(r*c)

'''

def get_cnt(matrix):
    return len(matrix)*len(matrix[0])

def getMedian(matrix):
    from collections import OrderedDict #CHECK THIS OUT

    # Write your code here.
    #pass
    dct=dict()
    #print(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #print(matrix[i][j])
            #print("dct.get(matrix[i][j]",dct.get(matrix[i][j],0))
            dct[matrix[i][j]]=dct.get(matrix[i][j],0)+1
            
    total=get_cnt(matrix)
    mid=(total+1)//2
    dct=OrderedDict(sorted(dct.items()))
    #print(dct)
    cnt=0
    prev=0
    for k,v in dct.items():
        prev_cnt=cnt
        cnt+=v
        #For even if cnt is in middle, taken Care
        if mid>prev_cnt and mid<=cnt:
            return k
        if total%2==0:
            if prev_cnt==desired:
                return (prev+k)/2
        prev=k
            
            
    return 0



'''
TC: O(nlogn)
SC: O(1) #if mergesort O(n)
'''
def getMedian(matrix):
    # Write your code here.
    lst=list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            lst.append(matrix[i][j])
    lst.sort()
    mid=(len(lst)+1)//2
    if len(lst)%2==0:
        return (lst[mid-1]+lst[mid])/2
    return lst[mid-1]
    
