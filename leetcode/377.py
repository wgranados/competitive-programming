class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # Base: F(0) = 1
        # F(i) = sum(F(i - num_J) )
        dp = [0] * (target + 1)
        dp[0]=1
        for curr_sum in range(target+1):
            for num in nums:
                if curr_sum - num >= 0:
                    dp[curr_sum] += dp[curr_sum - num]
        return dp[target]
        

if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([1, 2, 3], 4, 7),
        ([9], 3, 0),
        ([1], 1, 1),
        ([2], 1, 0),
        ([1], 10, 1),
        ([2], 10, 1),
        ([2], 9, 0),
        # order matters, so this is the Fibonacci numbers: F(11) = 89
        ([1, 2], 10, 89),
        # nums not given in sorted order
        ([3, 1, 2], 4, 7),
        ([5, 1, 8], 24, 982),
        ([4, 2, 1], 32, 39882198),
        # most numbers are bigger than the target
        ([3, 4, 5, 6, 7, 8, 9, 10, 11], 10, 9),
        ([1000], 1000, 1),
        ([999], 1000, 0),
        ([1, 1000], 1000, 2),
        # every number is a multiple of 3 (or 7, or 2) but the target isn't
        ([3, 33, 333], 1000, 0),
        ([7, 77, 777], 1000, 0),
        (list(range(2, 201, 2)), 999, 0),
        # Max sizes (200 nums, target 1000)
        (list(range(1, 201)), 1, 1),
        # every way to split 30 into ordered parts: 2^29
        (list(range(1, 201)), 30, 536870912),
        ([50, 100], 1000, 10946),
    ]
    for i, (nums, target, want) in enumerate(testcases):
        got = s.combinationSum4(nums, target)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
