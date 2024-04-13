class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dt = {}
        dt[0]=1
        res = 0
        currSum = 0
        for num in nums:
            currSum += num
            if currSum - goal in dt:
                res += dt[currSum - goal]
            dt[currSum] = dt.get(currSum, 0)+1
        return res