class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for val in nums:
            if val not in count:
                count[val] = 1
            else:
                count[val] += 1
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        num = list(sorted_count.keys())[:k]
        return num

