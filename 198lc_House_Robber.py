class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        TC: O(n)
        SC: O(1)
        '''
        if len(nums)==1:
            return nums[0]
        tmp1, tmp2 = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            cmon = max(nums[i]+ tmp1, tmp2)
            tmp1, tmp2 = tmp2, cmon
        
        return tmp2
        