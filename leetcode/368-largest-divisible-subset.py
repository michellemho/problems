class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        divisorCount = [1 for num in sorted_nums]
        divisors = [[num] for num in sorted_nums]

        for index, i in enumerate(sorted_nums):
            currMax = 0
            currWinner = index
            for index_j, j in enumerate(sorted_nums[:index]):
                # print('is {} (and all its divisors found so far) divisible by {}?'.format(i, j))
                # print(divisors[index])
                # print('and is the resulting set larger than the current winner?')
                if i % j == 0 and len(divisors[index_j]) > currMax:
                    # print('yes')
                    currMax = len(divisors[index_j])
                    currWinner = index_j
            if currWinner != index:
                print(currMax, sorted_nums[currWinner])
                divisorCount[index] = divisorCount[index] + currMax
                divisors[index] = divisors[index] + divisors[currWinner]
        print(divisors, divisorCount)
        return divisors[divisorCount.index(max(divisorCount))]
