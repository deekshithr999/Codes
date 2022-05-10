'''
15. 3Sum
Medium

17214

1653

Add to List

Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
Accepted
1,886,555
Submissions
6,089,686

'''



#############################################################################
'''
TC : O(n^2)
SC: O(1)

Using 3 pointer approach
Fixing ele 'a'. Inorder to handle the max 2 same elems in a triplet

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        low,high=0,0
        res_lst=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=len(nums)-1
            a=nums[i]
            while low<high:
                if nums[low]+nums[high]<-a:
                    low+=1
                elif nums[low]+nums[high]>-a:
                    high-=1
                else:
                    res_lst.append([a,nums[low],nums[high]])
                    low+=1
                    high-=1
                    while(low<len(nums) and nums[low]==nums[low-1]):
                        low+=1
                    while(high>-1 and nums[high]==nums[high+1]):
                        high-=1
        return res_lst

#############################################################################
'''
with the middle ele as the fixed one
i.e b as fixed. Read the problem desc

TC : O(nlogn)+O(n*n)+O(m*logn)
SC : O(n)

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res_lst=[]
        nums.sort()
        for i in range(1,len(nums)-1):
            low=0
            high=len(nums)-1
            #if i>1 and nums[i]==nums[i-1]:
            #    continue
            
            while low<i and high>i:
                if nums[low]+nums[high]<-nums[i]:
                    low+=1
                elif nums[low]+nums[high]>-nums[i]:
                    high-=1
                else:
                    tlst=[nums[low],nums[i],nums[high]]
                    res_lst.append(tlst)
                    low+=1
                    high-=1
                    while low<i and nums[low]==nums[low-1]:
                        low+=1
                    while high>i and nums[high]==nums[high+1]:
                        high-=1
        res_lst=set(tuple(ele) for ele in res_lst)
        res_lst=list(list(ele) for ele in res_lst)
        return res_lst
            
        
#############################################################################
'''
TC : O(nlogn)+O(n^2)+O(nlogn)
SC : O(n)

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res_list=[]
        dt=dict()
        
        for num in nums:
            
            if num in dt:
                dt[num]+=1
            else:
                dt[num]=1
        
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                dt[nums[i]]-=1
                dt[nums[j]]-=1
                add=nums[i]+nums[j]
                if -add in dt and dt[-add]>0:
                    tlst=[nums[i],nums[j],-add]
                    tlst.sort()
                    res_list.append(tlst)
                dt[nums[i]]+=1
                dt[nums[j]]+=1
                
                
                
                
        res_list=set(tuple(ele) for ele in res_list)
        res_list=[list(ele) for ele in res_list]
        return res_list
    


############################################################################
'''
Using maps to store data and the set to store unique values

TC : O(n)+O(n^3)+O(nlogn)
SC: O(2n)

Fails in the time limit

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        dt={}
        res_list=[]
        
        #got the dict
        for i in range(len(nums)):
            if nums[i] in dt:
                dt[nums[i]].append(i)
            else:
                dt[nums[i]]=[i]
        vals=dt.keys()
        #print(vals)
        for key in dt:
            if len(dt[key])>1:
                tmp=2*key
                if tmp!=0 and -tmp in vals:
                    tlst=[key,key,-tmp]
                    res_list.append(tlst)
                if key==0 and (len(dt[key])>2):
                    #print("here")
                    res_list.append([0,0,0])
                    #print(-tmp)
        #done double case handling
        
        uniquelst=list(vals)
        for i in range(len(uniquelst)-2):
            for j in range(i+1,len(uniquelst)-1):
                for k in range(j+1,len(un   iquelst)):
                    tmp=uniquelst[i]+uniquelst[j]+uniquelst[k]
                    if tmp==0:
                        tlst=[uniquelst[i],uniquelst[j],uniquelst[k]]
                        res_list.append(tlst)
        
        return res_list


#############################################################################
'''
TC : O(n^3)
SC : O(1)
'''




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res_list=[]
        
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    tmp=nums[i]+nums[j]+nums[k]
                    if tmp==0:
                        tlst=[nums[i],nums[j],nums[k]]
                        tlst.sort()
                        res_list.append(tlst)
        
        res_list=set(tuple(ele) for ele in res_list)
        res_list=[list(ele) for ele in res_list]
        return res_list
        