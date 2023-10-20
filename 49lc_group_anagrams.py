
class Solution:
    '''
    TC: O(m*n)
    SC: O(m*n)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for st in strs:
            cnt = [0]*26
            for ch in st:
                cnt[ord(ch)-ord('a')]+=1
            res[tuple(cnt)].append(st)
        return res.values()


        

class Solution:
    '''
    TC: O(m*nlogn)
    sc: O(n)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dt = {}
        for st in strs:
            sst = str(sorted(st))
            print(sst)
            dt[sst]=dt.get(sst,[])
            dt[sst].append(st)
        
        for keys in dt:
            res.append(dt[keys])
        return res

class Solution:
    '''
    TC: O(m*n +m^2)
    SC: O(n*m)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cntr_lst = []
        res = []
        for st in strs:
            cntr_lst.append(Counter(st))
        
        for i in range(len(cntr_lst)):
            if cntr_lst[i] == -1:
                continue
            anas = [strs[i]]
            for j in range(i+1, len(cntr_lst)):
                if cntr_lst[j]==-1:
                    continue
                if cntr_lst[i]==cntr_lst[j]:
                    anas.append(strs[j])
                    cntr_lst[j]=-1
            cntr_lst[i]=-1
            res.append(anas)
        return res
        

        