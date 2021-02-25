class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # base condition
        if len(nums) == 1:
            return True
        
        # if all greater than one, then return True
        if all([num >= 1 for num in nums]):
            return True

        last_step = len(nums) - 1
        for i in range(last_step-1, -1, -1):
            curr_step_value = nums[i]
            if curr_step_value + i >= last_step:
                if i == 0:
                    return True
                else:
                    return self.canJump(nums[:i+1])
            else:
                continue
        return False
