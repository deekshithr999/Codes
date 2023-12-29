class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        The biggest doubt, wt if the right side contributes +vely?
        or left side contributes negatively. But this doesn't happen 
        since a negative contribution is taken out. when the cumSum>0
        this does it.
        '''
        maxSum=nums[0]
        currSum = 0
        for num in nums:
            if currSum <0:
                currSum=0
            currSum += num
            maxSum = max(currSum, maxSum)
        return maxSum
        