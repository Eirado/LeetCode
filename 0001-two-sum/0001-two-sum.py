class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums): 
            desirable = target - num 
            if desirable in nums and i != nums.index(desirable):
                return [ nums.index(desirable), i]
           
   