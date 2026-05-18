class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #keep backtracking until no palindrome is found 
        # Base Case: append current partition if i >= len(s)
        # iterate through every other character in range(i, len(s))
        # starting from string i to j, if its a palindrome, we can append s[i: j + 1]
        # if palindrome, recursively continue dfs
        res = []
        subset = []
        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return 
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    subset.append(s[i:j + 1])
                    dfs(j + 1)
                    subset.pop()
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r- 1
        return True