class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjLst = {} # v -> (v, w)
        # for v in range(n): adjLst[v] = []

        for v1, v2, w in edges:
            adjLst[v1] = adjLst.get(v1, [])
            adjLst[v1].append((v2, w))
            adjLst[v2] = adjLst.get(v2, [])
            adjLst[v2].append((v1, w)) 

        minCov = n+1
        minCity = -1
        for v in range(n):
            nCov = self.calCities(adjLst, v, distanceThreshold, n)
            if nCov < minCov:
                minCov = nCov
                minCity = v
            elif nCov == minCov:
                if v > minCity: minCity=v #always true right
        return minCity

    def calCities( self, adjLst, fromV, distThres, n):
        minHeapq = [(0, fromV)]# (w, v)
        vis = [0]*n
        nCities = 0
        while True:

            while minHeapq and vis[ minHeapq[0][1]]:
                heapq.heappop(minHeapq)
            
            if not minHeapq:
                return nCities-1 # exit point
            
            fromW, fromV = minHeapq[0]
            heapq.heappop(minHeapq)
            vis[fromV]=1
            nCities += 1

            for toV, toW in adjLst[fromV]:
                if vis[toV] or fromW+toW > distThres: continue
                heapq.heappush(minHeapq, (fromW+toW, toV))
