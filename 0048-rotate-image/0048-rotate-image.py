class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N= len(matrix)
        #transpose
        for i in range(N):
            for j in range(0, i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # swap mirror columns
        col = floor(N/2)
        for i in range(N):
            for j in range(col):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][N-j-1]
                matrix[i][N-j-1] = tmp
