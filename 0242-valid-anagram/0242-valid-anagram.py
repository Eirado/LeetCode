class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        N = len(s)
        
        if N != len(t): 
            return False

        for i in range(N):
            dic[s[i]] = dic.get(s[i], 0)  + 1 
 
        for i in set(t):
            if i in dic.keys():
                if t.count(i) != dic[i]:
                    return False
            else: 
                return False
        return True 
          
        
       