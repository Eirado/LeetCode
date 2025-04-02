class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_set = set(nums)
        result = 0

        for i, num in enumerate(nums): 
           result = target - num
           if result in nums and nums.index(result) != i:
                return [i , nums.index(result)]
           
            


        