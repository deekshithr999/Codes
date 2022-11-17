
def fact(n):
    if n==1 or n==0:
        return 1
    
    return n*fact(n-1)

def kthpermutation(n,k):
    reslst=[]
    index=n
    lst=[1]*(n+1)
    while index>0:

        quot= int(k/fact(index-1))
        rem= k%fact(index-1)
        it=0
        cnt=0
        if rem==0:
            while cnt<quot:
                it+=1
                if lst[it]:
                    cnt+=1
            
            lst[it]=0
            reslst.append(it)
            it=n
            while it>0:
                print("making it happy")
                if lst[it]:
                    reslst.append(it)
                    lst[it]=0
                
                it-=1
            print("breakkk")
            break
        print("it ",it)
        while cnt<quot+1:
            it+=1
            print("it :",it," ",lst)
            if lst[it]:
                print("cnt :",cnt)
                cnt+=1
        lst[it]=0
        k-=quot*fact(index-1)
        reslst.append(it)
        index-=1
    return reslst

        
                


        






if __name__=="__main__":

    n,k= list(map(int,input("Enter n, k").split()))
    kth = kthpermutation(n,k)
    print(k,"th perm of ",n, kth)