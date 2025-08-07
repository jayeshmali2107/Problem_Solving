class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        i = 0

        # Step 1: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        p = i

        # p must be between 1 and n-2
        if p == 0 or p >= n - 2:
            return False

        # Step 2: strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        q = i

        # q must be between p+1 and n-2
        if q == p or q >= n - 1:
            return False

        # Step 3: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1