class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        curMin, curMax = arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            minEle, maxEle = arrays[i][0], arrays[i][-1]
            res = max(res, maxEle-curMin, curMax-minEle)
            curMin = min(curMin, minEle)
            curMax = max(curMax, maxEle)
        return res
