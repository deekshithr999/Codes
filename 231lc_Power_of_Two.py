
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0
        

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
        p = 0
        while 2**p <= n:
            if 2**p == n:
                return True
            p +=1
        return False
        
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
        while n > 1:
            if n%2:
                return False
            n = n//2
        return True
