
class Solution:
    '''
    Din't quite get though
    '''
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
    '''
    Adding each element to the subset progressively
    {}
    {1}
    {2,1}, {1,2}
    {3,2,1}, {2,3,1}, {2,1,3}, {3,1,2}, {1,3,2}, {1,2,3}
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        resSet = [[]]
        for num in nums:
            newResSet = []
            for subSet in resSet:
                for pos in range(len(subSet)+1):
                    newSubSet = subSet[:]
                    newSubSet.insert(pos, num)
                    newResSet.append(newSubSet)
            resSet = newResSet
        return resSet
               

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


