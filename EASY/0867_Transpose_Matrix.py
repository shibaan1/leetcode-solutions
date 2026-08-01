class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        n =len(matrix)
        m = len(matrix[0])

        for x in range(m):
            row = [0]*n
            arr.append(row)

        for i in range(0,n):
            for j in range(0,m):

                arr[j][i] = matrix[i][j]

        return arr