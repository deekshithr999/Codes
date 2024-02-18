class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}
        def dfs(idx):
            if idx in cache:
                return cache[idx]
            res = 0 #handles the edge case j==len(arr)
            currMax = 0
            for i in range(idx, min(idx+k, len(arr))):
                ws = i-idx+1
                currMax = max(currMax, arr[i])
                res = max(res, currMax*ws + dfs(i+1))
            cache[idx]=res
            return res
        return dfs(0)

        