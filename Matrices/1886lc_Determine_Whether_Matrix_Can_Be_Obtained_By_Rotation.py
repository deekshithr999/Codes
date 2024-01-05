class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        if mat == target:
            return True
        def compare_matrices(m1, m2):
            return m1 == m2

        n_rotations =0
        n= len(mat)
        tmp_mat = mat
        while n_rotations <4:
            rot_mat = [[0]*n for _ in range(n)]
            for row in range(n):
                for col in range(n):
                    rot_mat[col][n-row-1] = tmp_mat[row][col]
            if compare_matrices(tmp_mat, target):
                return True
            tmp_mat = rot_mat
            n_rotations += 1
        return False
            

        