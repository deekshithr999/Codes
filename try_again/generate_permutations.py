

class Permutations(object):

    def __init__(self):
        pass

    def generate_permutations(self, lst:list, curr_idx):

        if curr_idx == len(lst)-1:
            print(lst)
            return
        else:

            for i in range(curr_idx,len(lst)):
                lst1 =lst[:]
                lst1[i],lst1[curr_idx] = lst1[curr_idx],lst1[i]
                self.generate_permutations(lst1,curr_idx+1)
        return 




if __name__ == "__main__":

    lst = list(map(int,input().split()))
    perm = Permutations()
    perm.generate_permutations(lst,0)