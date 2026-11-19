from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        # invert frequency to negative so that the heap is a max-heap
        freq_list = [(-freq, num) for num, freq in frequency.items()]
        heapq.heapify(freq_list)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(freq_list)[1])
        return result





if __name__ == '__main__':
    big = [7] * 50000 + [-3] * 30000 + list(range(1, 20001))
    testcases = [
        # examples
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
        # k == number of unique elements
        ([4, 5, 6], 3, [4, 5, 6]),
        ([1, 1, 2, 2, 2], 2, [1, 2]),
        # single element repeated
        ([9, 9, 9, 9], 1, [9]),
        # negatives and zero
        ([-1, -1, 0, 0, 0, 5], 2, [0, -1]),
        ([-10000, -10000, 10000], 1, [-10000]),
        # most frequent element appears last / unsorted input
        ([3, 1, 2, 2, 3, 3], 1, [3]),
        ([5, 4, 4, 3, 3, 3, 2, 2, 2, 2], 3, [2, 3, 4]),
        # k smaller than unique count, ties below the cutoff are fine
        ([1, 1, 1, 2, 3, 4, 5], 1, [1]),
        # large input (n = 100000)
        (big, 2, [7, -3]),
    ]
    for i, (nums, k, want) in enumerate(testcases):
        s = Solution()
        got = s.topKFrequent(list(nums), k)
        try:
            # answer may be returned in any order
            ok = sorted(got) == sorted(want)
        except TypeError:
            # malformed output (e.g. None)
            ok = False
        if not ok:
            print('Test {}: got != want, {} != {}'.format(i, got if len(str(got)) < 200 else '...', want))
        else:
            print('Test {}: passed'.format(i))
