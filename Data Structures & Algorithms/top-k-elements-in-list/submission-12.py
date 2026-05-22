class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) 
        print(counts)
        heap = []
        for v,c in counts.items():
            heapq.heappush(heap, (c,v))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for (c,v) in heap:
            res.append(v)

        return res
