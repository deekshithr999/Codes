class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor = xor^num
        return xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dt = {}
        for num in nums:
            dt[num]= dt.get(num,0)+1
        
        for k,v in dt.items():
            if v==1:
                return k
        return -1