class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        res = []

        for i, string in enumerate(strs): 
            sorted_string = "".join(sorted(string))
           
            if sorted_string in hashmap:
                hashmap[sorted_string] = hashmap.get(sorted_string) + [string]
            else: 
                hashmap[sorted_string] = [string]
        
        for value in hashmap.values():
            res.append(value)
            
        return res 