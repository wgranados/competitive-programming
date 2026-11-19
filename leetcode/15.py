from collections import defaultdict
from bisect import bisect_left
import random
import time


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                compliment = -1*(nums[i] + nums[j]) 
                k = bisect_left(nums, compliment, j+1)
                if k < len(nums) and nums[k] == compliment:
                    comb=(nums[i], nums[j], nums[k])
                    triplets.add(tuple(sorted(comb)))
        return list(triplets)

    def threeSumTwoPointers(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 2):
            # same value for i would produce the same triplets again
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # smallest remaining value is positive, so no sum can reach 0
            if nums[i] > 0:
                break
            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    triplets.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # skip duplicates so the same triplet isn't added twice
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
        return triplets


def normalize(triplets):
    # order of triplets and of values within a triplet does not matter,
    # but duplicates do, so sort instead of building a set
    return sorted(tuple(sorted(t)) for t in triplets)


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]
    for method in (s.threeSum, s.threeSumTwoPointers):
        print(method.__name__)
        for i, (nums, want) in enumerate(testcases):
            got = method(nums)
            if normalize(got) != normalize(want):
                print('Test {}: got != want, {} != {}'.format(i, got, want))
            else:
                print('Test {}: passed'.format(i))

    # timing on max-size inputs (n = 3000)
    random.seed(1)
    big_inputs = [
        ('random', [random.randint(-10**5, 10**5) for _ in range(3000)]),
        ('all zeros', [0] * 3000),
    ]
    for name, nums in big_inputs:
        results = []
        for method in (s.threeSum, s.threeSumTwoPointers):
            start = time.perf_counter()
            results.append(normalize(method(nums)))
            print('{} on {}: {:.3f}s'.format(method.__name__, name, time.perf_counter() - start))
        if results[0] != results[1]:
            print('{}: methods disagree'.format(name))
        