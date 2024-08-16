class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        mini = nums[0]
        for num in nums[1:]:
            if num > mini:
                maxDiff = max(maxDiff, num-mini)
            else:
                mini = min(mini, num)
        return maxDiff
        