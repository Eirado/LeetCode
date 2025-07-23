class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = {}
        list_part_size = len(nums) / 2

        for i in nums: 
            hashmap[i] = hashmap.get(i,0) + 1
            if hashmap[i] > list_part_size:
                    return i
                

                
            