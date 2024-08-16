class Solution:
    def clearDigits(self, s: str) -> str:
        modS = s

        i = 0
        while i < len(modS):
            if ord('a') <= ord(modS[i]) <= ord('z'):
                pass
            else:
                if i == 0:
                    modS = modS[:i] + modS[i+1:]
                 
                else:
                    modS =  modS[:i-1] + modS[i+1:]
                    i -= 1
                continue
            i += 1
        return modS
        