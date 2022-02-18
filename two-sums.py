class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate from the first number and check one by one if it sums to the target number
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j