class Solution:
    def countSubstrings(self, s: str) -> int:
        tot_palins = 0

        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r < len(s) and s[l]==s[r]:
                tot_palins += 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l>=0 and r< len(s) and s[l]==s[r]:
                tot_palins += 1
                l -= 1
                r += 1
        return tot_palins
        