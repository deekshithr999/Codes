class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        remBottles = 0
        while numBottles:
            res += numBottles
            fullBottles = (numBottles+ remBottles)//numExchange
            remBottles = (numBottles+ remBottles)%numExchange
            numBottles = fullBottles
        return res