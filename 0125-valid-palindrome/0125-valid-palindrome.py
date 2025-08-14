class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = "".join(ch.lower() for ch in s if ch.isalnum())
        
        
        x, y = 0, len(string) - 1

        while x < y:
            if string[x] != string[y]:
                return False
            x += 1
            y -= 1
     
        return True