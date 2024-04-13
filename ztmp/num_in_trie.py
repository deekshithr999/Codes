
'''
Now we are goingg to implement a trie block to store phone numbers
'''

class Node:
    def __init__(self):
        self.isValid = False
        self.arr = [None]*10

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insertNum(self, number):
        numStr = str(number)
        iterNode = self.root
        for idx, nc in enumerate(numStr):
            n = int(nc)
            if not iterNode.arr[n]:
                iterNode.arr[n]= Node()
            if idx == len(numStr)-1:
                iterNode.isValid = True
            iterNode = iterNode.arr[n]
    
    def searchNum(self, number):
        numStr = str(number)
        iter = self.root
        for idx, nc in enumerate(numStr):
            n = int(nc)
            if not iter.arr[n]:
                return False
            if idx == len(numStr)-1 :
                return iter.isValid
            iter = iter.arr[n]
        return True

                

if __name__ == "__main__":
    numBook = Trie()
    while True:
        print("num ?? type end for ending")
        num = int(input())
        if num == "end":
            break
        print("1. Insert \n 2. Search ?")
        op = int(input())
        if op == 1:
            numBook.insertNum(num)
            print("inserted !!")
        else:
            if numBook.searchNum(num):
                print("num Exists")
            else:
                print("Dangg no found")




