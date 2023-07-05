class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0 = 1
        r =len(matrix)
        c= len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    matrix[0][j]=0 #marking which column need to be zeroed
                    if i==0:
                        row0=0 #marking which row to be zeroed
                    else:
                        matrix[i][0]=0 #marking which row to be zeroed

        for i in range(1, r):
            for j in range(1, c):
                # If row or column has 0 set it to 0
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if matrix[0][0] == 0:
            for i in range(r):
                matrix[i][0]=0
        if row0 == 0:
            for i in range(c):
                matrix[0][i]=0
    