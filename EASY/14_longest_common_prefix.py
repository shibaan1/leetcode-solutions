class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = len(strs[0])
        alpha = ''
        flag =False
        sf = []

        if min_word == 0:
            return ''

        for word in strs:
            if len(word)<=min_word:
                min_word = len(word)
               
        for i in range(min_word):
            alpha = strs[0][i]
            flag = False

            for word in strs:
                if word[i] == alpha:
                    flag = True

                else:
                    if len(sf) == 0:
                        return ''    
                    else:
                        return ''.join(sf)    

            if flag ==True:
            sf.append(strs[0][i])    

        return ''.join(sf)
