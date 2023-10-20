
class Solution:
    '''
    TC: O(2n)
    SC: O(1) # Since space for answer is not consiered as an extra space
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        right_prod =1
        ans[0]= nums[0]
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i]
        for i in range(len(nums)-1,0,-1):
            ans[i]=ans[i-1]*right_prod
            right_prod *= nums[i]
        ans[0]= right_prod
        return ans
        


class Solution:
    '''
    TC: O(3*n)
    SC: O(2*n)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        res = [0]*len(nums)
        left,right = [0]*len(nums),[0]*len(nums)
        left[0] = nums[0]
        right[len(nums)-1] = nums[len(nums)-1]
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i]
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i]
        
        res[0]=right[1]
        res[len(nums)-1]=left[len(nums)-2] 
        for i in range(1,len(nums)-1):
            res[i]= left[i-1]*right[i+1]
        return res


class Solution:
    '''
    TC: O(2n)
    SC: O(1)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_zeros = 0
        tot_prod =1
        res = []
        for num in nums:
            if num == 0:
                n_zeros += 1
                continue
            tot_prod *= num
        if n_zeros >1:
            return [0]*len(nums)
        elif n_zeros == 1:
            for idx in range(len(nums)):
                if nums[idx] == 0:
                    res.append(tot_prod)
                else:
                    res.append(0)
            return res
        else:
            for num in nums:
                res.append(tot_prod//num)
            return res
        return res


        

class Solution:
    '''
    TC: O(n^2)
    SC: O(1)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            prod =1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            ans.append(prod)
        return ans
        