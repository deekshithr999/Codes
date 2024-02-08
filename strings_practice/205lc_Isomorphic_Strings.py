class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap, dmap = {}, {}

        for c1, c2 in zip(s,t):
            if (c1 in smap and smap[c1] != c2 ) or (c2 in dmap and dmap[c2] != c1):
                return False
            smap[c1],dmap[c2]=c2,c1
        return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dt = {}
        st = set()

        for i in range(len(s)):
            if s[i] not in dt:
                if t[i] in st:
                    return False
                dt[s[i]]=t[i]
                st.add(t[i])
            else:
                if dt[s[i]] != t[i]:
                    return False
        return True