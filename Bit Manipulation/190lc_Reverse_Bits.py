class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            if(n>>i) & 1:
                res = res | (1<<(31-i))
        return res
        
class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        mul=(1<<31)
        i=0
        while i < 32:
            if n & (1<<i):
                res = res+mul
            mul= mul>>1
            i += 1
        return res
        

class Solution:
    def reverseBits(self, n: int) -> int:
        rev_bin = bin(n)[2:]
        rev_bin = "0"*(32-len(rev_bin))+rev_bin
        rev_bin = rev_bin[::-1]
        num= int(rev_bin,2)
        return num

class Solution:
    def reverseBits(self, n: int) -> int:

        def intToBin(num):
            res = ""
            while num:
                res = str(num%2)+res
                num = num>>1
            res= "0"*(32-len(res))+res
            return res
        
        def binToInt(binRep):
            res=0
            mul=1
            for char in binRep[::-1]:
                res += int(char)*mul
                mul *= 2
            return res
        binRep= intToBin(n)
        revbinRep=binRep[::-1]
        return binToInt(revbinRep)
        