
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def genPerms(lidx, ridx, subSet):
            if ridx >= len(subSet):
                if lidx >=len(subSet):
                    res.append(subSet.copy())
                return

            subSet[lidx], subSet[ridx] = subSet[ridx], subSet[lidx]
            genPerms(lidx+1, lidx+1, subSet)
            subSet[lidx], subSet[ridx] = subSet[ridx], subSet[lidx]
            genPerms(lidx, ridx+1, subSet)

        genPerms(0,0,nums)
        return res
        

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res =[]
        def genPerms(cIdx, subSet):
            if cIdx == len(nums):
                res.append(subSet.copy())
                return
            for i in range(cIdx, len(nums)):
                subSet[i], subSet[cIdx] = subSet[cIdx], subSet[i]
                genPerms(cIdx+1, subSet)
                subSet[i], subSet[cIdx] = subSet[cIdx], subSet[i]
        genPerms(0, nums)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res =[]
        def genPerms(cIdx, subSet):
            if cIdx == len(nums):
                res.append(subSet)
                return
            for i in range(cIdx, len(nums)):
                subSetcpy = subSet.copy()
                subSetcpy[i], subSetcpy[cIdx] = subSetcpy[cIdx], subSetcpy[i]
                genPerms(cIdx+1, subSetcpy)
        genPerms(0, nums)
        return res
