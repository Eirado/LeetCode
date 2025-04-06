class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_element = strs[0]
        result_str = ""
       
        for i in range(len(first_element)): 
            for j in strs: 
                if i == len(j) or j[i] != first_element[i]:
                    return result_str
            
            result_str = result_str + first_element[i]
        
        return result_str

        # O(n) n being the len of the first word