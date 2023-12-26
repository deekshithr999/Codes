

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        TC: O(n *p)
        SC: O(1) # since the max space required will be 26 size
        '''
        if len(s)< len(p):
            return []
        p_dict = Counter(p)
        l, r = 0, len(p)-1
        s_dict = Counter(s[l:r+1])
        res = []

        while r < len(s):
            # search the dict
            all_vals = True
            for key,val in p_dict.items():
                if val == s_dict.get(key,0):
                    #fine
                    pass
                else:
                    all_vals = False
            if all_vals:
                res.append(l)
            s_dict[s[l]]-=1
            l +=1
            r +=1
            if r < len(s):
                s_dict[s[r]]= s_dict.get(s[r],0)+1
        return res

        

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        TC: O(n(p+p))
        SC: O(1) #same as above
        '''
        resIndices = []

        ctr_p = Counter(p)
        for idx, letter in enumerate(s):
            if letter in ctr_p:
                substr = s[idx: idx+len(p)]
                tmpctr = Counter(substr)
                if tmpctr == ctr_p:
                    resIndices.append(idx)
        return resIndices
        
