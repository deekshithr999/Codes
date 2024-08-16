class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            canPlace = True
            if n==0:break
            if flowerbed[i]: canPlace = False
            if i-1>=0 and flowerbed[i-1]==1:canPlace = False
            if i+1 < len(flowerbed) and flowerbed[i+1]==1: canPlace = False
            if canPlace:
                flowerbed[i]=1
                n -= 1
        return n==0


        