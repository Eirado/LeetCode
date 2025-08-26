from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        N = len(nums) 
        answer = [0] * N
        print(answer)
        current_prefix = 1 
        current_suffix = 1
        # [1,2,3,4]
        # [1, 1, 2, 6]
        # [24,12,4,1]
        

        for i in range(N):
            answer[i] = current_prefix
            current_prefix *= nums[i]
        for i in range(N - 1, -1, -1):
            answer[i] *= current_suffix
            current_suffix *= nums[i]    
        return answer




 