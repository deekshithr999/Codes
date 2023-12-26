

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def recSubGen(currIdx, subSet):
            if currIdx == len(nums):
                res.append(subSet.copy())
                return
            subSet.append(nums[currIdx])
            recSubGen(currIdx+1, subSet)
            subSet.pop()
            while currIdx +1 < len(nums) and nums[currIdx]== nums[currIdx+1]:
                currIdx +=1
            recSubGen(currIdx+1, subSet)
        recSubGen(0,[])
        return res
        
        
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        dt =Counter(nums)
        keysTup = tuple(dt.keys())
        def recSetGen(currIdx, subSet):
            if currIdx == len(keysTup):
                res.append(subSet.copy())
                return
            subSet.extend([keysTup[currIdx]]*dt[keysTup[currIdx]])

            for i in range(dt[keysTup[currIdx]], -1,-1):
                recSetGen(currIdx+1, subSet)
                if i!=0:
                    subSet.pop()
        recSetGen(0,[])
        return res
        