class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        maxBombs = 0
        for idx in range(len(bombs)):
            vis = [0]*len(bombs)
            self.detonateBomb(bombs, vis, idx)
            maxBombs = max(maxBombs, sum(vis))
        return maxBombs

    def withinRadius(self, src, dst):
        x1, y1 = src[0], src[1]
        radius = src[2]
        x2, y2 = dst[0], dst[1]
        if ((x1-x2)**2 + (y1-y2)**2 <= radius**2):
            return True
        return False
    

    def detonateBomb(self, bombs, vis, srcIdx):

        vis[srcIdx] = 1
        for tarIdx in range(len(bombs)):
            if (not vis[tarIdx]) and self.withinRadius(bombs[srcIdx], bombs[tarIdx]):
                self.detonateBomb(bombs, vis, tarIdx)