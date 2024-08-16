class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        globalMin = len(nums)+1
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target: # = is to handle edge case when equal
                globalMin = min(globalMin, r-l+1)
                curSum -= nums[l]
                l += 1
                
        return globalMin if globalMin!= len(nums)+1 else 0
        