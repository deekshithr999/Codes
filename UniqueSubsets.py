'''
Link : https://www.codingninjas.com/codestudio/problems/unique-subsets_3625236?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

Problem Statement
Ninja is observing an array of ‘N’ numbers and wants to make as many unique subsets as possible. Can you help the Ninja to find all the unique subsets?
Note: Two subsets are called same if they have same set of elements.For example {3,4,1} and {1,4,3} are not unique subsets.
You are given an array ‘ARR’ having N elements. Your task is to print all unique subsets.
For Example
For the given if ARR = [1,1,3],the answer will be [ ],[1],[1,1],[1,3],[3],[1,1,3].
Input Format:
The first line of the input contains an integer, 'T,’ denoting the number of test cases.

The first line of each test case contains a single integer ‘N’ denoting the number of elements.
The second line of each test case contains ‘ARR’ array.
Output Format:
For each test case, print all the subsets in each line.
Note:
You do not need to print anything. It has already been taken care of. Just implement the given function.
Return the output in sorted format as shown in the sample output.
Constraints:
1 <= T <= 10
1 <= N <= 20.
1 <= ARR[i] <=100

Time limit: 1 sec
Sample Input 1:
2
3
1 1 3
4
1 3 3 3
Sample Output 1:
1
1 1
1 3
3
1 1 3

1
1 3
1 3 3
1 3 3 3 
3 
3 3
3 3 3
Explanation Of Sample Input 1:
For the first test case,
The unique subsets will be  [ ],[1],[1,1],[1,3],[3],[1,1,3]. 

For the second test case:
The unique subsets will be  [ ],[1,3],[1,3,3],[1,3,3,3],[3],[3,3],[3,3,3]. 
Sample Input 2:
2
4
5 5 3 5 
3
1 3 5 
Sample Output 2:
3 
3 5 
3 5 5 
3 5 5 5 
5 
5 5 
5 5 5 

1 
1 3 
1 3 5 
1 5 
3 
3 5 
5


'''

#####################################################################

'''
I'm Lazy

TC : O(nlogn)+O(2^n)
SC : O(2^n)

'''
from typing import *

  
def uniqueSubsets(n :int,arr :List[int]) -> List[List[int]]:

    # Write your code here.
    # pass
	arr.sort()
	tlst=[]
	reslst=[]
	depthsubs(arr,n, 0,tlst,reslst)
	return reslst

def depthsubs(arr, n, start,tlst, reslst):
	#print ("start : ",start)
	if start == n:
		#print("==retu==")
		return
	
	for i in range(start,n):
		#print ("idx : ", i)
		if (i>0 and i-1>=start) and arr[i]==arr[i-1]:
			continue
			#pass
		ttlst=tlst.copy()
		ttlst.append(arr[i])
		reslst.append(ttlst)
		#print("here ",ttlst)
		depthsubs(arr,n,i+1,ttlst, reslst)
			
