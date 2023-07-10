'''
https://practice.geeksforgeeks.org/problems/number-of-distinct-subsequences0909/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


Recursion

TC: O(2^n)
SC: O(2^n*n) #check
'''

class CntDistinctSubSeq_Rec(object):

    def __init__(self):
        pass

    def cnt_dist_sseq(self, txt1 :str) -> int:
        st =set()
        nsseq = self.cnt_through_recurse(txt1,"", 0, st)
        #print(st)
        print("SSeq = ", len(st))

    
    def cnt_through_recurse(self, txt1:str, gen_txt: str, curr_idx: int, store: set) -> int:

        if curr_idx == len(txt1):
            #print(len(store))
            return

        store.add(gen_txt)
        self.cnt_through_recurse(txt1, gen_txt, curr_idx+1,store )
        store.add(gen_txt+txt1[curr_idx])
        self.cnt_through_recurse(txt1, gen_txt+txt1[curr_idx], curr_idx+1,store)



'''
Through Iteration

TC : O(2^n)
SC : O(2^n*n)
'''
class CntDistinctSubSeq_Iter(object):

    def __init__(self):
        pass

    def cnt_dist_sseq(self, txt1 :str) -> int:
        st =set()
        self.cnt_through_iter(txt1,st)
        #print(st)
        print("SSeq = ", len(st))
    
    def cnt_through_iter(self, txt1: str, st) -> int:

        #
        for i in range(1<<len(txt1)):
            tmp_txt = ""
            for j in range(len(txt1)):
                if i & (1 << j):
                    tmp_txt += txt1[j]
            st.add(tmp_txt)
        
        #print(st)
        print(len(st))
        return 


'''
Dynamic Programming
TC: O(n)
SC: O(n)
'''

class CntDistinctSubSeq_dyanmic_prog(object):

    def __init__(self):
        pass

    def cnt_dist_sseq(self, txt1 :str) -> int:   
        nsseq = self.cnt_through_dynamic(txt1)
        #print(st)
        print("SSeq = ", nsseq) 
    
    def cnt_through_dynamic(self, txt1 :str):

        lst = [0]*len(txt1) #storing counts
        lst[0]=2
        dt = {txt1[0]:0} # storing indexes
        dt.update({'.':1})
        for i in range(1,len(txt1)):
            #print(lst[-1])
            lst[i] = 2*lst[i-1]
            #print(dt.get(txt1[i],-1))
            if dt.get(txt1[i],-1)!=-1:
                if dt.get(txt1[i],-1)!=0:
                    lst[i] = lst[i] - lst[dt.get(txt1[i])-1]
                else:
                    lst[i] = lst[i] - 1
            dt[txt1[i]]=i
        #print(lst)
        print ("Dynamic prog res: ", lst[len(txt1)-1])
        return lst[len(txt1)-1]%(pow(10,9)+7)


    


if __name__ == "__main__":

    csseq1 = CntDistinctSubSeq_Rec()
    csseq2 = CntDistinctSubSeq_Iter()
    csseq3 = CntDistinctSubSeq_dyanmic_prog()
    txt = input()
    #csseq1.cnt_dist_sseq(txt)
    #csseq2.cnt_dist_sseq(txt)
    csseq3.cnt_dist_sseq(txt)
