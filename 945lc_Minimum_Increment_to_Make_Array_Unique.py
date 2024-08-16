class Solution:
    '''
    TC: O(nlogn)
    '''
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1]>= nums[i]:
                res += 1 + nums[i-1]-nums[i]
                nums[i] = nums[i-1]+1
        return res


class Solution:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def minIncrementForUnique(self, nums: List[int]) -> int:
        countDict = Counter(nums)
        res = 0
        for i in range(max(nums)+len(nums)):
            if countDict[i] > 1:
                extra = countDict[i]-1
                countDict[i+1] += extra
                res += extra
        return res