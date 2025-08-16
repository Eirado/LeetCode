class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        x, y = 0, 0
        res = []
        range_len = min(len(word1), len(word2))
        for i in range(range_len):
            res.append(word1[x]) 
            res.append(word2[y])
            x += 1
            y += 1

        res.append(word1[x:])
        res.append(word2[y:])
        
        return "".join(res)