

class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r = len(nums), -1
        maxL, minR = float('-inf'), float('inf')
        
        for i in range(len(nums)):
            maxL = max(maxL, nums[i])    
            if nums[i] < maxL:
                r = i
        if r == -1: return 0 # completely sorted

        for i in range(len(nums)-1,-1,-1):
            minR = min(minR, nums[i])

            if nums[i]>minR:
                l = i
        return r-l+1

        

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        TC: O(nlogn)
        SC: O(1)
        '''
        newArr  = nums[:]
        newArr.sort()
        start,end = 0, len(nums)-1

        for start in range(len(nums)):
            if nums[start] != newArr[start]:
                break
        if start == len(nums)-1:return 0
        for end in range(len(nums)-1, -1, -1):
            if nums[end] != newArr[end]:
                break
        return end-start+1
        

class Solution:
    '''
    TC: O(n^2)
    SC: O(1)
    '''
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = len(nums), -1

        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j]<nums[j-1]:
                left = min(left, j-1)
                right = max(right, j)
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return max(right -left +1 , 0)

        