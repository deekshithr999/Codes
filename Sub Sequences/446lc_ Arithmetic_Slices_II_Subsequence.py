class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        TC: O(n^2)
        SC: O(n^2)
        '''
        track = [{} for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(0, i):
                diff = nums[j]-nums[i]
                track[i][diff]=1+track[i].get(diff,0)+track[j].get(diff,0)
        items = len(nums)
        cnt = -items*(items-1)//2

        for dt in track:
            for _,val in dt.items():
                cnt += val
        return cnt
        