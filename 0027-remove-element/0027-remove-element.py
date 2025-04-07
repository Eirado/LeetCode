class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        N = len(nums)

        for i in range(N):
            while i < len(nums) and nums[i] == val:
                nums.pop(i)

            
            
            