class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        count = 0
        p = 0

        while count<=(h-n):
            flag = False
            for i in range(n):

                if needle[i]== haystack[p+i]:
                    flag =True

                else:
                    flag = False
                    break    

            if flag == True:
                return p        
            p +=1
            count +=1

        return -1         