class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dts = {}
        for c1 in s:
            dts[c1] = dts.get(c1, 0)+1
        for c in t:
            if c in dts and dts[c]>0:
                dts[c] -=1
        cnt = 0
        for key in dts:
            cnt += dts[key]
        return cnt
        