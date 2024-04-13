class Solution:
    '''
    TC: O(n)
    SC: O(m) #len of array
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqLst = [[] for _ in range(len(nums)+1)]
        dt = {}
        for num in nums:
            dt[num] = dt.get(num,0)+1
        
        for num, freq in dt.items():
            freqLst[freq].append(num)
        
        for subfLst in freqLst[::-1]:
            for ele in subfLst:
                if not k:
                    return res
                res.append(ele)
                k -= 1
        return res


class Solution:
    '''
    Using Min Heap
    TC: O(nlogk)
    SC: O(k)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = {}
        minHeap = []
        res = []
        for num in nums:
            dt[num] = dt.get(num, 0)+1

        for num,freq in dt.items():
            if len(minHeap)<k:
                heapq.heappush(minHeap, (freq, num))
                continue
            top = minHeap[0]
            if top[0]< freq:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (freq, num))
        
        for _, num in minHeap:
            res.append(num)
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