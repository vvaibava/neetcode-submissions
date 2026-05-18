from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep = 0  # Maximum index that can be reached so far
        
        for i, num in enumerate(nums):
            if i > maxStep:  # If the current index is not reachable, return False
                return False
            maxStep = max(maxStep, i + num)  # Update the maximum reachable index
            if maxStep >= len(nums) - 1:  # If we can reach or go beyond the last index, return True
                return True
        
        return False
