class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        TC: O(n)
        SC: O(1)
        '''
        if n<=2:
            return n
        p2,p1 = 1,2
        for i in range(3,n+1):
            tmp = p2+p1
            p2=p1
            p1=tmp
        return p1

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        TC: O(n)
        SC: O(n)
        '''
        if n <=2:
            return n
        lst = [0]*(n+1)
        lst[1], lst[2]=1,2

        for i in range(3, n+1):
            lst[i]= lst[i-1]+lst[i-2]
        return lst[n]
        