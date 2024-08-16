class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def genCombin(idx, lst):
            if len(lst)==k:
                res.append(lst[:])
                return#more work heree
            for i in range(idx, n+1):
                lst.append(i)
                genCombin(i+1, lst)
                lst.pop()
        genCombin(1, [])
        return res
        