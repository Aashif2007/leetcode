class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
       min=float("inf")
       i=0
       for s in strs:
        if len(s)<min:
            min=len(s)
       while i < min:
        for s in strs:
            if s[i]!=strs[0][i]:
                return s[:i]
        i+=1
       return strs[0][:i]
        

