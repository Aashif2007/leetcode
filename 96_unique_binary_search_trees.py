class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for nodes in range(1, n + 1):
            for left in range(nodes):
                right = nodes - 1 - left
                dp[nodes] += dp[left] * dp[right]
        return dp[n]
