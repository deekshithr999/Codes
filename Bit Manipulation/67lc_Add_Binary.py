'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a,b = b,a
        b = "0"*(len(a)-len(b))+b
        res = ""
        carry =0
        for i in range(len(a)-1,-1,-1):
            a1,b1 = int(a[i]), int(b[i])
            tot = a1+b1+carry
            carry = 1 if tot >1 else 0
            tot = tot%2 #chee dis
            res = str(tot)+res
        if carry:
            res = "1"+res
        return res


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        if len(a)< len(b):
            a,b = b,a
        i1, i2 = len(a)-1, len(b)-1
        carry = 0

        while i2 >=0:
            tot = int(a[i1])+int(b[i2])+carry
            carry = 0
            if tot>1:
                carry = 1
            tot = tot%2
            res = str(tot)+res
            i1, i2 = i1-1, i2-1

        while i1 >=0:
            tot = int(a[i1])+carry
            carry = 0
            if tot>1:
                carry =1
            tot = tot%2
            res = str(tot)+res
            i1 -=1
        if carry:
            res = "1"+res
        return res 
