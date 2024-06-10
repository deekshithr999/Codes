class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dt = {}
        def isPalin(ipStr):
            if ipStr in dt:
                return dt[ipStr]
            l,r = 0, len(ipStr)-1
            while l < r:
                if ipStr[l] != ipStr[r]:
                    dt[ipStr]=False
                    return False
                l += 1
                r -= 1
            dt[ipStr]=True
            return True

        def partGen(idx, curLst, resLst):
            if idx == len(s):
                resLst.append(curLst)
                return
            for i in range(idx, len(s)):
                sst = s[idx: i+1]
                if not isPalin(sst):
                    continue
                newcurLst = curLst[:]
                newcurLst.append(sst)
                partGen(i+1, newcurLst, resLst)
        resLst = []
        curLst = []
        partGen(0, curLst, resLst)
        return resLst