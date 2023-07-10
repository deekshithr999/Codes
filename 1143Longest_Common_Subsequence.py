
'''
https://leetcode.com/problems/longest-common-subsequence/

'''
class LongestSubsequence:

    def __init__(self):
        pass

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Handle diff lenghts
        # chill madi no problem in lengths
        #return self.tryLongSS3(text1, text2, 0, 0, 0)
        return self.tryLongSS5(txt1, txt2, 0, 0)
    
    def tryLongSS1(self, txt1, txt2):
        # fcked up, won't work bcz the problem is solved in SS2. Recursion doesn't play nicely in this case.
        mxlen = 0
        tlen = 0

        if len(txt1)> len(txt2):
            txt1, txt2 = txt2, txt1

        for k in range(len(txt1)):
            i = k
            j = 0
            tlen = 0
            while i < len(txt1):
                while j < len(txt2):
                    if txt1[i] == txt2[j]:
                        tlen += 1
                        mxlen = max(mxlen, tlen)
                        i += 1
                        j += 1
                        break                    
                    j += 1
        return mxlen
   
    '''
    Not sure of this solution
    1. First match First. Order doesn't matter
    2. inclusion exclusion type
    '''
    def tryLongSS2(self, text1, text2, t1_idx, t2_idx, curr_len):
        print("curr_len :", curr_len)
        if t1_idx == len(text1): #edge case
            return curr_len
        mxlen = curr_len
        # including the char
        for j in range(t2_idx, len(text2)):
            if text2[j] == text1[t1_idx]:
                #curr_len += 1        
                if j == len(text2)-1:
                    return curr_len+1 #Edge Case, fcked this up
                #J = j
                mxlen = max(self.tryLongSS2(text1, text2, t1_idx+1, j+1, curr_len+1),mxlen) #fcked up here
                break
        # excluding the char 
        mxlen = max(self.tryLongSS2(text1, text2, t1_idx+1, t2_idx, curr_len),mxlen)
        return mxlen 
    
    def tryLongSS3(self, txt1, txt2, t1idx, t2idx, mxlen ):

        if t1idx == len(txt1) or t2idx == len(txt2):
            return mxlen
        
        if txt1[t1idx] == txt2[t2idx]:
            return self.tryLongSS3(txt1, txt2, t1idx+1, t2idx+1, mxlen+1)
        
        else:
            #fairness, problem on both sides
            return max(self.tryLongSS3(txt1, txt2, t1idx+1, t2idx, mxlen), self.tryLongSS3(txt1, txt2, t1idx, t2idx+1, mxlen))
        

        return mxlen

    def tryLongSS4(self, txt1, txt2, t1idx, t2idx):

        if t1idx == len(txt1) or t2idx == len(txt2):
            return 0
        
        if txt1[t1idx] == txt2[t2idx]:
            return self.tryLongSS4(txt1, txt2, t1idx, t2idx)+1
        else:
            return max(self.tryLongSS4(txt1, txt2, t1idx+1, t2idx), self.tryLongSS4(txt1, txt2, t1idx, t2idx+1))
    
'''
Memoization
'''

class LongestSubsequence2:

    def __init__(self):
        pass
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.tryLongSS5(text1, text2, 0, 0)
    
    def tryLongSS5(self, txt1, txt2, t1idx, t2idx):
        matrix = [[-1]*(len(txt2)+1) for j in range(len(txt1)+1)]
        return self.tryLongSS51(txt1, txt2, 0, 0, matrix)
    
    def tryLongSS51(self, txt1, txt2, t1idx, t2idx, matrix):

        if (matrix[t1idx][t2idx] != -1 ):
            return matrix[t1idx][t2idx]
        
        # will be Redundant
        if t1idx == len(txt1) or t2idx == len(txt2):
            return 0
        
        if txt1[t1idx] == txt2[t2idx]:
            matrix[t1idx][t2idx] = self.tryLongSS51(txt1, txt2, t1idx+1, t2idx+1, matrix)+1
            return matrix[t1idx][t2idx]
        else:
            matrix[t1idx][t2idx] = max(self.tryLongSS51(txt1, txt2, t1idx+1, t2idx, matrix), self.tryLongSS51(txt1, txt2, t1idx, t2idx+1, matrix))
            return matrix[t1idx][t2idx]


'''
Dynamic Programming

'''

class LongestSubsequence3(object):
    def __init__(self):
        pass

    def longestCommonSubsequence(self, st1, st2):
        matrix = [[0]*(len(st2)+1) for i in range(len(st1)+1)] #this is moment u realize u hecked up.
        for i in range(1,len(st1)+1):
            for j in range(1, len(st2)+1):
                if st1[i-1]==st2[j-1]:
                    matrix[i][j]= matrix[i-1][j-1]+1
                else:
                    matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])
        
        return matrix[len(st1)][len(st2)]



if __name__ == "__main__":

    lss = LongestSubsequence3()
    st1 = input()
    st2 = input()
    print("LSS length : ", lss.longestCommonSubsequence(st1, st2))





        


