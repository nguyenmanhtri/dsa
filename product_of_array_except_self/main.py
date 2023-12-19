# Description: https://leetcode.com/problems/product-of-array-except-self

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right = nums[-1]
        for i in range(n - 2, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


nums1 = [1, 2, 3, 4]  # expected: [24,12,8,6]
nums2 = [-1, 1, 0, -3, 3]  # expected: [0,0,9,0,0]
nums3 = [1, 3, 3, 4]  # expected: [36,12,12,9]
solution = Solution()
print(solution.productExceptSelf(nums1))
print(solution.productExceptSelf(nums2))
print(solution.productExceptSelf(nums3))
