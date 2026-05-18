class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersOne = Counter(s)
        lettersTwo = Counter(t)
        if lettersOne == lettersTwo:
            return True
        return False