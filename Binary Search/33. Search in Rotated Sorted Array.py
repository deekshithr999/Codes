class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            if nums[mid] < nums[r]: #right sorted
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid+1
            else: #left sorted
                if target > nums[mid] or target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return -1



class Solution:
    '''
    More intuitive
    '''
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            if nums[mid]<nums[r]:
                if target>nums[mid]:
                    if target<=nums[r]:
                        l = mid+1
                    else:
                        r = mid-1
                else:
                    r = mid-1
            else:
                if target > nums[mid]:
                    l = mid+1
                else:
                    if target <= nums[r]:
                        l = mid+1
                    else:
                        r = mid-1
        return -1
        