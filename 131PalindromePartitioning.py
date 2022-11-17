'''
Link : https://leetcode.com/problems/palindrome-partitioning/
131. Palindrome Partitioning
Medium

6627

208

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
Accepted
451,380
Submissions
757,434

'''

##########################################################

'''

'''

class Solution:
    def ispalindrome(self,s):
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        currlst,final_lst=[],[]
        self.palinpartition(s,0,currlst,final_lst)
        return final_lst
    
    def palinpartition(self,s,start_idx,currlst,final_lst):
        
        if start_idx==s.__len__(): #len(s)
            final_lst.append(currlst)
            return
        
        for k in range(start_idx,len(s)):
            ss = s[start_idx: k+1]
            if (self.ispalindrome(ss)):
                tcurrlst = currlst.copy()
                tcurrlst.append(ss)
                self.palinpartition(s,k+1,tcurrlst,final_lst)
        return 