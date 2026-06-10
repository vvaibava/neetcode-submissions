class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        i, j = 0, 0
        count = 0
        while j < len(s): 
            counts[s[j]] += 1
            window = j - i + 1
            maxCounts = max(counts.values())
            if window - maxCounts <= k:
                count = max(count, window)
                j += 1
            else: 
                counts[s[i]] -= 1
                i += 1
                counts[s[j]] -= 1
        
        return count 
