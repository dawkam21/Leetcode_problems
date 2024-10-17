from typing import List

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for num in range (1, n):
            if nums[num] == nums[num - 1]:
                return True
        return False
if __name__ == '__main__':
    print(Solution.containsDuplicate(Solution, nums=[1, 2, 3, 1]))