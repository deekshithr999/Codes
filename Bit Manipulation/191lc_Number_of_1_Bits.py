class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while n:
            cnt+=1
            n=n&(n-1) #Amazing Approach
        return cnt

class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_rep = bin(n)[2:]
        cnt = 0
        for char in bin_rep:
            cnt += ( 1 if char == "1" else 0)
        return cnt

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt, i =0,0
        while i < 32:
            cnt += ( 1 if n & (1<<i) else 0) #diff
            i += 1
        return cnt

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt =0
        while n:
            if n & 1:
                cnt +=1
            n=n>>1 #difference, right shift
        return cnt
        