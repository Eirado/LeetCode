class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        x, y = 0, 0
        res = []
        while x < len(word1) and y < len(word2): 
            res.append(word1[x]) 
            res.append(word2[y])
            x += 1
            y += 1
        res.append(word1[x:])
        res.append(word2[y:])
        return "".join(res)