class Solution:
    def reverseString(self, s: List[str]) -> None:
       
        x = 0
        y = len(s) - 1 

        while x <= y:
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
            

       





        """
        Do not return anything, modify s in-place instead.
        """
        