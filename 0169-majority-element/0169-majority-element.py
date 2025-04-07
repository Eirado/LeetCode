class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        my_set = set(nums)
        for i in my_set:
            if nums.count(i) > N // 2:
                return i
  
        