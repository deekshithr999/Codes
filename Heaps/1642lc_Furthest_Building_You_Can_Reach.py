class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxheap = []
        for i in range(1, len(heights)):
            diff = heights[i]-heights[i-1]
            if diff <=0:
                continue
            heapq.heappush(maxheap, -diff)
            bricks = bricks-diff
            if bricks <0:
                if ladders == 0:
                    return i -1 
                ladders -=1
                bricks += -heapq.heappop(maxheap)
        return len(heights)-1