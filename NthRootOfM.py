

'''
Link : https://www.codingninjas.com/codestudio/problems/1062679
Problem Statement
You are given two positive integers N and M. You have to find the Nth root of M i.e. M^(1/N).
Note:
N'th root of an integer M is a real number, which when raised to the power N gives M as a result.

N'th root of the M should be correct up to 6 decimal places.
Input Format:
The first line of the input contains an integer T denoting the number of test cases.

The first and only line of each test case consists of two space-separated integers N and M.
Output Format:
For each test case, print a real number with precision till 6 decimal places that denote the Nth root of M in a separate line.
Note:
You don't have to print anything, it has already been taken care of. Just Implement the given function.
Constraints:
1<= T <= 10^3
1<= N <= 300
1<= M <= 10^15

Time Limit: 1 sec.
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

'''


#####################################################3
'''

'''

def powmn(m,n):
    return pow(m,n)
def findNthRootOfM(n,m):
    # Write your Code here.
    return binsearch(1,m,m,n)

def binsearch(left,right,m,n):
    #print(1e-6*1)
    if right-left<1e-6:
        return left
    mid=(left+right)/2
    val=powmn(mid,n)
    #print(val)
    if val==m:
        return mid
    if val<m:
        return binsearch(mid,right,m,n)
    if val>m:
        return binsearch(left,mid,m,n)



