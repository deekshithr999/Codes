class Solution:
    def longestPalindrome(self, s: str) -> str:

        big_str = ""
        
        #1. odd
        for i in range(0, len(s)):
            l,r = i,i
            while l>=0 and r < len(s):
                if s[l]== s[r]:
                    if r-l+1 >len(big_str):
                        big_str = s[l:r+1]
                else:
                    break
                l-=1
                r+=1
        
        #2. Even
        for i in range(0, len(s)):
            l,r = i, i+1
            while l >=0 and r < len(s):
                if s[l]==s[r]:
                    if r-l+1 > len(big_str):
                        big_str = s[l:r+1]
                else:
                    break
                l -= 1
                r += 1
        return big_str

        