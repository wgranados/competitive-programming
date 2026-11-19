class Solution:
    def rob(self, nums: list[int]) -> int:
        # F(i) = max(F(i+1), F(i+2) + nums[i])
        # intuitin: either pick this house, and maximum on next interval
        # or you don't pick this house and pick you must have selected the next one
        dp = [0 for i in range(len(nums)+1)]
        n = len(nums)
        dp[n] = 0
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2] + nums[i])
        return dp[0]
        

if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([5], 5),
        ([0], 0),
        ([1, 2], 2),
        ([2, 1], 2),
        ([0, 0, 0], 0),
        # best plan skips two houses in a row: plain odd/even alternation fails here
        ([2, 1, 1, 2], 4),
        ([1, 3, 1, 3, 100], 103),
        # Max size (n = 100, nums[i] = 400).
        ([400] * 100, 20000),
        ([1, 400] * 50, 20000),
        ([400, 0] * 50, 20000),
        (list(range(100)), 2500),
    ]
    for i, (nums, want) in enumerate(testcases):
        got = s.rob(nums)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
