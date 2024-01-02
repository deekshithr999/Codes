class Solution:
    '''
    TC: O(n+m)
    SC: O(n+m)
    '''
    def minWindow(self, s: str, t: str) -> str:
        if t== "" or len(s)< len(t):
            return ""
        windowS, trackT = {}, {}
        for c in t:
            trackT[c] = trackT.get(c,0)+1
        have, need = 0, len(trackT)
        resStr, resLen = "", len(s)+1

        l,r = 0,0
        while r < len(s):
            windowS[s[r]]=windowS.get(s[r],0)+1
            if s[r] in trackT and windowS[s[r]]==trackT[s[r]]:
                have += 1
            r += 1
            
            while have==need: # remove l < r bcz empty t str is handled 1st.
                if resLen > r-l:
                    resStr,resLen = s[l:r], r-l 
                windowS[s[l]] -=1
                if s[l] in trackT and windowS[s[l]]< trackT[s[l]]:
                    have -= 1
                l += 1
        return resStr



class Solution:
    '''
    TC: O(n*m)
    SC: O(n+m)
    '''
    def minWindow(self, s: str, t: str) -> str:
        resStr, resLen = "", len(s)+1
        s_dict=defaultdict(int)
        t_dict = Counter(t)
        l,r = 0,0

        def compd1gtd2(dt1, dt2):
            for key in dt2:
                if dt1[key]<dt2[key]:
                    return False
            return True
        
        while r < len(s):
            if s[r] in t_dict:
                s_dict[s[r]] += 1
            r += 1

            while l < r:
                if s[l] not in t_dict or s_dict[s[l]]>t_dict[s[l]]:
                    s_dict[s[l]]-=1
                    l += 1
                else:
                    break
            
            if compd1gtd2(s_dict, t_dict) and r-l <resLen:
                resStr, resLen = s[l:r], r-l
        return "" if resLen==(len(s)+1) else resStr
