class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2: 
            return True

        window = len(s1)
        nums = Counter(s1) 
        print(window)
        print(nums) 
        counts = defaultdict(int) 
        for i in range(len(s2) - window + 1): 
            j = i
            while j < i + window and j < len(s2):
                counts[s2[j]] += 1
                j += 1
            if counts == nums:
                return True
            else:
                counts.clear() 
        

        return False


