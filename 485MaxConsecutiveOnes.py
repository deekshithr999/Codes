'''
link : https://leetcode.com/problems/max-consecutive-ones/

485. Max Consecutive Ones
Easy

2523

395

Add to List

Share
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
Accepted
639,038
Submissions
1,161,241

'''

#############################################################
'''
TC : O(n)
SC : O(1)

'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_ones=0
        t_ones=0
        
        for i in range(len(nums)):
            if nums[i]:
                t_ones+=1
            else:
                max_ones=max(max_ones,t_ones)
                t_ones=0
        
        max_ones=max(max_ones,t_ones)
        return max_ones
