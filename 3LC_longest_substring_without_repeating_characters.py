'''
TC : O(n)
SC: O(n)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx_len = 0
        front,back = 0,0
        dt = dict()

        for front in range(len(s)):
            if s[front] not in dt:
                mx_len = max(front-back+1, mx_len)
                dt[s[front]]=front
            else:
                if dt[s[front]] < back:
                    mx_len = max(front-back+1, mx_len)
                    dt[s[front]]=front
                    #continue
                else:
                    back = dt[s[front]]
                    back += 1
                    dt[s[front]]=front
        return mx_len


'''
TC: O(2n)
SC: O(n)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx_len = 0
        front, back = 0,0
        st = set()

        while front < len(s):
            if s[front] not in st:
                st.add(s[front])
                mx_len = max(front-back +1, mx_len)
                front += 1
            else:
                st.remove(s[back])
                back += 1
        return mx_len
        
        

'''
TC O(n^2)
SC O(n)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi_len = 0
        for i in range(len(s)):
            st = set()
            for j in range(i,len(s)):
                l = j-i +1
                st.add(s[j])
                if len(st) == l:
                    maxi_len = max(maxi_len, l)
        return maxi_len


'''
asdf
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi_len = 0
        front, back = 0,0

        for front in range(len(s)):
            if s[front] in s[back:front]:
                idx = s.find( s[front], back)
                back = idx +1
            else:
                maxi_len = max(maxi_len, front-back+1)
        
        return maxi_len
        
        