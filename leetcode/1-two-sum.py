class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            if (target - num) not in lookup:
                lookup[num] = (target - num, i)
            else:
                return [i, lookup[target - num][1]]
