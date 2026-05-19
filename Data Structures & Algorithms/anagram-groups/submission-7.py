class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)  
        for s in strs: 
            ang = Counter(s)
            key = tuple(sorted(ang.items()))
            keys[key].append(s)
        
        print(keys)
        res = []
        for v in keys.values():
            res.append(v) 
        
        print(res)
        return res