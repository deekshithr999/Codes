'''
sorting 3 colors / sort 0's 1's and 2's
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''
'''
method 3

#left of low should point to 0's
#left of mid should point to 1's
#right of high should point to 2's
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        low=mid=0
        # print(low,mid)
        high=len(nums)-1
        
        while(mid<=high):
            
            if nums[mid] == 1:
                mid+=1
                continue
            elif nums[mid] == 0:
                nums[low],nums[mid]=nums[mid],nums[low]
                mid +=1
                low +=1
                continue
            elif nums[mid] == 2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            
            
        return
                
        
'''
#method 2

#count all the 0's 1's and 2's
'''

'''
method 1
sort 2's first then sort 0's and 1's
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        #sort 2's inplace
        
        left=0
        right=len(nums)-1
        
        while(left<right):
            
            while left<len(nums) and nums[left]!=2:
                left+=1
                
            
            while right>-1 and nums[right]==2 :
                right-=1
                
            
            if left<right:
                nums[left],nums[right]=nums[right],nums[left]
        
        twos_start=len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==2:
                twos_start=i
        left=0
        right=twos_start-1
        
        while left < right:
            
            while left<twos_start and nums[left]==0:
                left+=1
            
            while right >-1 and nums[right]==1:
                right-=1
            
            if left < right:
                nums[left],nums[right]=nums[right],nums[left]
        
        
        return