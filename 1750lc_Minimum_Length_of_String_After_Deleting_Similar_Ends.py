class Solution:
    def minimumLength(self, s: str) -> int:
        l,r = 0, len(s)-1
        prev = '_'

        while l < r:
            if s[l] == prev:
                l += 1
            elif s[r] == prev:
                r -= 1
            elif s[l] == s[r]:
                prev = s[l]
                l,r = l+1, r-1
            else:
                break
        if l == r and prev == s[l]:
            l += 1
        
        return r-l+1 if r>=l else 0