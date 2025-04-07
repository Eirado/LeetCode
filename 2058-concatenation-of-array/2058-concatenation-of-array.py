class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        N = len(nums)
        ans = [0] * (N * 2)
        k = 0

        for i in range(len(ans)):
            if k == N:
                k = 0
            ans[i] = nums[k]
            k += 1

        return ans

        # or just return nums + nums