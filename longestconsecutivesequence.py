'''
128. Longest Consecutive Sequence
Medium

8592

374

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
612,232
Submissions
1,262,189

'''


'''
Sol 

Use set to store the elems

note: Avoid duplicate searching ie avoid o(n^2)

TC : O(n)+O(n)+O(n)
SC : O(n)
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st =set()
        mx_len=0
        for i in range(len(nums)):
            st.add(nums[i])
        
        for i in range(len(nums)):
            if (nums[i]-1) in st:
                continue
            else:
                tlen=1
                tnum=nums[i]+1
                while(tnum in st):
                    tlen+=1
                    tnum+=1
                mx_len=max(mx_len,tlen)
        return mx_len

'''
Sol :

sort the array and look for the max consecutive sequence

TC: O(nlogn)+O(n)
SC: O(n) if mergesort
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        
        mx_len=0
        
        tlst=[]
        
        for i in range(len(nums)):
            if len(tlst)==0:
                tlst.append(nums[i])
            elif  nums[i]==tlst[len(tlst)-1]+1 or nums[i]==tlst[len(tlst)-1]:
                if nums[i]!=tlst[len(tlst)-1]:
                    tlst.append(nums[i])
            else:
                if mx_len<len(tlst):
                    mx_len=len(tlst)
                del tlst[:]
                    #tlst=[]
                tlst.append(nums[i])
        if len(tlst)>mx_len:
            mx_len=len(tlst)
        return mx_len
                    
        