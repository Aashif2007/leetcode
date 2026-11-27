class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            money = nums[i - 1]
            skip = dp[i - 1]
            rob = money + (dp[i - 2] if i > 1 else 0)
            dp[i] = max(skip, rob)

        return dp[len(nums)]