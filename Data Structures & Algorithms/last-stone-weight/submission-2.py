class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #make max heap by converting each element into - in list
        #while length > 1, if second > first, push difference between two
        #append(0) to end of list in case there arent any values
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])



