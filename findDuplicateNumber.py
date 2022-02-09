'''
287. Find the Duplicate Number
Medium

11220

1182

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?


'''

'''
Soln 1: Using Floyd's loop detection algorithm
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        loop_at = 0
        slow = fast = 0
        
        while (True):
            
            slow = nums[slow]
            fast =nums[nums[fast]]
            
            if slow ==fast:
                break
        
        slow =0
        
        while True:
            
            slow =nums[slow]
            fast =nums[fast]
            
            if slow ==fast :
                return slow
            
'''
Soln #2:

Using hashing / storing the address or values of the visited nodes
'''

'''
Soln #3:

modifying the visited index with -ve .
'''