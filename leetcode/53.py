
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            if best < current:
                best = current
        return best

    def maxSubArrayNonLinear(self, nums: list[int]) -> int:
        prefix = [0 for i in range(len(nums) + 1)]
        prefix [0] = nums[0]
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        
        best = nums[0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                total = prefix[j] - prefix[i]
                if total > best:
                    best = total
        return best


            
    

if __name__ == '__main__':
    import random
    import time

    testcases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
        ([0], 0),
        ([-3, -1, -2], -1),
        ([-2, -1], -1),
        ([-1, 0, -2], 0),
        ([1, 2, 3], 6),
        ([3, -2, 3], 4),
        ([3, -4, 3], 3),
        ([8, -19, 5, -4, 20], 21),
    ]
    for i, (nums, want) in enumerate(testcases):
        s = Solution()
        for method in (s.maxSubArray, s.maxSubArrayNonLinear):
            got = method(list(nums))
            if got != want:
                print('Test {} ({}): got != want, {} != {}'.format(i, method.__name__, got, want))
            else:
                print('Test {} ({}): passed'.format(i, method.__name__))