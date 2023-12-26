
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(cIdx, csum, subSet):
            if csum == target:
                res.append(subSet.copy())
                return
            if cIdx == len(candidates) or csum > target:
                return
            
            csum += candidates[cIdx]
            subSet.append(candidates[cIdx])
            dfs(cIdx, csum, subSet)
            csum -= candidates[cIdx]
            subSet.pop()
            dfs(cIdx+1, csum, subSet)
        dfs(0, 0, [])
        return res



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def recSum(cIdx, subSet, csum):
            if cIdx >= len(candidates):
                return
            i = 0
            while True:
                if i != 0:
                    csum += candidates[cIdx]
                    subSet.append(candidates[cIdx])
                    
                if csum > target:
                    break
                elif csum == target:
                    res.append(subSet.copy())    
                    # print("here i = ",i,  res)
                    break
                else:
                    # print("subSet ", subSet)
                    recSum(cIdx+1, subSet.copy(), csum)
                i += 1
        recSum(0,[], 0)
        return res
        
        