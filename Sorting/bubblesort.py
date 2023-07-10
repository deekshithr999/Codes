
'''
TC : O(N^2)
SC : O(1)
'''
def bubblesort(lst):
    tlst = lst[:]
    print("id lst",id(lst)," id(tlst):",id(tlst))

    for i in range(len(tlst)-1):
        for j in range(len(tlst)-1):
            if tlst[j]>tlst[j+1]:
                tlst[j],tlst[j+1] = tlst[j+1],tlst[j]
    
    print("sorted tlst :", tlst)


'''
Improved bubble sort
TC : O(N^2)
SC : O(1)
'''

def improved_bubble_sort(lst):
    import copy
    tlst = copy.copy(lst)
    print("id lst",id(lst)," id(tlst):",id(tlst))

    for i in range(len(tlst)-1):
        for j in range(len(tlst)-1-i):
            if tlst[j]>tlst[j+1]:
                tlst[j],tlst[j+1] = tlst[j+1],tlst[j]
    print("sorted tlst :", tlst)

if __name__ == "__main__":

    lst= list(map(int,input().split()))
    improved_bubble_sort(lst)