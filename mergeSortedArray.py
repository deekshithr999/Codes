'''
link : https://leetcode.com/problems/merge-sorted-array/
88. Merge Sorted Array
Easy

2918

288

Add to List

Share
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''

'''
Sol 1: Traverse the arr1 and look for pos where arr2[index2]<arr1[index1]. shift all
elemens from index1 to the right and insert ele at arr2[index2] into arr1 at index1.

Time Complexity : O(n^2)
Space Complexity: O(1)
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j =0
        l =m
        
        while j<n:
            
            for i in range(l+1):
                if i ==l:
                    nums1[i]=nums2[j]
                    j+=1
                    l+=1
                    break
                elif nums2[j]<nums1[i]:
                    self.shiftright(nums1,i,l)
                    nums1[i]=nums2[j]
                    j+=1
                    l+=1
                    break
                    
    
    def shiftright(self,nums,index,length):
        
        for j in range(length-1,index-1,-1):
            nums[j+1]=nums[j]
                    
                
'''
Sol 2: 
since the elems are in non decreasing order, track the pos at which the elem from arr2 
is previously inserted. olah, from there u traverse to insert.
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        previous_inserted =-1
        l=m
        
        for j in range(n):
            
            for i in range(previous_inserted+1,l+1):
                if i ==l:
                    nums1[i]=nums2[j]
                    l+=1
                    j+=1
                    previous_inserted =i
                    break
                
                elif nums2[j]<nums1[i]:
                    self.shiftRight(nums1,i,l)
                    nums1[i]=nums2[j]
                    j+=1
                    l+=1
                    break
                    
                    
                    
    def shiftRight(self,nums,index,length):
        
        for i in range(length-1,index-1,-1):
            nums[i+1]=nums[i]
                
        