'''
link : https://leetcode.com/problems/4sum/
18. 4Sum
Medium

5724

653

Add to List

Share
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
Accepted
550.8K
Submissions
1.5M

'''

'''
Sol :
TC: O(n^3)+O(nlogn)
SC:O(n)

'''

import bisect
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        flst=[]
        for i in range(len(nums)):
            if i==0 or (i>0 and nums[i-1]!=nums[i]):
                for j in range(i+1,len(nums)):
                    if j==i+1 or (nums[j-1]!=nums[j]):
                        tmp=nums[i]+nums[j]
                        pt=target-tmp
                        k=j+1
                        l=len(nums)-1
                        while(k<l):
                            if k!=j+1 and (nums[k]==nums[k-1]):
                                k+=1
                                continue
                            elif l!=len(nums)-1 and (nums[l]==nums[l+1]):
                                l-=1
                                continue
                            elif nums[k]+nums[l]<pt:
                                k+=1
                            elif nums[k]+nums[l]>pt:
                                l-=1
                            elif nums[k]+nums[l]==pt:
                                flst.append([nums[i],nums[j],nums[k],nums[l]])
                                k+=1
                                l-=1
                                
        return flst

'''
Sol :
TC:O(n^3 log(n)) +O(nlogn)
SC:O(n)
'''
import bisect
class Solution(object):
    def bin_search(self,nums,target,lo,hi):
        i=bisect.bisect_left(nums,target,lo,hi)
        if i<len(nums) and nums[i]==target:
            return i
        return -1
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        flst=[]
        nums=sorted(nums)
        start=0
        l=len(nums)
        i=0
        while i<len(nums):
            if ((i==0) or (i>0 and (nums[i-1]!=nums[i]))):
                print("i ",i)
                j=i+1
                while j<len(nums):
                    if((j==i+1) or (nums[j]!=nums[j-1])):
                        print("j ",j)
                        k=j+1
                        #prev_idx=-2
                        while k<len(nums) :
                            if((k==j+1) or (nums[k]!=nums[k-1])):
                                print("k ",k)
                                tmp =nums[i]+nums[j]+nums[k]
                                rt =self.bin_search(nums,target-tmp,k+1,len(nums))
                                print("rt ",rt)
                                if rt !=-1 :
                                    flst.append([nums[i],nums[j],nums[k],nums[rt]])
                                    #prev_idx=rt
                            k+=1
                    j+=1
            i+=1
                    
        return flst
                        
                        
        

'''
Sol :

TC:O(n^4)
SC: O(1)
'''