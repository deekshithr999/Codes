class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        res = 0
        l, r = 1, max(candies)

        while l <= r:
            mid = (l+r)//2
            piles = 0
            for c in candies:
                piles += c//mid
            
            if piles >= k:
                res = max(res, mid)
                l = mid+1
            else:
                r = mid-1
        return res