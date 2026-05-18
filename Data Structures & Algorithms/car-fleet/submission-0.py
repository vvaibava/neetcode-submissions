class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #combine two arrays into one array of pairs(pos, speed) 
        #order by desc because the speeds can change if car becomes fleet
        #car fleet if two cars intersect --> (distance diff)/speed
        #add cars to stack and compare cars, if they collide, remove top of stack
        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)