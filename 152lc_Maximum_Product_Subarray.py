
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        resMax = nums[0]

        prod = 1
        for i in range(len(nums)):
            prod = prod*nums[i]
            resMax = max(resMax, prod)
            if not prod:prod=1
        
        prod = 1
        for j in range(len(nums)-1,-1,-1):
            prod *=nums[j]
            resMax = max(resMax, prod)
            if not prod: prod=1
        return resMax


        

class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1,1
        for num in nums:
            if num == 0:
                currMax, currMin = 1,1
                res = max(res,0)
                continue
            
            stored_max = currMax
            currMax = max(currMax*num, currMin*num, num)
            currMin = min(stored_max*num, currMin*num, num)
            res = max(res, currMax)
        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        curProd = 1
        maxProd = nums[0] 
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0: #handle this
                while l < i-1: # [-6, 0] , [2, 0]

                    curProd = curProd//nums[l]
                    maxProd = max(maxProd, curProd)
                    l+=1
                maxProd = max(maxProd, 0)
                curProd =1 
                l = i+1
            else:
                curProd *= nums[i]
                maxProd = max(maxProd, curProd)
        
        while l < len(nums)-1: #handle last negative
            curProd = curProd//nums[l]
            l+=1
            maxProd = max(maxProd, curProd)
        return maxProd
        