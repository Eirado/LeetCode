class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        
        N = len(s)
        
        if N != len(t): 
            return False

        for i in range(N):
            dic[s[i]] = (dic.get(s[i]) or 0) + 1 

        for key in dic.keys():
            if t.count(key) != dic[key]:
                return False
        return True   
          
       