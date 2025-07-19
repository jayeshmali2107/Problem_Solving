class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        minn = float('inf')
        for num in nums:
            if num > minn:
                ans = max(ans, num - minn)
            minn = min(minn, num)
        return ans