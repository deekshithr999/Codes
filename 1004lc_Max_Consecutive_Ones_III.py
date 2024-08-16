
class Solution:
    '''
    Awesomee!!!
    The idea is to find only the max window size expand or remain constant
    '''
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroIdx = -1
        maxOnes = 0
        for i in range(len(nums)):
            if nums[i]:pass
            else:
                k -= 1
                if k == -1:
                    zeroIdx += 1
                    while nums[zeroIdx]:
                        zeroIdx += 1
                    k += 1
            maxOnes = max(maxOnes, i - zeroIdx)
        return maxOnes


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxSum = 0
        curSum = 0
        zeroIdx = -1
        for i in range(len(nums)):
            if nums[i]: curSum += 1
            elif k:
                k -= 1
                curSum += 1
            else:
                zeroIdx += 1
                while nums[zeroIdx]:
                    zeroIdx += 1
                    curSum -= 1
            maxSum = max(maxSum, curSum)
        return maxSum
        