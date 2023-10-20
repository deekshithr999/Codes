
'''
https://leetcode.com/problems/valid-parentheses/description/
'''

class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def isValid(self, s: str) -> bool:
        st = list()
        match = {
            ')':'(',
            '}':'{',
            ']':'['
          }
        for ele in s:
            if ele in match.values():
                st.append(ele)
            elif len(st)== 0 or match[ele]!=st.pop():
                return False
        if len(st)!=0:
            return False
        return True
        