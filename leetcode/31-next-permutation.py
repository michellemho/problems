class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        a = len(nums) - 1
        b = a - 1
        
        while nums[a] <= nums[b] and b >= 0:
            a = a-1
            b = b-1
        print(a, b)
        
        # if nums already in descending order, no possible larger value, smallest (reverse)
        if b < 0:
            nums[:] = nums[::-1]
            print('exiting', nums)
            return
            
        
        # once a spot where nums[a] > nums[b] is found, traverse back right
        # find where nums[b] fits in the order and swap with next highest
        nums_b_val = nums[b]
        print(b, nums_b_val)
        counter = 0
        for i in nums[b+1:]:
            if nums_b_val >= i:
                break
            else:
                counter += 1
        print("counter", counter)
        swap_spot = counter + b
        swap_value = nums[swap_spot]
        
        nums[b] = swap_value
        nums[swap_spot] = nums_b_val
        
        nums[b+1:] = nums[b+1:][::-1]
