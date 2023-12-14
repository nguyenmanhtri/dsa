from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # index
        most_water = 0
        while left < right:
            most_water = max(
                most_water, min(height[left], height[right]) * (right - left)
            )
            # check if next element of left or right is greater than left or right
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return most_water
