
'''
TC : O(n^2) + O(nlogn)
SC : O(n^2)
'''

class KMaxSumCombinations_BruteForce:

    def __init__(self):
        pass

    def kmaxsumcomb(self, lst1, lst2, kcomb):
        comb_lst = []

        for i in range(len(lst1)):
            for j in range(len(lst2)):
                comb_lst.append(lst1[i]+lst2[j])
        
        comb_lst.sort(reverse = True)
        return comb_lst[:kcomb]
        


'''
Sorting the elems & storing in an Array

'''

class KMaxSumCombinations_Array_DPkind:

    def __init__(self):
        pass

    def kmaxsumcomb(self, lst1, lst2, kcomb):
        lst1.sort(reverse = True)
        lst2.sort( reverse = True)
        res_lst = list()

        # store till which value've been used...

        tracker = [0]*len(lst1)

        for curr_comb in range(kcomb):
            l1mx, l2mx =0,0
            prev_mx = -1
            for i in range(len(lst1)):
                if tracker[i] < len(lst1) and prev_mx < lst1[i]+lst2[tracker[i]]:
                    l1mx, l2mx = i, tracker[i]
                    prev_mx = lst1[i]+lst2[tracker[i]]
            
            res_lst.append(prev_mx)
            tracker[l1mx] = l2mx+1
        return res_lst


'''
 TC : O(n**2)+O(n**2logn**2)
'''               

class KMaxSumCombinations_min_pq_heap:

    def __init__(self):
        pass

    def create_heap(self, lst):
        self.heapify_min(lst)

    def swap(self, lst, idx1, idx2):
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    
    def heapify_min(self, lst):
        idx = len(lst) -1
        while idx > 0:
            if idx %2 == 0: #2 childs
                if lst[idx] < lst[idx-1]:
                    if lst[idx] < lst[(idx -1)//2]:
                        self.swap(lst, idx, (idx -1)//2)
                else:
                    if lst[idx-1] < lst[(idx-1)//2]:
                        self.swap(lst, idx-1, (idx-1)//2)

            else : #1 child
                if lst[idx] < lst[(idx-1)//2]:
                    self.swap(lst, idx, (idx-1)//2)
            idx -=1
        return
    
    def kmaxsumcomb(self, lst1, lst2, kcomb):
        pq = [-1]*kcomb

        for i in range(len(lst1)):
            for j in range(len(lst2)):
                if pq[0] < lst1[i]+lst2[j]:
                    pq.pop(0)
                    pq.append(lst1[i]+lst2[j])
                    self.heapify_min(pq)
        return sorted(pq, reverse=True)
   

class KMaxSumCombinations_Optimized_pq_Final:
       
    def __init__(self):
        pass

    def kmaxsumcomb(self, lst1, lst2, kcomb):
        import heapq
        tracker_set = set()
        lst1.sort(reverse = True)
        lst2.sort(reverse = True)
        res_lst=[]
        pque = [(-(lst1[0]+lst2[0]),(0,0))]
        tracker_set.add((0,0))
        curr_comb = 0

        while curr_comb < kcomb:
            lstlen = len(lst1)
            topele = heapq.heappop(pque)
            #print(topele)
            res_lst.append(-topele[0])
            curr_comb += 1
            i,j = topele[1][0], topele[1][1]

            if i+1 <lstlen and ((i+1,j) not in tracker_set):
                heapq.heappush(pque, (-(lst1[i+1]+lst2[j]),(i+1,j)))
                tracker_set.add((i+1,j))
            
            if j+1 < lstlen and ((i, j+1) not in tracker_set):
                heapq.heappush(pque, (-(lst1[i]+lst2[j+1]),(i,j+1)))
                tracker_set.add((i,j+1))
        return res_lst

if __name__ == "__main__":
    kmxcomb_bf = KMaxSumCombinations_BruteForce()
    kmxcomb_dp = KMaxSumCombinations_Array_DPkind()
    kmxcomb_hp = KMaxSumCombinations_min_pq_heap()
    kmxcomb_hf = KMaxSumCombinations_Optimized_pq_Final()
    kcomb = int(input())
    lst1 = list(map(int,input().split(',')))
    lst2 = list(map(int, input().split(',')))
    print("BF : ",kmxcomb_bf.kmaxsumcomb(lst1[:], lst2[:], kcomb))
    print("DP : ",kmxcomb_dp.kmaxsumcomb(lst1[:], lst2[:], kcomb))
    print("hp : ", kmxcomb_hp.kmaxsumcomb(lst1[:], lst2[:], kcomb))
    print("hF : ", kmxcomb_hf.kmaxsumcomb(lst1[:], lst2[:], kcomb))





