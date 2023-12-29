

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        TC: O(n)
        SC: O(1)
        wt an awesome loghgic
        '''
        first = second = float('inf')
        for num in nums:
            if num<=first:
                first = num
            elif num<= second:
                second = num
            else:
                return True
        return False
        

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        TC: O(n)
        SC: O(n)
        '''
        if len(nums)<3:
            return False
        min_lst = [nums[0]]*len(nums)
        max_lst = [nums[-1]]*len(nums)

        for i in range(1, len(nums)):
            min_lst[i]= min(min_lst[i-1], nums[i])
        for i in range(len(nums)-2,-1,-1):
            max_lst[i]= max(max_lst[i+1], nums[i])
        
        for i in range(1, len(nums)-1):
            if min_lst[i-1]<nums[i]< max_lst[i+1]:
                return True
        return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        TC: O(n^2)
        SC: O(1)
        '''
        if len(nums)<3:
            return False
        
        for i in range(len(nums)-2):
            max_ele = nums[-1]
            for j in range(len(nums)-1,i,-1):
                if nums[i]<nums[j]< max_ele:
                    return True
                max_ele = max(max_ele, nums[j])
        return False
        