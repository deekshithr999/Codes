class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        nflips = 0
        for i in range(32):
            if c & 1 <<i:
                if a & 1 <<i or b & 1<<i:
                    continue
                nflips += 1
            else:
                if a & 1<<i:
                    nflips += 1
                if b & 1 <<i:
                    nflips += 1
        return nflips



class Solution:
    '''
    Going round and round and round and round and go round
    '''
    def minFlips(self, a: int, b: int, c: int) -> int:
        nflips = 0
        a_and_b = a&b
        a_or_b = a | b
        for i in range(32):
            if c & 1 << i:
                if a_or_b & 1<<i:
                    pass
                else:
                    nflips +=1 
            else:
                if a_and_b & 1 << i:
                    nflips +=2
                elif a_or_b & 1 <<i:
                    nflips += 1
        return nflips