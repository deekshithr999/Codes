'''
Link : https://leetcode.com/problems/two-sum/
1. Two Sum
Easy

29854

940

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
Accepted
6,098,690
Submissions
12,620,794
'''



class Solution:
    '''
    Sol 1 :

    Using HashTable 

    TC : O(n)
    SC : O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_dt = {}
        for i in range(len(nums)):
            idx = prev_dt.get(target-nums[i],-1)
            if idx != -1:
                return [i, idx]
            else:
                prev_dt[nums[i]]=i
        return [0,0]
        
                

'''
Sol 2 :

Use iterative approach to solve

TC:O(n^2)
SC:O(1)

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    
                    return [i,j]
        return []
                


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [0,0]