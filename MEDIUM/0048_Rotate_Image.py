class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        ce = m-1
        arr = []

        for i in range(n):
            col =['x']*m
            arr.append(col)


        for i in range(n):
            for j in range(m):

                 if ce>=0:

                    arr[j][ce] = matrix[i][j]    

            ce -=1        

        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[i][j]