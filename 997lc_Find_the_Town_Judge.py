class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ntrusts = [0]*(n+1)
        ppl = [0]*(n+1)
        for p,t in trust:
            ntrusts[t] += 1
            ppl[p] = 1 
        
        for idx, nt in enumerate(ntrusts):
            if idx ==0:
                continue
            if nt == n-1 and not ppl[idx]:
                return idx

        return -1 
