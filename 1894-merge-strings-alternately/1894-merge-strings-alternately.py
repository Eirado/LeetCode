class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        x, y = 0, 0

        size_word1 = len(word1)
        size_word2 = len(word2)
        res = ""
        while x < size_word1 or y < size_word2: 
           
            if x < size_word1:
                res += word1[x]
                x += 1
            if y < size_word2:
                res += word2[y]
                y += 1
        return res