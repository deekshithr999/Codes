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
    '''
    TC: O(n)
    SC: O(1)
    '''
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        l,r = 0,0
        curr_prod = 1
        while r < len(nums):
            if nums[r]==0:
                while l<r:
                    if l+1 == r:
                        curr_prod = nums[l]
                    else:
                        curr_prod = curr_prod // nums[l]
                    max_prod = max(max_prod, curr_prod)
                    l += 1
                max_prod = max(max_prod, 0)
                l += 1
                curr_prod = 1
            else:
                curr_prod *= nums[r]
                max_prod = max(max_prod, curr_prod)
            # print("max_sum, idx", max_prod, r)
            r += 1

        if curr_prod >0:
            return max_prod
        while l < r:
            if l+1 == r:
                curr_prod = nums[l]
            else:
                curr_prod = curr_prod // nums[l]
            max_prod = max(max_prod, curr_prod)
            l += 1
        return max_prod