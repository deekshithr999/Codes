
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