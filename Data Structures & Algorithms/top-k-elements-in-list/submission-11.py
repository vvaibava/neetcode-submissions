class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) 
        print(counts)
        heap = []
        for v,c in counts.items():
            heapq.heappush(heap, (-c,v))

        res = []
        for i in range(k):
            num = heapq.heappop(heap)
            res.append(num[1])

        return res
