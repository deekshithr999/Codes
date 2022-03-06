'''
link : https://leetcode.com/problems/powx-n/


50. Pow(x, n)
Medium

3951

4990

Add to List

Share
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104


'''

# check the range of the Integer values
'''
Sol 4 :

Similar to Sol2 except using the bit wise operator

Time :O(logn)
Space :O(1)

'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n==0:
            #print("comes here")
            return 1
        elif n <0:
            return 1/(self.myPow(x,-1*(n+1))*x)
        
        elif (n & 1):
            #print("x is :",x)
            return self.myPow(x,n-1)*x
        
        else :
            return self.myPow(x*x,n>>1)
        
        


'''
Sol  3: 

optimization of the Sol 2

instead of doing x^2 : get tval= X^(n/2)
and do  tval =tval*2

Time Complexity : O(logn)
Space Complexity : O(1)
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n>0:
            
            if n==1:
                return x

            elif n%2==0:
                tval=self.myPow(x,n/2)
                return tval*tval
            
            else :
                return x*self.myPow(x,n-1)
        
        elif n<0:
            if n==1:
                return 1/x
            
            elif n%2 ==0:
                tval =self.myPow(x,n/2)
                return tval*tval
            else :
                return (1/x)*self.myPow(x,n+1)
        
        else :
            return 1

'''
Sol 2:

Break the computation to do half power 
ie. X^n= (X^2)^(n/2)

Time Complexity : O(logn)
Space Complexity : O(1)

'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n>0:
            
            if n==1:
                return x

            elif n%2==0:
                return self.myPow(x*x,n/2)
            
            else :
                return x*self.myPow(x,n-1)
        
        elif n<0:
            if n==1:
                return 1/x
            
            elif n%2 ==0:
                return self.myPow(x*x,n/2)
            else :
                return (1/x)*self.myPow(x,n+1)
        
        else :
            return 1





'''
sol 1:

do the iteration on each power

Time Complexity : O(n)
Space Complexity : O(1)

'''