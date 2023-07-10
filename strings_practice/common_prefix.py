
def comm_pref(lst:list):
    fstr=""
    ch =""
    j = 0

    for k in range(len(lst[0])):
        for i in range(len(lst)):

            if j< len(lst[i]):
                if i ==0:
                    ch = lst[i][j]
                if ch !=lst[i][j]:
                    break
            else:
                break
            if i==len(lst)-1:
                fstr +=ch
                j+=1
    return fstr

def comm_pref2(lst:list):
    j=0
    fstr=""

    while j < len(lst[0]):
        ch = ""
        for i in range(len(lst)):
            if j<len(lst[i]):
                if i == 0:
                    ch = lst[i][j]
                if lst[i][j] != ch:
                    break

                if i == len(lst)-1:
                    fstr += ch
            else:
                break
        j+=1
    return fstr

def comp_div_conq(st1:str, st2:str):
    fstr = ""
    mlen = mini(len(st1),len(st2))
    j = 0
    while j < len(mlen):
        if st1[j]==st2[j]:
            fstr = st1[j]
        else:
            break
    return fstr


def div_div_conq(lst:list[str], left, right):
    if left<right:
        mid = left + (right-left)//2
        st1 = div_div_conq(lst, left, mid)
        st2 = div_div_conq(lst, mid+1, right)
        return comp_div_conq(st1,st2)
    if left == right:
        return lst[left]



def comm_pref_div_conq(lst:list[str]):
    return div_div_conq(lst,0,len(lst)-1)


if __name__ == "__main__":
    lst = []
    n = int(input("n strs"))
    for i in range(n):
        lst.append(input())
    
    print("Comm Pref :",comm_pref(lst))
    print("Comm Pref2:",comm_pref2(lst))
    print("Comm pref div: ", comm_pref_div_conq(lst))
