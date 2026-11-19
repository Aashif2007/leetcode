class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0
        for value in nums:
            total += value
            result.append(total)
        return result
