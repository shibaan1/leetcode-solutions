class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        avglist = []
        add = 0
        avg = 0
        newlist = []
        n = len(img)
        m = len(img[0])

        for i in range(n):
            col = [0]*m
            newlist.append(col)

        for i in range(0,n):
            for j in range(0,m):
                    avglist.append(img[i][j])
                    if i-1 >= 0:
                        avglist.append(img[i-1][j])

                    if j-1 >= 0:
                        avglist.append(img[i][j-1])

                    if i+1 <= n-1:
                        avglist.append(img[i+1][j])

                    if j+1 <= m-1:
                        avglist.append(img[i][j+1])

                    if i-1 >=0 and j-1>=0:
                        avglist.append(img[i-1][j-1])

                    if i-1>=0  and j+1<=m-1:
                        avglist.append(img[i-1][j+1])

                    if i+1<=n-1 and j-1>=0:
                        avglist.append(img[i+1][j-1])

                    if i+1<=n-1 and j+1 <= m-1:
                        avglist.append(img[i+1][j+1])                   

                    for x in avglist:
                        add += x

                    avg = add//len(avglist)

                    newlist[i][j] = avg         

                    avg = 0
                    add = 0
                    avglist = []

        return newlist            
