class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #goal is to get both arrays matching, if not return false
        #create array of two and add 26 letters
        #increment current counts by ord(s1[i]) - ord('a'))
        #increment matching variable if there is a match between two arrays
        #loop thru s1 --> s2, get index of current letter via ord
        #increment count in array s2
        #if the index at both counts are equal, increase matches, 
        # elif s1 index + 1 = s2? --> decrease matches
        # do the same with left pointer

        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for c in range(len(s1)):
            s1Count[ord(s1[c]) - ord('a')] += 1
            s2Count[ord(s2[c]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
            print(matches)
        return matches == 26