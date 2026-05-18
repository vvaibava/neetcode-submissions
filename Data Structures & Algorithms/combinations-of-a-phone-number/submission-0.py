class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Base Case: length of each output string is length of each input string
        #map of every digit value
        #call backtrack for each value in digit, (i + 1, string + c)
        #4^n time complexity, must brute force
        counts = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        output = []
        def combinations(i, string):
            if (len(string) == len(digits)):
                output.append(string)
                return
            for c in counts[digits[i]]:
                combinations(i + 1, string + c)
        
        if digits:
            combinations(0, "")
        
        return output
            
            
