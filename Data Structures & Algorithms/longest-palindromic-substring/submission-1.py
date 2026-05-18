class Solution:
    def longestPalindrome(self, s: str) -> str:
        # edge cases: if no palindromes at all, return 0
        #two pointer approach, and one middle pointer
        currLength, resIdx = 0, 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if currLength < r - l + 1:
                    currLength = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            l, r = i,i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if currLength < r - l + 1:
                    currLength = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
        return s[resIdx : currLength + resIdx]
                