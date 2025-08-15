class Solution:
    def validPalindrome(self, s: str) -> bool:


        l, r = 0, len(s) - 1
        
        while l < r:

            if s[l] != s[r]:

               left_skip = s[l+1:r+1]
               right_skip = s[l:r]
                
               return left_skip == left_skip[::-1] or right_skip == right_skip[::-1]
                
            l, r = l + 1, r - 1

        return True