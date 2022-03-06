
def permutation(lst,curr):
    if curr==len(lst):
        print(lst)
        return

    for i in range(curr,len(lst)):
        t_lst=lst.copy()
        t_lst[curr],t_lst[i]=t_lst[i],t_lst[curr]
        permutation(t_lst,curr+1)



if __name__=="__main__":
    lst =list(map(int,input("enter the list:").split()))
    permutation(lst,0)
