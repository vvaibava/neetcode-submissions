class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        s = "".join(s.split())
        i = 0
        j = len(s) - 1
        while i < j:
            print(i)
            print(j)
            front = s[i]
            back = s[j]

            if not front.isalnum():
                i += 1
                continue
            elif not back.isalnum():
                j -= 1
                continue
            else:
                if front.lower() != back.lower():
                    return False

            
            i += 1
            j -= 1

        return True