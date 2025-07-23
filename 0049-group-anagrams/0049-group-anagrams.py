class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        res = []

        for i, word in enumerate(strs):
          sorted_word = "".join(sorted(word))
          
          if sorted_word in hashmap:
            hashmap[sorted_word] = hashmap.get(sorted_word) + [word]
          else:
            hashmap[sorted_word] = [word]

        for value in hashmap.values():
            res.append(value)

        return res