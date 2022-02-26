class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x:len(x))
        n = len(strs[0])
        while n:
            for s in strs[1:]:
                if strs[0][:n] != s[:n]:
                    break
            else:
                return strs[0][:n]
            n -= 1
        else:
            return ""