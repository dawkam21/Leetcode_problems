from typing import List


class Solution(object):
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

print(Solution.two_sum(Solution, nums=[3, 3], target=6))
