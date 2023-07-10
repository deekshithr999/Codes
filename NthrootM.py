'''
Problem Statement
Detailed explanation ( Input/output format, Notes, Constraints, Images )
Sample Input 1:
1
3 27
Sample Output 1:
3.000000
Explanation For Sample Input 1:
3rd Root of 27 is 3.000000, as (3.000000)^3 is equal to 27.
Sample Input 2:
1
4 69
Sample Output 2:
2.882121
''''


'''
TC: O(logn)
SC: O(1)
'''
def findNthRootOfM(n,m):
    # Write your Code here.
    error_cap=0.000001
    low=0
    high=m
    if m<1:
        low =m
        high=1
    while True:
        mid = (low+high)/2
        kk = pow(mid,n)
        if kk>m:
            high = mid
        else:
            low=mid
        if abs(kk-m) <error_cap:
            return mid
    