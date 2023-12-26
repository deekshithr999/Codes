class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        TC: O(n)
        SC: O(1)
        '''
        intervals.sort()
        res=0
        prevEnd=intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd=intervals[i][1]
            else:
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
        return res



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1], intervals[i][1])
        return res

        