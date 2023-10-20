class Solution:
    '''
    TC : O(n) + O(nlogn)
    SC : O(n)
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for num in nums:
            if num in st:
                return True
            else:
                st.add(num)
        return False

class Solution:
    '''
    TC : O(nlogn)
    SC : O(n)
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set(nums)
        if len(nums) != len(st):
            return True
        return False


class Solution:
    '''
    TC : O(nlogn)
    SC: O(1)
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        val = nums.sort()
        print("val : ", val)
        if len(nums) <2:
            return False
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


class Solution:
    '''
    TC : O(n^2)
    SC : O(1)
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False