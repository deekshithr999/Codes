'''
https://leetcode.com/problems/valid-sudoku/description/
'''
class Solution:
    '''
    TC: O(n^2 + n*mlogm*n)
    SC: O(3*m*n)
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row-wise
        # check column wise
        #check sub matrix

        #st = set()
        for i in range(len(board)):
            st = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in st:
                    return False
                st.add(board[i][j])
        #column wide 

        for i in range(len(board[0])):
            st = set()
            for j in range(len(board)):
                if board[j][i]==".":
                    continue
                if board[j][i] in st:
                    return False
                st.add(board[j][i])
        
        # Run sub-matrix wide

        for i in range(0,len(board[0]),3):
            for j in range(0, len(board),3):
                st = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] == ".":
                            continue
                        if board[i+k][j+l] in st:
                            return False
                        st.add(board[i+k][j+l])
        return True