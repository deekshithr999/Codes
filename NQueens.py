'''
Link : https://leetcode.com/problems/n-queens/
51. N-Queens
Hard

5958

153

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
Accepted
372,229
Submissions
642,576

'''

#########################################################

'''
TC : O(n*n)
SC : O(n*n)

'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        reslst=[]
        curr=[""]*n
        self.letsPlay(curr,0,n,reslst)
        print(reslst)
        return reslst
        
        
    def canAdd(self,lst:List[str],row,col,n):
        
        for i in range(row-1, -1, -1):
            if lst[i][col]=='Q':
                return False
        #check diag lef
        
        i=row-1
        j=col-1
        
        while i>=0 and j>=0:
            if lst[i][j]=='Q':
                return False
            i-=1
            j-=1
        i=row-1
        j=col+1
        
        while i>=0 and j<n:
            if lst[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True
    
    def letsPlay(self, curr, crow, n, res):
        if crow==n:
            res.append(curr.copy())
            #print(res)
            #print(curr)
            return
        
        for j in range(n):
            if self.canAdd(curr,crow,j,n):
                #print ("Can Add for ", crow+1," ",j+1)
                curr[crow]="."*j+"Q"+"."*(n-j-1)
                self.letsPlay(curr,crow+1,n,res)
            else:
                pass