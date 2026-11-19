import math 
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi)//2
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile/mid)
            if hours_spent <= h:
                hi = mid
            else:
                lo = mid+1
        return lo
                


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([1], 1, 1),
        # h == len(piles): must eat the biggest pile in one hour
        ([3, 6, 7, 11], 4, 11),
        ([1, 1, 1, 1], 4, 1),
        ([10**9], 1, 10**9),
        ([10**9], 2, 5 * 10**8),
        # lots of spare time: slowest speed of 1 is enough
        ([10**9], 10**9, 1),
        ([312884470], 312884469, 2),
        # total hours overflows 32-bit ints at low speeds
        ([805306368, 805306368, 805306368], 10**9, 3),
        # Max size (n = 10^4): a linear scan over k from 1 to max(piles) is far too slow here.
        ([10**9] * 10**4, 10**4, 10**9),
        ([10**9] * 10**4, 10**9, 10**4),
    ]
    for i, (piles, h, want) in enumerate(testcases):
        got = s.minEatingSpeed(piles, h)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
