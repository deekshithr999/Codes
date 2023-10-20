
class Solution:
    '''
    TC : O(nlogn)
    SC : O(n)
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds,dt = {},{}
        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i],0)+1
            dt[t[i]] = dt.get(t[i], 0) +1
        return ds == dt


class Solution:
    '''
    TC : O(nlogn)
    SC: O(n)
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        cs = Counter(s)
        ct = Counter(t)
        #print(cs)
        return cs == ct

class Solution:
    '''
    TC: O(nlogn)
    sc: O(1)
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        st = sorted(t)
        return ss == st