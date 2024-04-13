

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dt = Counter(arr)
        vals = dt.values()
        return len(vals)==len(set(vals))

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dt = Counter(arr)
        arr = [0]*(1001)
        for _, val in dt.items():
            if arr[val] !=0:
                return False
            arr[val]=1
        return True
        