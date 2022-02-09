'''
Link : https://leetcode.com/problems/rotate-image/
Sol 1:

simply traverse the matrix and write the new matrix
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        matrix_copy =[]
        
        row=[0 for i in matrix[0]]
        print("row ",row)
        
        matrix_copy =[row[:] for i in range(len(matrix))]
        #print("matrix_copy ",matrix_copy)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix_copy[j][len(matrix)-1-i]=matrix[i][j]
                print( matrix_copy[j][len(matrix)-1-i])
    
        print(matrix_copy)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=matrix_copy[i][j]
        return matrix_copy

'''
Sol 2 :

Intuitive Approach :
step 1: Transpose the matrix
step 2: Reverse rows in the matrix
=> matrix rotated by 90'degrees
'''           
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # Reverse the rows
        
        for i in range(len(matrix)):
            for j in range(int(len(matrix)/2)):
                matrix[i][j],matrix[i][len(matrix)-1-j]=matrix[i][len(matrix)-1-j],matrix[i][j]



'''
Sol 3:

update one element each by traversing in circular order and
step into the inner circle of the matrix



Time Complexity : O(n^2)
Space Complexity:O(1)
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        start =-1
        for mat_size in range(len(matrix),1,-2):
            start +=1
            for j in range(mat_size-1):
                
                temp1 = matrix[start+j][len(matrix)-1-start]
                matrix[start+j][len(matrix)-1-start]=matrix[start][start+j]
                
                temp2= matrix[len(matrix)-1-start][len(matrix)-1-start-j]
                matrix[len(matrix)-1-start][len(matrix)-1-start-j]=temp1
                temp1=temp2
                
                temp2=matrix[len(matrix)-1-start-j][start]
                matrix[len(matrix)-1-start-j][start]=temp1
                temp1=temp2
                
                matrix[start][start+j]=temp1
            
        

                
                
                
                
        

