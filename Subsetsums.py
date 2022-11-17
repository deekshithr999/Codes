'''

Link : https://practice.geeksforgeeks.org/problems/subset-sums2234/1#
Given a list arr of N integers, print sums of all subsets in it.

 

Example 1:

Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.
Example 2:
Example 2:

Input:
N = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8
Your Task:  
You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes a list/vector and an integer N as an input parameter and return the list/vector of all the subset sums.

Expected Time Complexity: O(2N)
Expected Auxiliary Space: O(2N)

Constraints:
1 <= N <= 15
0 <= arr[i] <= 104

'''
##########################################################
'''

Recursive Approach 
TC : O(2^N)
SC : O(2^N)
'''
class Solution:
    def subsetSums(self, arr, N):
        # code here
        nelem =0
        reslst = [0]
        csum = 0
        self.depthSum(arr,N,0,csum,reslst)
        return reslst
            
    
    def depthSum( self, arr,N, start,csum,reslst):
        if start == N:
            return
        
        for i in range(start,N):
            reslst.append(csum+arr[i])
            self.depthSum(arr,N,i+1,csum+arr[i],reslst)
            self.depthSum(arr,)
            
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends
##########################################################

'''
TC : O(N*2^n)
SC : O(2^N)

Recursive Approach

'''
#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		nelem =0
		reslst = [0]
		csum = 0
		for mxdepth in range(1,N+1):
            self.depthSum(arr,N,0,csum,1,mxdepth,reslst)
        return reslst
		    
	
	def depthSum( self, arr,N, start,csum, currdepth, maxdepth,reslst):
	    if currdepth > maxdepth:
	        reslst.append(csum)
	        return
	    
	    for i in range(start,N):
	        #csum+=arr[i]
	        self.depthSum(arr,N,i+1,csum+arr[i],currdepth+1,maxdepth,reslst)
	        
	        
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends