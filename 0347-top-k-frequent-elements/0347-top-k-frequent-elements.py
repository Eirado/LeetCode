class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        res = []
        
        for i in nums:
          hashmap[i] = hashmap.get(i,0) + 1

        
        sorted_dict = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)


        for i in sorted_dict[:k]:
            res.append(i[0])

        return res

