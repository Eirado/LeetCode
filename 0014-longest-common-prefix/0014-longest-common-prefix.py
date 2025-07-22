class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs == "" or strs == None: 
            return ""

        first_srt = strs[0]
        result = ""

        for i, char in enumerate(first_srt):
          
          for j in strs[1:]:
            if i == len(j) or j[i] != char:
                return result
          result += char

        return result

      