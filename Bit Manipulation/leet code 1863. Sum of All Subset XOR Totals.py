class Solution:
    '''
    Recursive Approach
    '''
    def subsetXORSum(self, nums: List[int]) -> int:
        def getXor(i,xor):
            if i == len(nums):
                return xor    
            return getXor(i+1, xor) + getXor(i+1, nums[i]^xor)
        return getXor(0, 0)


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        nSubSets = 2**n
        totSum = 0
        for i in range(nSubSets):
            subXor = 0
            for j in range(n):
                if i & (1 << j):
                    subXor ^= nums[j]
            totSum += subXor
        return totSum
