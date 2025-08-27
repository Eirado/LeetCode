class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lengh = len(nums)
        x, y = 0, 0
        k = 0
    
        while y < lengh:
            nums[x] = nums[y]
            while y < lengh and nums[x] == nums[y]:
                y += 1
            x += 1
            k += 1
           
           
        
            
        return k

        
        # [1,1,2]
        # x = 0 y = 2
        # x = 1 y = 2
        # [1,2,1]

        # [0,]