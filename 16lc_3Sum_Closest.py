class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        tot = sum(nums[0:3])
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l < r:
                tsum = nums[i]+nums[l]+nums[r]
                if tsum == target:
                    tot = tsum
                    return tot
                if abs(tsum-target)<abs(tot-target):
                    tot = tsum
                if nums[i]+nums[l]+nums[r]<target:
                    l += 1
                else:
                    r -= 1
        return tot
        