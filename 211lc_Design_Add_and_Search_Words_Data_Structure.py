class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.trieRoot
        for c in word:
            if c not in currNode.children:
                currNode.children[c]=TrieNode()
            currNode = currNode.children[c]
        currNode.eow = True

    def search(self, word: str) -> bool:

        def recSearch(word, curr_idx, currNode): #->bool
            if curr_idx == len(word):
                if currNode.eow:
                    return True
                return False
            if word[curr_idx] != ".":
                if word[curr_idx] in currNode.children:
                    currNode = currNode.children[word[curr_idx]]
                    return recSearch(word, curr_idx+1, currNode)
                else:
                    return False
            else:
                for key,val in currNode.children.items():
                    if  recSearch(word, curr_idx+1, val):
                        return True 
                return False
        return recSearch(word, 0, self.trieRoot)
                    

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)