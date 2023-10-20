
class Solution:
    '''
    
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = {}
        res = []
        for num in nums:
            dt[num] = dt.get(num,0)+1
        arr = [[] for i in range(len(nums)+1)]
        for key, val in dt.items():
            arr[val].append(key)
        rem = k
        for i in range(len(arr)-1,-1,-1):
            if len(arr[i])==0:
                continue
            for kk in range(len(arr[i])):
                if rem == 0:
                    return res
                res.append(arr[i][kk])
                rem -=1
        return res


class Solution:
    '''
    TC: O(n + nlogn +k)
    SC: O(n)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dt = defaultdict(int)
        dt = {}
        res = []
        for num in nums:
            dt[num] = dt.get(num,0)+1
        lsttup = [tup for tup in dt.items()]
        lsttup.sort(key=lambda x:x[1], reverse = True)
        res = [ lsttup[i][0] for i in range(k)]
        return res


        