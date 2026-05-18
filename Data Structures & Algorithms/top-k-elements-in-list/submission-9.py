class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
        heap = []
        for n in counts.keys():
            heapq.heappush(heap, (counts[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        res = []
        print(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        
        
