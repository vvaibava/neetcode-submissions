class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep = 0
        for i, num in enumerate(nums):
            if i > maxStep:
                return False
            maxStep = max(maxStep, num + i)
            if maxStep >= len(nums) - 1:
                return True

        return False
