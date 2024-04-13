class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i=0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return left << i

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        lbin = bin(left)[2:]
        rbin = bin(right)[2:]

        lbin = '0'*(32-len(lbin))+lbin
        rbin = '0'*(32-len(rbin))+rbin
        i = 0
        while i < 32:
            if lbin[i] == '0' and rbin[i] == '1':
                break
            i +=1
        res = lbin[:i]+'0'*(32-i)
        res = int(res,2)
        return res
        