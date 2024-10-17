from typing import List

class Solution(object):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for n, f in counter.items():
            freq[f].append(n)
            return


print(Solution.topKFrequent(Solution, nums = [1,1,1,2,2,3], k = 2))
