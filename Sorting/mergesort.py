'''
TC: O(nlogn)
SC: O(n)

'''
class mergesort():

    def mergesort(self, lst:list, left:int,right:int):
        if(left < right):
            mid = left+(right-left)//2
            self.mergesort(lst, left, mid)
            self.mergesort(lst, mid+1, right) #Handling edge case
            self.merge(lst, left, mid, right)
    
    def merge(self, lst:list, left:int, mid:int, right:int):

        tlst:int = []
        il = left
        ir = mid+1
        while il<=mid and ir<=right:
            if lst[il] <lst[ir]:
                tlst.append(lst[il])
                il+=1
            else:
                tlst.append(lst[ir])
                ir+=1
        
        if il>mid:
            while ir<=right:
                tlst.append(lst[ir])
                ir+=1
        
        if ir>right:
            while il<=mid:
                tlst.append(lst[il])
                il+=1
        
        for it in range(len(tlst)):
            lst[left+it]=tlst[it]



class mergesort2():

    def mergesort(self, lst:list, left:int,right:int):
        if(left < right):
            mid = left+(right-left)//2
            self.mergesort(lst, left, mid)
            self.mergesort(lst, mid+1, right) #Handling edge case
            self.merge(lst, left, mid, right)
    
    def merge(self, lst:list, left:int, mid:int, right:int):

        tlst:int = [0]*(right-left+1)
        cidx = -1
        il = left
        ir = mid+1
        while il<=mid and ir<=right:
            cidx+=1
            if lst[il] <lst[ir]:
                tlst[cidx] = lst[il]
                il+=1
            else:
                tlst[cidx] = lst[ir]
                ir+=1
        
        if il>mid:
            while ir<=right:
                cidx +=1
                tlst[cidx] = (lst[ir])
                ir+=1
        
        if ir>right:
            while il<=mid:
                cidx +=1
                tlst[cidx] = (lst[il])
                il+=1
        
        for it in range(len(tlst)):
            lst[left+it]=tlst[it]

if __name__=="__main__":

    lst = list(map(int,input().split(',')))
    ms = mergesort()
    print(" BEF    :", lst)
    ms.mergesort(lst, 0, len(lst)-1)
    print("Sorted  :", lst)
