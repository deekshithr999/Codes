class Solution:
    def countBits(self, n: int) -> List[int]:
        if n<=1:
            return range(n+1)
        res=[0]*(n+1)
        res[1]=1
        div=2
        for i in range(2,n+1):
            res[i]=1+ res[i%div]
            if not i%div:
                div=i
        return res
        