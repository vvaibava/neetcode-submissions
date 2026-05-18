class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #create a maxheap and adding distance of each point to the heap [dist, x, y]
        #if distance length > k, then pop items 
        #create a list and while distance exists, add coords to it
        distance = []
        for x, y in points:
            dist = -((x**2) + (y**2))
            heapq.heappush(distance, [dist, x, y])
            if len(distance) > k:
                heapq.heappop(distance)
        res = []
        while distance:
            dist, x, y = heapq.heappop(distance)
            res.append([x, y])
        return res