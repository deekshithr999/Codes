'''
link : https://www.codingninjas.com/codestudio/problems/920321?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

Longest Subarray Zero Sum
Difficulty: EASY
Avg. time to solve
15 min
Success Rate
85%
Problem Statement
Ninja loves playing with numbers. So his friend gives him an array on his birthday. The array consists of positive and negative integers. Now Ninja is interested in finding the length of the longest subarray whose sum is zero.
Input Format:
The first line contains a single integer T, denoting the number of test cases. 

The first line of each test case will contain the integer N, denoting the number of elements in the given array.

The second and last line contains N space-separated integers that denote the value of the elements of the array.
Output Format
The first and only line of each test case in the output contains an integer denoting the length of the longest subarray whose sum is zero.
Note:
You are not required to print the expected output; it has already been taken care of. Just implement the function.
Constraints:
1 <= T <= 10
1 <= N <= 10^4
-10^5 <= arr[i] <= 10^5

Time Limit: 1 sec
Sample Input 1:
2 
5
1 3 -1 4 -4
4
1 -1 2 -2 
Sample Output 1:
2
4 
Explanation For Sample Output 1:
In the first test case, the given array is (1, 3, -1, 4, -4). The sub-arrays we can create are (1), (3), (-1), (4), (-4), (1, 3), (3, -1), (-1, 4), (4, -4), (1, 3, -1), (3, -1, 4), (-1, 4, -4), (1, 3, -1, 4), (3, -1, 4, -4), (1, 3, -1, 4, -4). Out of them only (4, -4) is the sub array whose sum is zero.Length of this sub array is 2 and hence we return 2 as the final answer.

In the second test case, the given array is (1, -1, 2, -2). The sub-arrays we can create are (1), (-1), (2), (-2), (1, -1), (-1, 2), (2, -2), (1, -1, 2), (-1, 2, -2), (1, -1, 2, -2). Out of them sub arrays with zer sum are (1, -1), (2, -2), (1, -1, 2, -2). Out of them only (1, -1, 2, -2) has the longest length of 4. Hence we return 4 as the final answer.
Sample Input 2:
2 
3
4 -5 1
4
1 2 1 -2
Sample Output 2 :
3
0

'''
'''
Sol :

Storing the intermittent values

if the sum repeats again from the start which means that
values between the curr and 1st occurance adds upto 0

TC: O(n)+O(1)
SC: O(n)
'''
def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    mxlen=0
    dct={}
    tsum=0
    dct.setdefault(0,-1)
    for i in range(len(arr)):
        tsum=tsum+arr[i]
        if tsum in dct:
            mxlen=max(mxlen,i-dct[tsum])
        else:
            dct.setdefault(tsum,i)
    return mxlen


###################################################

'''
Sol :

improvement for the below

Instead of storing the intermediate vals
perform the temp comparison of the sum

TC : O(n^2)
SC : O(1)
'''
def LongestSubsetWithZeroSum(arr):
    
    mxlen=0
    
    for i in range(len(arr)):
        tsum=0
        for j in range(i,len(arr)):
            tsum=tsum+arr[j]
            if tsum==0:
                mxlen=max(mxlen,j-i+1)
    return mxlen

###################################################
'''
Sol :

Storing the intermediate results and calculate the sum

TC : O(n^2)
SC : O(n)
'''
def LongestSubsetWithZeroSum(arr):

    slst=[]
    mxlen=0
    slst.append(arr[0])
    idx=0
    for i in range(1,len(arr)):
        slst.append(slst[idx]+arr[i])
        idx+=1
    
    for i in range(0,len(slst)):
        for j in range(-1,i):
            if j ==-1:
                if slst[i]==0:
                    mxlen=max(mxlen,i+1)
                
            elif slst[j]-slst[i]==0:
                mxlen=max(mxlen,i-j)
    
    return mxlen
                
    
###################################################
'''

Sol :

use brute force approach to calculate the sum

TC: O(n^3)
SC: O(1)

'''
def LongestSubsetWithZeroSum(arr):
    
    mxlen=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            tsum=0
            for k in range(i,j+1):
                tsum+=arr[k]
            if tsum==0:
                mxlen=max(mxlen,j-i+1)
    return mxlen