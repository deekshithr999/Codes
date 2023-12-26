class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        TC: O(n)
        SC: O(n)
        '''
        res=[]
        
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0], newInterval[1]= min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res














class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        idx =-1

        for i in range(len(intervals)):
            stari=intervals[i][0]
            if newInterval[0]<stari:
                break
            idx=i

        tmpidx = idx+1

        while tmpidx < len(intervals):
            if newInterval[1]>=intervals[tmpidx][1]:
                intervals.pop(tmpidx)
            else:
                break
        if len(intervals)==0:
            intervals.append(newInterval)
            return intervals
        if idx == len(intervals)-1:
            if newInterval[0]>intervals[-1][1]:
                #append and return
                intervals.append(newInterval)
            elif newInterval[1]>intervals[-1][1]:
                intervals[-1][1]=newInterval[1]
            return intervals

        if idx == -1:
            if len(intervals)>0:
                if newInterval[1] < intervals[0][0]:
                    intervals.insert(0, newInterval)
                else:
                    intervals[0][0]=newInterval[0]
            else:
                intervals.append(newInterval)
            return intervals
        
        if newInterval[0]> intervals[idx][1] and newInterval[1] < intervals[idx+1][0]:
            intervals.insert(idx+1, newInterval)
        elif newInterval[0]<= intervals[idx][1] and newInterval[1]>=intervals[idx+1][0]:
            intervals[idx][1]=intervals[idx+1][1]
            intervals.pop(idx+1)

        elif newInterval[0]<= intervals[idx][1]:#edge case
            if newInterval[1]> intervals[idx][1]:
                intervals[idx][1]=newInterval[1]
            
        elif newInterval[0] < intervals[idx+1][0] :
            intervals[idx+1][0]=newInterval[0]
        return intervals