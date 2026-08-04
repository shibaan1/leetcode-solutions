class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        add = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(0,n):
            for j in range(0,m):

                if grid[i][j] == 1:

                    if i-1>=0:
                        if grid[i-1][j] != 1:
                            add +=1

                    else :
                        add+=1   

                    if i+1<=n-1:
                        if grid[i+1][j] != 1:
                            add+=1

                    else :
                        add+=1

                    if j-1 >= 0:
                        if grid[i][j-1] != 1:
                            add +=1

                    else :
                        add+=1

                    if j+1 <= m-1:
                        if grid[i][j+1] !=1:
                            add+=1
                    else :
                        add+=1

        return add
