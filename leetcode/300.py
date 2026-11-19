class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # F(i, j) = max(F(i,j), F(i, 0..j) + 1, F(i, 0..j)) if nums[j] > nums[i]
        dp = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        

if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([1], 1),
        ([1, 2], 2),
        ([2, 1], 1),
        ([-2, -1], 2),
        ([5, 4, 3, 2, 1], 1),
        # strictly increasing: equal values can't both be used
        ([1, 2, 2, 3], 3),
        ([2, 2, 1, 1, 3, 3], 2),
        # the best subsequence doesn't start at the smallest element
        ([4, 10, 4, 3, 8, 9], 3),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
        ([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12], 6),
        ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6),
        ([-10**4, 10**4], 2),
        ([10**4, -10**4], 1),
        # Max size (n = 2500)
        (list(range(-1250, 1250)), 2500),
        (list(range(1250, -1250, -1)), 1),
        ([0, 1] * 1250, 2),
        # 50 blocks, each decreasing inside, blocks increasing: one pick per block
        ([i * 50 + (49 - j) for i in range(50) for j in range(50)], 50),
    ]
    for i, (nums, want) in enumerate(testcases):
        got = s.lengthOfLIS(nums)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
