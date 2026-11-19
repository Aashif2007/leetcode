class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        best = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                best[col] = triangle[row][col] + min(best[col], best[col + 1])
        return best[0]
