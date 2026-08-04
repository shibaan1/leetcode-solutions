class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])

        for i in range(0,n):
            image[i].reverse()

        for i in range(0,n):
            for j in range(0,m):
                if image[i][j] == 0:
                    image[i][j] = 1    

                elif image[i][j] ==1 :
                    image[i][j] = 0  

        return image            