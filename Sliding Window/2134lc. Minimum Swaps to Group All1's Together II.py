class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        totOnes = nums.count(1)
        maxOnes = curOnes = 0
        l = 0

        for r in range(2*N):
            curOnes += nums[r%N]
            if r-l+1 > totOnes:
                curOnes -= nums[l%N]
                l += 1
            maxOnes = max(maxOnes, curOnes)
            
        return totOnes - maxOnes
        