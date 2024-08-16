class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        for i in range(32):
            if n & (1 << i):
                if i%2: odd += 1
                else: even += 1
        return [even, odd]
        