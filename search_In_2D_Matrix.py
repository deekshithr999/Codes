'''
Link : https://leetcode.com/problems/search-a-2d-matrix/

74. Search a 2D Matrix
Medium

6008

242

Add to List

Share
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
Accepted
651,300
Submissions
1,537,256
'''

'''
Sol 1:

Use the Binary search to find out the row of range in which target
exists and on the col wise search as well

Time Complexity :O(logm +logn)
Space Complexity: O(1)

'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Use Binary Search
        return self.bSearch(matrix,target,0,len(matrix)-1)
        
    
    def bSearch(self,matrix,target,top,bottom):
        
        while(top<=bottom):
                    
            mid_row=top + int((bottom-top)/2)

            if(target >=matrix[mid_row][0] and target<=matrix[mid_row][len(matrix[0])-1]):
                #do bsearch over the row 
                return self.bSearchOLst(matrix[mid_row],target,0,len(matrix[mid_row])-1)
            
            
            elif target<matrix[mid_row][0]:
                return self.bSearch(matrix,target,top,mid_row-1)
            elif target >matrix[mid_row][len(matrix[0])-1]:
                return self.bSearch(matrix,target,mid_row+1,bottom)
        return False
    
    def bSearchOLst(self,lst,target,left,right):
        
        mid=left+int((right-left)/2)
        while left<=right:
            
            if lst[mid]==target:
                return True
            elif target < lst[mid]:
                return self.bSearchOLst(lst,target,left,mid-1)
            
            else:
                return self.bSearchOLst(lst,target,mid+1,right)
            

'''
Sol 2 :

Use the Binary Search to find out the row in which the target range exists

Time Complexity : O(log(m)+n)
Space Complexity: O(1)

'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Use Binary Search
        return self.bSearch(matrix,target,0,len(matrix)-1)
        
    
    def bSearch(self,matrix,target,top,bottom):
        
        while(top<=bottom):
                    
            mid_row=top + int((bottom-top)/2)

            if(target >=matrix[mid_row][0] and target<=matrix[mid_row][len(matrix[0])-1]):
                #do bsearch over the row or use iterative method
                for k in range(len(matrix[0])):
                    if matrix[mid_row][k]==target:
                        return True
                return False
            elif target<matrix[mid_row][0]:
                return self.bSearch(matrix,target,top,mid_row-1)
            elif target >matrix[mid_row][len(matrix[0])-1]:
                return self.bSearch(matrix,target,mid_row+1,bottom)
        return False
            
            
                

'''
Sol 3:
Find the row in which a target exists in the range

Time Complexity : O(m +n)
Space Complexity: O(1)

'''
# Time Complexity :O(m+n)
#space Complexity : O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if target>=matrix[i][0] and target<=matrix[i][len(matrix[0])-1]:
                for j in range(len(matrix[0])):
                    if matrix[i][j]==target:
                        return True
            
        
        return False
        

'''
Sol 4 :

Run the iterative approach on the whole matrix and check for the target

Time Complexity : O(mxn)
Space Complexity: O(1)

'''