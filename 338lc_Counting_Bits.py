class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        TC: O(N)
        SC: O(N)
        '''
        match n:
            case 0:
                return [0]
            case 1:
                return [0,1]
        res = [0]*(n+1)
        res[1]=1
        prev = 2
        for num in range(2,n+1):
            if num%prev==0:
                prev = num
                res[num]=1
                continue
            res[num]= 1+ res[num%prev]
        
        return res

        
class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        TC: O(nlogn)
        SC: O(1)
        '''
        res = []
        def binrep(ele):
            n_ones = 0
            if not ele:
                return 0
            while ele !=0:
                if ele%2:
                    n_ones += 1
                ele //= 2
            return n_ones
        for i in range(n+1):
            res.append(binrep(i))
        return res
        