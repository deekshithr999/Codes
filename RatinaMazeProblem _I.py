'''
Link : https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is 
blocked.
Your Task:  
You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order. 
Note: In case of no path, return an empty list. The driver will output "-1" automatically.

Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

Constraints:
2 ≤ N ≤ 5
0 ≤ m[i][j] ≤ 1

'''

#################################################

'''
TC : O(4^(mxn))
SC : O(mxn)

'''
import copy
class Solution:
    def findPath(self, matrix, n):
        colmat=[0]*n
        trav_mat=[copy.deepcopy(colmat) for i in range(n)]
        cstr=""
        res=[]
        self.traverseMatrix(matrix,n,0,0,cstr,res,trav_mat)
        res=sorted(res)
        #print(res)
        return res
    
    
    def traverseMatrix(self,matrix,n,cr,cc,cstr,res,trav_matrix):
        if (cr==n-1 and cc==n-1):
            #print(cstr)
            if matrix[cr][cc]==1:
                res.append(cstr)
            
            return
        
        if cr<0 or cc<0:
            return
        if cc==n or cr==n:
            return
        if matrix[cr][cc]==0:
            return
        
        if trav_matrix[cr][cc]==0:
            
            #trav_cpy=copy.deepcopy(trav_matrix)
            trav_matrix[cr][cc]=1
            self.traverseMatrix(matrix,n,cr+1,cc,cstr+"D",res,trav_matrix)
            self.traverseMatrix(matrix,n,cr-1,cc,cstr+"U",res,trav_matrix)
            self.traverseMatrix(matrix,n,cr,cc+1,cstr+"R",res,trav_matrix)
            self.traverseMatrix(matrix,n,cr,cc-1,cstr+"L",res,trav_matrix)
            trav_matrix[cr][cc]=0
            return
        
        
        # code here
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends


#################################################

'''
TC : O(4^(nxm))
SC : O((n*m)x4^(n*m))
'''

#User function Template for python3


import copy
class Solution:
    def findPath(self, matrix, n):
        colmat=[0]*n
        trav_mat=[copy.deepcopy(colmat) for i in range(n)]
        cstr=""
        res=[]
        self.traverseMatrix(matrix,n,0,0,cstr,res,trav_mat)
        res=sorted(res)
        #print(res)
        return res
    
    
    def traverseMatrix(self,matrix,n,cr,cc,cstr,res,trav_matrix):
        if (cr==n-1 and cc==n-1):
            #print(cstr)
            if matrix[cr][cc]==1:
                res.append(cstr)
            return
        
        if cr<0 or cc<0:
            return
        if cc==n or cr==n:
            return
        if matrix[cr][cc]==0:
            return
        
        if trav_matrix[cr][cc]==0:
            
            trav_cpy=copy.deepcopy(trav_matrix)
            trav_cpy[cr][cc]=1
            self.traverseMatrix(matrix,n,cr+1,cc,cstr+"D",res,trav_cpy)
            self.traverseMatrix(matrix,n,cr-1,cc,cstr+"U",res,trav_cpy)
            self.traverseMatrix(matrix,n,cr,cc+1,cstr+"R",res,trav_cpy)
            self.traverseMatrix(matrix,n,cr,cc-1,cstr+"L",res,trav_cpy)
            return
        
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends