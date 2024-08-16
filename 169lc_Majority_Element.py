class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorEle = 1
        cnt = 0

        for num in nums:
            if num == majorEle:cnt+=1
            elif cnt: cnt-=1
            else:
                cnt=1
                majorEle = num
        return majorEle


'''
link : https://leetcode.com/problems/majority-element-ii/

229. Majority Element II
Medium

4431

268

Add to List

Share
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?

Accepted
271,431
Submissions
647,924

'''

'''
Sol 1:

Since there could be maximum 2 elements whose count is >n/3
Track them

Use Boyer moore's voting algorithm
TC : O(n)
SC : O(1)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Using boyer moore voting algorithm
        rest =[]
        num1=num2=-3
        count1=count2=0
        #print(count1,count2)
        for num in nums:
            if num==num1:
                count1+=1
            elif num==num2:
                count2+=1
            
            elif count1==0:
                num1=num
                count1+=1
            elif count2==0:
                num2=num
                count2+=1
            else:
                count1-=1
                count2-=1
            
        tc1=0
        tc2=0
        #print(num1," ",num2)
        for num in nums:
            if num1==num:
                tc1+=1
            elif num2==num:
                tc2+=1
        
        if tc1>int(len(nums)/3):
            rest.append(num1)
        if tc2>int(len(nums)/3):
            rest.append(num2)
        return rest

'''
Sol 2 :

Sort the array and count the occurances and verify

TC: O(nlogn)
SC: O(1)
'''

'''
Sol 3:

Use the hashmap /dict to trace the #occurances

TC: O(n)
SC: O(n)
'''
                
        