
'''
Dynamic Programming
TC : O(m*n)
SC : O(m*n)
'''

class LongestCommSubSeq_DynamicProg(object):

    def __init__(self):
        pass
    
    def longcommsubseq(self, st1: str, st2: str) -> int:
        return self.compute_longsubseq(st1, st2)
    
    def compute_longsubseq(self, st1: str, st2: str) -> int:

        mat = [[0 for i in range(len(st2)+1)] for i in range(len(st1)+1)]
        for i in range(1, len(st1)+1):
            for j in range(1, len(st2)+1):
                if st1[i-1] == st2[j-1]:
                    mat[i][j] = mat[i-1][j-1]+1
                else:
                    mat[i][j] = max(mat[i-1][j], mat[i][j-1])
        
        return mat[len(st1)][len(st2)]


'''
Brute Force Approach

'''

class LongestCommSubSeq_Recursive(object):

    def __init__(self):
        pass
    def longcommsubseq(self, st1: str, st2: str) -> int:
        return self.compute_longsubseq(st1, st2, 0, 0)

    def compute_longsubseq(self, st1: str, st2: str, st1_idx :int, st2_idx :int) -> int:

        if  st1_idx == len(st1) or st2_idx == len(st2):
            return 0
        
        if st1[st1_idx] == st2[st2_idx]: #how to ignoremax both???
            return self.compute_longsubseq(st1, st2, st1_idx+1, st2_idx+1)+1


        return max(self.compute_longsubseq(st1, st2, st1_idx+1, st2_idx),
                    self.compute_longsubseq(st1, st2, st1_idx, st2_idx+1))
    

if __name__ == "__main__":

    st1 = input()
    st2 = input()

    lss1 = LongestCommSubSeq_DynamicProg()
    lss2 = LongestCommSubSeq_Recursive()

    print(lss1.longcommsubseq(st1, st2))
    print(lss2.longcommsubseq(st1, st2))



