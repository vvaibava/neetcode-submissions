class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #hashmap of all values in s
        #if window size - count <= k --> move r
        #else move l

        count = {}
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            size = r - l + 1
            while (size - max(count.values()) > k):
                count[s[l]] -= 1
                l += 1
                size = r - l + 1
            res = max(res, size)
        return res