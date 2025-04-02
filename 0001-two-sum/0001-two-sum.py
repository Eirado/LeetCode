class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}
        result = 0

        for i, num in enumerate(nums): 
            
            result = target - num
            
            if result in hashMap:
                return [i, hashMap[result]]
           
            hashMap[num] = i
            
            

           
            


        