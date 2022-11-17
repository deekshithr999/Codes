'''
Link : https://leetcode.com/problems/sudoku-solver/

37. Sudoku Solver
Hard

5273

156

Add to List

Share
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
Accepted
354,522
Submissions
652,376

'''


'''
TC : O(9^nxn)
SC: O(1)
'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.playNext(board,0,0,len(board))
    
    def playNext(self,board: List[List[str]],crow,ccol,n):
        #print ("crow, ccol", crow,"-",ccol)
        nrow,ncol=0,0
        if crow==n and ccol==0:
            #print("Here")
            return True

        if ccol==n-1:
            ncol=0
            nrow=crow+1
        else:
            nrow=crow
            ncol=ccol+1

        if board[crow][ccol]==".":
            for i in range(1,10):
                if self.canAdd(board,crow,ccol,str(i),n):
                    board[crow][ccol]=str(i)
                    ret =self.playNext(board,nrow,ncol,n)
                    if ret==True:
                        return ret
            #print ("Falseeh")
            board[crow][ccol]="."
            return False
        else:
             return self.playNext(board,nrow,ncol,n)
            
        
        
    
    def canAdd(self,board, crow,ccol,num,n):
        #print ("crow , ccol ",crow," ",ccol)
        #check row
        for i in range(n):
            if board[i][ccol]==num:
                return False
        
        #check col
        for i in range(n):
            if board[crow][i]==num:
                return False
        #check in sub-matrix
        r=int(crow/3)*3
        c=int(ccol/3)*3
        for i in range(r,r+3):
            for j in range(c,c+3):
                if board[i][j]==num:
                    return False
        #print("returning True")
        return True

