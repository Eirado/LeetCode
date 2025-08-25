from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [0] * N
        prefix_array = []
        suffix_array = []
        
        prefix = 1
        for i in range(N):
            prefix *= nums[i]
            prefix_array.append(prefix)

        suffix = 1
        for i in range(N - 1, -1, -1):
            suffix *= nums[i]
            suffix_array.append(suffix)
        suffix_array = suffix_array[::-1]

        for i in range(N):
            prefix_product = prefix_array[i - 1] if i > 0 else 1
            suffix_product = suffix_array[i + 1] if i < N - 1 else 1
            answer[i] = prefix_product * suffix_product

        return answer
