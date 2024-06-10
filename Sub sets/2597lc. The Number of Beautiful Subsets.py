class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        dt = defaultdict(int)
        def genSubSets(idx):
            if idx == len(nums):
                return 1
            res = genSubSets(idx+1)
            if not dt[nums[idx]-k] and not dt[nums[idx]+k]:
                dt[nums[idx]] += 1
                res += genSubSets(idx+1)
                dt[nums[idx]] -= 1
            return res
        return genSubSets(0)-1