

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        TC: O(2**n *n)
        SC: O(2**n *n)
        '''
        res = []
        nPowSets = 2**len(nums)
        for i in range(nPowSets):
            subSet = []
            for j in range(len(nums)):
                if i & (1<<j):
                    subSet.append(nums[j])
            res.append(subSet)
        return res

class Solution:
    '''
    Recursive Solution
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def generateSubSets(nums, cIdx, cLst, res):
            '''
            TC: O(2^n)
            SC: O(2^n *n) # 2**n subsets with max of n elems
            '''
            for i in range(cIdx+1, len(nums)):
                lst_cpy = cLst.copy()
                lst_cpy.append(nums[i])
                res.append(lst_cpy)
                generateSubSets(nums, i, lst_cpy, res)
        res = [[]]
        generateSubSets(nums, -1, [], res)
        return res
        