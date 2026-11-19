class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # 3, 1, 2, lo = 0, hi = 2, mid = 1 => nums[mid] = 1, nums[mid+1] = 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


def rotate(nums, k):
    # rotating once moves the last element to the front
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]


if __name__ == '__main__':
    s = Solution()
    big = list(range(-2500, 2500))
    testcases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([1], 1),
        ([1, 2], 1),
        ([2, 1], 1),
        ([3, 1, 2], 1),
        ([2, 3, 1], 1),
        # rotated once: minimum is the second element
        ([7, 0, 1, 2, 4, 5, 6], 0),
        # rotated n - 1 times: minimum is the last element
        ([1, 2, 4, 5, 6, 7, 0], 0),
        # odd/even lengths with the pivot right around the midpoint
        ([5, 6, 7, 1, 2, 3, 4], 1),
        ([4, 5, 6, 7, 1, 2, 3], 1),
        ([5, 6, 1, 2, 3, 4], 1),
        ([-1, -5000, -4000], -5000),
        ([5000, -5000], -5000),
        # Max size (n = 5000): an O(n) scan passes but misses the O(log n) requirement.
        (big, -2500),
        (rotate(big, 1), -2500),
        (rotate(big, 2500), -2500),
        (rotate(big, 4999), -2500),
        (rotate(big, 1234), -2500),
    ]
    for i, (nums, want) in enumerate(testcases):
        got = s.findMin(nums)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
