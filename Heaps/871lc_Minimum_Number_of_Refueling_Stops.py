class PriorityQueue:
    def __init__(self):
        self.minHeap = []
    
    def push(self, ele):
        heapq.heappush(self.minHeap, -ele)
    def pop(self):
        heapq.heappop(self.minHeap)
    def top(self):
        return -self.minHeap[0]
    def empty(self):
        return True if len(self.minHeap) == 0 else False


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cnt = 0
        pq = PriorityQueue()
        maxReach = startFuel

        index = 0
        while maxReach < target:
            while index < len(stations) and maxReach >= stations[index][0]:
                pq.push(stations[index][1])
                index+=1
            
            if pq.empty(): return -1
            maxReach += pq.top()
            pq.pop()
            cnt += 1
        return cnt
