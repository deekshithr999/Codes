
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[-1]

        #include 1st home & don't go till last
        #As expected exclude 1st and go till last

        def robWithCondition(nums):
            if len(nums)==1:
                return nums[-1]
            tmp1, tmp2 = nums[0], max(nums[0:2])
            for i in range(2, len(nums)):
                tmp = max(nums[i]+tmp1, tmp2)
                tmp1, tmp2 = tmp2, tmp
            return tmp2
        return max(robWithCondition(nums[:-1]), robWithCondition(nums[1:]))
        


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        TC: O(2N)
        SC: O(1)
        '''
        if len(nums)==1:
            return nums[-1]
        elif len(nums)==2:
            return max(nums)
        # leave this elif len(nums)==3:
        #1 ignore 1 
        tmp1, tmp2 = nums[1], max(nums[2], nums[1])
        for i in range(3, len(nums)):
            ccost = max(tmp2, tmp1+ nums[i])
            tmp1 = tmp2
            tmp2 = ccost
        from1st = tmp2

        #2 include 1
        tmp1, tmp2 = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)-1):
            ccost = max(tmp2, nums[i]+tmp1)
            tmp1 =tmp2
            tmp2 = ccost
        return max(from1st, tmp2)

