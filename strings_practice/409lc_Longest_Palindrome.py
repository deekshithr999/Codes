class Solution:
    def longestPalindrome(self, s: str) -> int:
        dt = Counter(s)
        cnt = 0
    
        for c in dt:
            if dt[c]%2==0:
                cnt += dt[c]
                dt[c]=0
            else:
                cnt += dt[c]-1
                dt[c]=1
        
        for c in dt:
            if dt[c]:
                cnt += 1
                break
        return cnt
