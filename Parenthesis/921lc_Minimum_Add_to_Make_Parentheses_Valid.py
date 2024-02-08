class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l= 0
        res = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                if l>0:
                    l -=1
                else:
                    res += 1
        res += l
        return res  


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        cnt = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    cnt +=1
        cnt += len(stack)
        return cnt

        