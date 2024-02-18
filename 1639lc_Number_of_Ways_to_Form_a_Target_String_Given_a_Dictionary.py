class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD_VAL = 10**9+7
        lst = [[0]*1000 for _ in range(26)]
        for w in words:
            for idx, l in enumerate(w):
                i = ord(l)-ord('a')
                lst[i][idx] += 1 #see see there see
        # print(lst)
        totWords = lst[ord(target[0]) - ord('a')][:]
        for i in range(1,1000):
            totWords[i] += totWords[i-1]
        
        for c in target[1:]:
            curr = [0]*1000
            pickedLst = lst[ord(c) -ord('a')]
            for i in range(1, 1000):
                curr[i] = (curr[i-1]+ totWords[i-1]*pickedLst[i])%MOD_VAL
            totWords = curr
        
        # print("totWords ", totWords)
        return totWords[-1]