class Solution:
    def twoSum(self, nums, target):
        store = {}   # dictionary to store number -> index

        for i, num in enumerate(nums):
            needed = target - num   # the number we are looking for

            if needed in store:
                return [store[needed], i]

            store[num] = i   # store current number with index

        return []