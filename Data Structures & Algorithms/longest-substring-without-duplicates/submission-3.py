class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1

        dups = set() 
        i = 0
        j = 1
        curr = 0
        dups.add(s[i])
        while j < len(s):
            if s[j] in dups:
                dups.remove(s[i])
                i += 1
            else:
                dups.add(s[j])
                curr = max(curr, len(dups))
                j += 1
        return curr
        