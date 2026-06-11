class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = len(s1)
        nums = Counter(s1) 
        counts = defaultdict(int) 
        i, j = 0, 0

        for k in range(window):
            counts[s2[j]] += 1
            j += 1

        if counts == nums:
            return True
    
        while j < len(s2): 
            counts[s2[j]] += 1
            counts[s2[i]] -= 1
            if counts[s2[i]] <= 0:
                del counts[s2[i]]

            if counts == nums:
                return True
            
            i += 1
            j += 1

        return False

