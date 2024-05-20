
class Solution:
    '''
    Iteration approach
    TC:O(logn)
    '''
    def findMin(self, nums: List[int]) -> int:
        minEle = nums[0]
        l,r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            minEle = min(minEle, nums[mid])
            if nums[mid]<nums[r]: # right side is sorted
                r = mid-1
            else:
                l = mid+1
        return minEle
        
        


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minEle = nums[0]
        def binSearch(nums, l, r):
            nonlocal minEle
            if (l > r):
                return
            mid = (l+r)//2
            minEle = min(minEle, nums[mid])
            if nums[mid]>nums[r]: #min exists in bw
                binSearch(nums, mid+1, r)
            else:
                binSearch(nums, l, mid-1)
        binSearch(nums, 0, len(nums)-1)
        return minEle
        