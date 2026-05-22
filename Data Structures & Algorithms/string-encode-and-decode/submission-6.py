class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs: 
            res = str(len(s)) + "#" + s
            encoded_string += res
        print(encoded_string)
        return encoded_string; 

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        while len(s) != 0:
            i = s.index("#")
            print(i)
            l = int(s[:i])
            print(l)
            decoded_string.append(s[i+1:l + i + 1])
            s = s[i + l + 1:]
        return decoded_string; 
