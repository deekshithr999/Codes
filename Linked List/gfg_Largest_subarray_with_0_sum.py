'''
https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
'''

#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        maxLen = 0
        dt = {0:-1}
        currSum = 0
        for idx, num in enumerate(arr):
            currSum += num
            if currSum in dt:
                maxLen = max(maxLen, idx - dt[currSum])
            else:
                dt[currSum]=idx
        return maxLen

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends