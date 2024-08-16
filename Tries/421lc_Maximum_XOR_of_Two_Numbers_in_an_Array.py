
class TrieNode:
    def __init__(self):
        self.arr = [None]*2
        self.val = -1
    

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):

        iNode = self.root
        for i in range(31, -1, -1):
            bit =  (num >> i) & 1 
            if iNode.arr[bit] is None:
                iNode.arr[bit] = TrieNode()
            iNode = iNode.arr[bit]
        iNode.val = num
    
    def searchMaxXORs(self, nums):
        maxXOR = 0
        for num in nums:
            ret = self.findMaxXOR(num)
            maxXOR = max(maxXOR, ret^num)
        return maxXOR
    
    def findMaxXOR(self, num):
        iNode = self.root

        for i in range(31, -1, -1):
            bit = (num >> i)  & 1
            if iNode.arr[bit^1]:
                iNode = iNode.arr[bit^1]
            else:
                iNode = iNode.arr[bit]
        res = iNode.val
        return res


        
class Solution:
    '''
    TC: O(32n)
    SC: no idea (2^32)
    '''
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = Trie()
        for num in nums:
            trie.insert(num)
        
        mxXOR = trie.searchMaxXORs(nums)
        return mxXOR