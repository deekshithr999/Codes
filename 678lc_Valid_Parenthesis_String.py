
class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0
        for c in s:
            if c == "(":
                leftMin, leftMax= leftMin +1, leftMax+1
            elif c == ")":
                leftMin, leftMax= leftMin -1, leftMax-1
            else:
                leftMin, leftMax= leftMin -1, leftMax+1
            if leftMax <0:
                return False
            if leftMin <0:
                leftMin = 0
        return leftMin==0

        


class Solution:
    '''
    Looks fishy, don't know how it worked
    TC: O(n)
    SC: O(n)
    '''
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = 0
        i = -1
        for char in s:
            i +=1
            if char == "*":
                stars += 1
            elif char == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    if stars:
                        stars -=1
                    else:
                        return False
        
        for i in range(len(s)-1,-1,-1):
            if not stack:
                return True
            if not stars:
                return False
            
            if s[i]=="*":
                ele = stack.pop()
                if ele<i:
                    stars -=1
                    pass
                else:
                    return False
            else:
                pass

        return True               
    

class Solution:
    '''
    Memoization Technique
    TC: O(n^3)  
    SC: O(n^2)
    '''
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def dfs(idx, left):
            if idx == len(s) or left < 0:
                return left == 0
            if (idx, left) in dp:
                return dp[(idx, left)]
            
            if s[idx] == '(':
                dp[(idx, left)] = dfs(idx+1, left+1)
            elif s[idx] == ')':
                dp[(idx, left)] = dfs(idx+1, left-1)
            else:
                dp[(idx, left)] = dfs(idx+1, left+1) or dfs(idx+1, left) or dfs(idx+1, left-1)
            
            return dp[(idx, left)]
        return dfs(0, 0)

        