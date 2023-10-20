
class Solution:
    '''
    TC: O(n)
    Sc: O(1)
    '''
    def isPalindrome(self, s: str) -> bool:
        tmpstr = s.lower()
        start = 0
        end = len(s)-1
        while start < end:
            if tmpstr[start].isalnum() == False:
                start +=1
            elif tmpstr[end].isalnum()==False:
                end -=1
            else:
                if tmpstr[start] != tmpstr[end]:
                    return False
                start +=1
                end -=1
        return True
        
class Solution:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def isPalindrome(self, s: str) -> bool:
        tmpstr = ""
        s = s.lower()
        for letter in s:
            if letter.isalnum():
                tmpstr += letter
        
        first = 0
        last = len(tmpstr)-1
        while first < last:
            if tmpstr[first] != tmpstr[last]:
                return False
            first += 1
            last -= 1
        return True
        