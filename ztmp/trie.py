

class Node:
    def __init__(self):
        self.array = [None]*11
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insertNum(self, num):
        iterNode = self.root
        for idx,cn in enumerate(str(num)):
            n = int(cn)
            if not iterNode.array[n]:
                iterNode.array[n]=Node()
            if idx == len(str(num))-1:
                iterNode.array[n].isEnd = True
            iterNode = iterNode.array[n]
        print(f'Number{num} Inserted')
        return 
    
    def isPresent(self, num):
        iter = self.root
        stNum = str(num)
        for idx,cn in enumerate(stNum):
            n = int(cn)
            if not iter.array[n]:
                return False
            if idx == len(stNum)-1 and not iter.array[n].isEnd:
                return False
            iter = iter.array[n]
        return True


if __name__ == "__main__":

    num = int(input("Enter num: "))
    TrieRoot = Trie()
    TrieRoot.insertNum(num)
    fnum = int(input("Enter num to search: "))
    
    print("Number present: ", TrieRoot.isPresent(fnum))

            
