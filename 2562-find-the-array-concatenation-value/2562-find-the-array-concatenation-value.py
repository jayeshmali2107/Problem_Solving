class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        if n%2!=0:
            sum+=nums[n//2]
        for i in range(n//2):
            sum+=int(str(nums[i])+str(nums[n-1-i]))
        return sum

        