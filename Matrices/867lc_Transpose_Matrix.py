class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = [[0]*len(matrix) for column in range(len(matrix[0]))]
        for  row in range(len(matrix)):
            for col in range(len(matrix[0])):
                new_matrix[col][row]=matrix[row][col]
        return new_matrix