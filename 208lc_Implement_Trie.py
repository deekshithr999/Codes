

class TrieNode:
    '''
    dictionary (or) HashMap implementation
    '''
    def __init__(self):
        self.children = {}
        self.eow = False
class Trie:

    def __init__(self):
        self.trieRoot = TrieNode()
    
    def insert(self, word: str) -> None:
        currNode = self.trieRoot
        for l in word:
            if l not in currNode.children:
                currNode.children[l]=TrieNode()
            currNode = currNode.children[l]
        currNode.eow = True

    def search(self, word: str) -> bool:
        currNode = self.trieRoot
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        if not currNode.eow:
            return False
        return True
        
    def startsWith(self, prefix: str) -> bool:
        currNode = self.trieRoot
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)




class Node:
    def __init__(self):
        self.lst = [None]*26
        self.isWord = False
        # self.next = None


class Trie:
    '''
    Array Implementation
    '''

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        tnode = self.root
        for idx, letter in enumerate(word):
            chr_idx = ord(letter)-ord('a')
            if tnode.lst[chr_idx] is None:
                tnode.lst[chr_idx]=Node()
            if idx == len(word)-1:
                tnode.lst[chr_idx].isWord = True
            tnode = tnode.lst[chr_idx]
        

    def search(self, word: str) -> bool:
        tnode = self.root
        for idx, letter in enumerate(word):
            chr_idx = ord(letter)-ord('a')
            if not tnode.lst[chr_idx]:
                return False
            if idx == len(word)-1 and not tnode.lst[chr_idx].isWord :
                return False
            tnode = tnode.lst[chr_idx]
        return True

    def startsWith(self, prefix: str) -> bool:
        tnode = self.root
        for idx, letter in enumerate(prefix):
            chr_idx = ord(letter)-ord('a')
            if not tnode.lst[chr_idx]:
                return False
            tnode = tnode.lst[chr_idx]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)