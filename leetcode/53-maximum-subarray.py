class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if all([i < 0 for i in nums]):
            return max(nums)
        # if len(nums) == 1:
        #     return nums[0]
        currentMax = 0
        bestMax = max(nums)
        for n in nums:
            currentMax = max(0, currentMax + n)
            bestMax = max(currentMax, bestMax)
        return bestMax
