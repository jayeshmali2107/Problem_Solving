class Solution(object):
    def sortColors(self, nums):
        n =len(nums)
        for i in range(n - 1):
            swapped =  False
            for j in range(0,n-i-1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                    break
        return nums
