class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
   
        N = len(s)

        if N != len(t):
            return False

        for i in range(N):
            dic[s[i]] = (dic.get(s[i]) or 0) + 1
            dic2[t[i]] = (dic2.get(t[i]) or 0) + 1
       
        if dic == dic2:
            return True
            
        return False
            
