class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        non DP
        TC: O(nlogn)
        SC: O(1)
        '''
        lst = [nums[0]]
        for num in nums:
            #maxi
            if lst[-1]<num:
                lst.append(num)
            #else
            #binSearch
            else:
                self.binSearch(num, lst, 0, len(lst)-1)
        # print(lst)
        return len(lst)
    
    def binSearch(self, num, lst, l, r):
        if(l>r):# It can/shld happen
            lst[l] = num
            return 
        mid = (l+r)//2
        if lst[mid] == num:
            return
        if num < lst[mid]:
            self.binSearch(num, lst, l, mid-1)
        else:
            self.binSearch(num, lst, mid+1, r) 
        
        

class Solution:
    '''
    Dynamic Programming
    TC: O(n^2)
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
    #get the max of prev nums lower than the curr num
        track = [1]*len(nums)
        res = 1

        for i in range(1, len(nums)):
            for j in range(i, -1, -1): # edge case : 0 1 [0 3] 2 3
                if nums[j]<nums[i]:
                    track[i] = max(track[j]+1, track[i])
        return max(track)

        