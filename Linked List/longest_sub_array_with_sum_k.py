'''
https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
'''

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        #Code here
        maxLen = 0
        dt = {0:-1}
        currSum = 0
        for idx, num in enumerate(arr):
            currSum += num
            # print("idx, tot ", idx, currSum," ", currSum-k)
            if currSum-k in dt:
                maxLen = max(maxLen, idx - dt[currSum-k])
            if currSum not in dt: # little logi, no confusion
                dt[currSum]=idx
        return maxLen


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends