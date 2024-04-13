class Solution:
    '''
    TC: O(n*m) # m is the maxsum
    SC: O(n*m)
    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, currSum):
            if i == len(nums):
                return 1 if currSum==target else 0
            if (i, currSum) in dp:
                return dp[(i, currSum)]
            dp[(i, currSum)] = dfs(i+1, currSum+nums[i]) + dfs(i+1, currSum-nums[i])
            return dp[(i, currSum)]
        return dfs(0, 0)
