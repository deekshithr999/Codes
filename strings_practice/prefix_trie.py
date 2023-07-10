

class TrieNode:

    def __init__(self):
        self.array = [None]*26
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = None
    
    def get_idx (self, letter):
        return ord(letter) - ord('a')

    def insert_into_trie(self,word): #insert word into the tried

        if self.root is None:
            self.root = TrieNode()
        
        trav_trie = self.root

        for i in range(len(word)):
            letter = word[i]
            idx = self.get_idx(letter)
            if trav_trie.array[idx] == None:
                tmp_trie = TrieNode()
                trav_trie.array[idx]=tmp_trie
            
            if i == len(word)-1:
                trav_trie.array[idx].is_word = True  
            trav_trie = trav_trie.array[idx]
        return
    
    def print_words_in_trie(self, trav_trie, word):

        for i in range(26):
            tword = word
            if trav_trie.array[i] != None:
                tword = tword + chr(ord('a')+i)
                if trav_trie.array[i].is_word:
                    #print("is word : ", tword)
                    print(tword)
                    
                self.print_words_in_trie(trav_trie.array[i], tword)
        
        return
    
    def print_longest_prefix_match(self, trav_trie, word):

        if trav_trie is None:
            return word
        #check array > 1 letter return
        cnt = 0
        idx = -1
        for i in range(26):
            if trav_trie.array[i]:
                cnt += 1
                idx =i
        
        if cnt == 0 or cnt > 1:
            return word
        
        word = word + chr(ord('a')+idx)
        #print("word : ", word)
        if trav_trie.array[idx].is_word :
            return word

        return self.print_longest_prefix_match(trav_trie.array[idx],word) #name confusion

        


if __name__ == "__main__":

    n = int(input("n strs\n"))
    lst=[]

    for i in range(n):
        lst.append(input())
    trie = Trie()

    for i in range(len(lst)):
        trie.insert_into_trie(lst[i])
    
    print("Printing :")

    trie.print_words_in_trie(trie.root, "")

    print(" Longest Prefix matched : ", trie.print_longest_prefix_match(trie.root, ""))


    


            
