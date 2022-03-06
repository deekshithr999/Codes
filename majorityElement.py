'''
leecode: https://leetcode.com/problems/majority-element/



169. Majority Element
Easy

8001

310

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''




'''
Solution 1: Intuitive 

Since #most occuring element > n/2

Use the count to track and finally the count comes out to be >=1


'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        desired_num=nums[0]
        nums.remove(nums[0])
        for num in nums:
            if num ==desired_num:
                count +=1
            else:
                count-=1
            
            if count<=0:
                count=1
                desired_num=num
        
        return desired_num





'''
Solution 2 :

sort the list/array. Since the number of occurances are >n/2 
=> the contiguous nums should exceed the middle element

TimeComplexity : O(nlogN)
SpaceComplexity: O(N) #if MergeSort


'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return(nums[int(len(nums)/2)])
        

'''
Solution 3: Naiive

count the occurances of each element

TimeComplexity :O(n)
spaceComplexity:O(n)
'''