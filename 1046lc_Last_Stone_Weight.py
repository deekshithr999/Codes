class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        inv_stones = [-stone for stone in stones]
        heapq.heapify(inv_stones)

        while len(inv_stones)>1:
            stone1, stone2 = heapq.heappop(inv_stones), heapq.heappop(inv_stones)
            stone1, stone2 = -stone1, -stone2
            if stone1==stone2:
                pass
            else:
                heapq.heappush(inv_stones, -1*abs(stone1-stone2))
        
        if inv_stones:
            return -inv_stones[0]
        else:
            return 0
        