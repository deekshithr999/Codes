'''
Iterative Approach

'''


def PrintSubsets(lst):
    for i in range(0,(1<<len(lst))):
        tlst =[]
        for j in range(len(lst)):
            if i & (1<<j):
                tlst.append(lst[j])
        print (tlst)

    return



if __name__=="__main__":
    lst =list(map(int,input().split()))
    PrintSubsets(lst)
