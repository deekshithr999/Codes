'''
link : https://leetcode.com/problems/reverse-pairs/

493. Reverse Pairs
Hard

2541

172

Add to List

Share
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
 

Constraints:

1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1
Accepted
77,471
Submissions
261,307

'''

'''
Sol 1 : 
Using mergeSort befor merging compare the elements
travel till num[left_iterator]<=2*num[right_iterator]
such that all the elems on the left of right_iterator are>2*num[right_iterator]

TC:O(nlogn) i.e O(nlogn)+O(n)+O(n)
SC:O(n)
'''
class Solution(object):
    count=0
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.mergeSort(nums,0,len(nums)-1)
        return self.count

    
    def mergeSort(self,nums,left,right):
        
        mid =left+int((right-left)/2)
        if left<right:
            self.mergeSort(nums,left,mid)
            self.mergeSort(nums,mid+1,right)
        self.countReverse(nums,left,mid,right)
        self.merge(nums,left,mid,right)
    
    def countReverse(self,nums,left,mid,right):
        
        #print(nums[left:mid+1]," ",nums[mid+1:right+1])
        il=left
        ir=mid+1
        
        while il<=mid and ir<=right:
            
            while ir<=right and  nums[il]>2*nums[ir]:
                ir+=1
            self.count+=(ir-mid-1)
            #print("cnt ",self.count)
            il+=1
        
        if ir>right:
            
            while il<=mid:
                self.count+=(ir-mid-1)
                il+=1

    def merge(self,nums,left,mid,right):
        #print("bef ",nums[left:mid+1]," ",nums[mid+1:right+1])
        il =left
        ir=mid+1
        tlst=[]
        while il<=mid and ir<=right:
            #print("il, nums[i;] ",il," ",nums[il])
            if nums[il]<nums[ir]:
                tlst.append(nums[il])
                il+=1
            else:
                tlst.append(nums[ir])
                ir+=1
        
        while il<=mid:
            
            tlst.append(nums[il])
            #print("here ",tlst)
            il+=1
        
        while ir<=right:
            tlst.append(nums[ir])
            ir+=1
        
        for i in range(len(tlst)):
            nums[left+i]=tlst[i]
        #print("aft ",nums[left:right+1])