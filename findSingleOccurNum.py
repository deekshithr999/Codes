
def twonumoccur(lst):

    res_xor=0
    for num in lst:
        res_xor=res_xor^num
    

    if res_xor ==0:
        print("Hell!! all are duplicates")
    
    else:
        lst_zero=[]
        lst_one=[]

        ath_bit=100

        for i in range(32):

            if(res_xor & 1<<i):
                ath_bit=i
                break
        

        for num in lst:

            if(num & 1<<ath_bit):
                lst_one.append(num)

            else:
                lst_zero.append(num)

        res_one_xor=res_zero_xor=0

        for num in lst_one:
            res_one_xor=res_one_xor^num

        for num in lst_zero:
            res_zero_xor=res_zero_xor^num
        
        print("Two singles in the list are : ",res_one_xor," ",res_zero_xor)





if __name__ == "__main__":
    lst =list(map(int,input().split()))
    twonumoccur(lst)