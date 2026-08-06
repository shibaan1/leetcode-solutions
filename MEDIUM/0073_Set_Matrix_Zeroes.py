class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        iarr = ['x']*n
        jarr = ['x']*m

        for i in range(n):
           for j in range(m):

               if matrix[i][j] == 0:
                   iarr[i] = 0
                   jarr[j] = 0

        for i in range(n):
            for j in range(m):

                if iarr[i]==0 or jarr[j]==0:
                    matrix[i][j] = 0            