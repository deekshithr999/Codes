'''
https://leetcode.com/problems/merge-intervals/
56. Merge Intervals
Medium


Add to List

Share
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

'''soln 1: '''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i =1
        
        while i <len(intervals):
            
            if intervals[i][0]<=intervals[i-1][1]:
                
                if intervals[i][1]<=intervals[i-1][1]:
                    intervals.pop(i)
                
                elif intervals[i][1]>intervals[i-1][1]:
                    intervals[i-1][1]=intervals[i][1]
                    intervals.pop(i)
                
            else:
                i+=1
        
        return intervals
        