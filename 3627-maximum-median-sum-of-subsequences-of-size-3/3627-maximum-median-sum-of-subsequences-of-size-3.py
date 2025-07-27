class Solution:
    def maximumMedianSum(self, nums):
        nums.sort()
        n = len(nums)
        k = n // 3
        res = 0
        idx = n - 2
        for _ in range(k):
            res += nums[idx]
            idx -= 2
        return res
