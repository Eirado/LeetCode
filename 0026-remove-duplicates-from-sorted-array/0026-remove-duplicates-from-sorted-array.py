class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lengh = len(nums)
        x, y = 0, 0

    
        while y < lengh:
            nums[x] = nums[y]
            while y < lengh and nums[x] == nums[y]:
                y += 1
            x += 1
        return x
