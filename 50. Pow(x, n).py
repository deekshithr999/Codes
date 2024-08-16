class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            if n < 0:
                return 1/helper(x, -n)

            res = helper(x, n//2)
            return res*res*x if n%2 else res*res

        return helper(x, n)
        