
'''
link : https://leetcode.com/problems/unique-paths/

62. Unique Paths
Medium

8093

281

Add to List

Share
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 
https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
Accepted
874,362
Submissions
1,468,608

'''

'''
Sol 1:
Using DP
TC :O(m*n)
SC : O(m*n)
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp =[[0 for i in range(n)] for i in range(m)]
        
        for i in range(n):
            dp[0][i]=1
        
        for i in range(m):
            dp[i][0]=1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]
    
        


'''
Sol 2:

Improvement to below ones 
Using dynamic programming

TC:O(mxn)
SC:O(mxn)
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_list=[[-1 for i in range(n)] for i in range(m)]
        return self.traverse(0,0,m,n,dp_list)
    
    def traverse(self,cr,cc,m,n,dp_list):
        local_cnt=0
        if((cr==m-1) and (cc==n-1)):
            return 1
        
        if cc>=n or cr >=m:
            return 0
        if dp_list[cr][cc] != -1:
            return dp_list[cr][cc]
        
        else:
            dp_list[cr][cc]=self.traverse(cr,cc+1,m,n,dp_list)+self.traverse(cr+1,cc,m,n,dp_list)
        return dp_list[cr][cc]
        #print("r,c ",cr," ",cc)
        #print(local_cnt)
        #return local_cnt
        

'''
Sol 3 :

Recusive solution traverse across the matrix and 
count the unique paths
TC: exponential
SC:O(1)
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.traverse(0,0,m,n)
    
    def traverse(self,cr,cc,m,n):
        local_cnt=0
        if((cr==m-1) and (cc==n-1)):
            return 1
        
        if cc<n-1:
            local_cnt+=self.traverse(cr,cc+1,m,n)
        
        if cr<m-1:
            local_cnt+=self.traverse(cr+1,cc,m,n)
        #print("r,c ",cr," ",cc)
        #print(local_cnt)
        return local_cnt
        
