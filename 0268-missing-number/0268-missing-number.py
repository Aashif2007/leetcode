class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        e=n*(n+1)//2
        a=sum(nums)
        return e-a
        