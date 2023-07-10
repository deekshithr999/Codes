

'''
Iterative
'''

class GenSubset01(object):

    def __init__(self):
        pass
    def gen_subset(self, bts):
        tot_ssets = 2**bts
        print(tot_ssets)
        for i in range(tot_ssets):
            txt = ""
            for j in range(bts):
                if i & (1 << j): # fffff upppp
                    txt = str(1)+txt
                else:
                    txt = txt + str(0)
            print(i," ",txt)
    
    def gen_subset2(self, bts):
         tot_ssets = 1 << bts

         for i in range(tot_ssets):
            txt = ""
            for j in range(bts):
                if i & (1 << j):
                    txt = str(1) +txt
                else:
                    txt = str(0) + txt
            print(txt)


'''
Recursive
'''

class GenSubsetRecursion01(object) :

    def __init__(self):
        pass

    def subset(self:object, bts :int) -> None:
        self.subset_rec(bts, 0, "")
    

    def subset_rec(self, bts :int, curr_idx :int, txt :str) -> None:
        if curr_idx == bts:
            print(txt)
            return
        
        self.subset_rec(bts, curr_idx+1, "0"+txt)
        self.subset_rec(bts, curr_idx+1, "1"+txt)


'''
Iterative Approach with Numbers
'''

class GenSSetwnum(object):

    def __init__(self):
        pass

    def subset(self, lst :list):
        npowset = 1 << len(lst)
        for i in range(npowset):
            tmp = []
            for j in range(len(lst)):
                if i & (1 << j):
                    tmp.append(lst[j])
            print(tmp)
        return


'''
Recursive Approach
'''
class GenSSetwnumRec(object):

    def __init__(self):
        pass

    def subset(self, lst :list):
        self.subset_recur(lst, 0, [])
    
    def subset_recur(self :GenSSetwnum, lst :list, curr_idx :int, rlst :list ) -> None:
        if curr_idx == len(lst):
            print(rlst)
            return 
        #tlst = rlst[:] # creating new array takes up more space.
        #tlst.append(lst[curr_idx])
        rlst.append(lst[curr_idx]) #instead use the same array & remove the last element
        self.subset_recur(lst, curr_idx+1, rlst)
        rlst.pop(len(rlst)-1) #list.pop(index)
        self.subset_recur(lst, curr_idx+1, rlst)




if __name__ == "__main__":

    #gsset = GenSubset()
    #gsset_rec = GenSubsetRecursion01()
    #bts = int(input())
    #gsset.gen_subset2(bts)
    #gsset_rec.subset(bts)
    lst = list(map(int, input().split()))
    gssnum = GenSSetwnumRec()
    gssnum.subset(lst)



        

