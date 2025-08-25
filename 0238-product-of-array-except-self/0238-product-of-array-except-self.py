from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [0] * N

        prefix = 1
        for i in range(N):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(N - 1, -1, -1): 
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
