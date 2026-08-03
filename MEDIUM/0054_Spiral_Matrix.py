class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        ans = []
        total = n*m
        c = 0

        rs = 0
        re = n-1
        cs = 0
        ce = m-1

        while c < total:
            # rs : cs-->ce
            for i in range(cs , ce+1):
                ans.append(matrix[rs][i])
                c +=1

            if c == total:
                break

            rs +=1        

            # ce: rs-->re
            for i in range(rs , re+1):
                ans.append(matrix[i][ce])
                c +=1

            if c == total:
                break

            ce -=1

            # re: ce --> cs
            for i in range(ce , cs-1 , -1):
                ans.append(matrix[re][i])
                c +=1

            if c == total:
                break

            re -=1

            # cs: re --> rs
            for i in range(re , rs-1, -1):
                ans.append(matrix[i][cs])
                c +=1

            if c == total:
                break    

            cs +=1                    

        return ans        