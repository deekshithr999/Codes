

def reverse_words(st1:str):
    l,r = 0,0
    rev_str=""

    while r<len(st1):
        while r<len(st1) and st1[r]!=" ":
            r+=1
        #reverse
        for i in range(r-1,l-1,-1):
            rev_str= rev_str+st1[i]
        rev_str += " "
        l=r+1
        r=r+1
    return rev_str

def reverse_words2(st1:str):
    l,r = 0,0
    rev_str = ""

    while True:
        if r >= len(st1):
            print("Broke")
            break

        while r<len(st1) and st1[r]!=" ":
            r+=1
        
        for i in range(r-1,l-1,-1):
            rev_str += st1[i]
            #print(rev_str)
        
        rev_str += " "
        r+=1
        l=r
    return rev_str





if __name__=="__main__":
    st = input()
    print ("Before : ", st)
    st2 = reverse_words2(st)
    print ("After  : ", st2)
