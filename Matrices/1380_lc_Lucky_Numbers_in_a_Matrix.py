class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        def is_max_in_col(ele_row, ele_col):
            for i in range(len(matrix)):
                if i == ele_row:
                    continue
                if matrix[i][ele_col] >= matrix[ele_row][ele_col]:
                    return False
            return True
        lucky_numbers = []
        for row in range(len(matrix)):
            min_ele, min_row, min_col= matrix[row][0], row, 0
            for col in range(len(matrix[0])):
                if matrix[row][col]< min_ele:
                    min_ele, min_col = matrix[row][col], col
            if is_max_in_col(min_row, min_col):
                lucky_numbers.append(matrix[min_row][min_col])
        return lucky_numbers
            