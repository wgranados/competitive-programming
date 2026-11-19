from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0 
        right = len(height) - 1
        while left < right:
            water = min(height[left], height[right]) * abs(left-right)
            area = max(area, water)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return area
         


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([0, 0], 0),
        ([0, 10**4], 0),
        ([10**4, 10**4], 10**4),
        ([1, 2, 1], 2),
        # widest pair wins even though the lines between are shorter
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 4, 3], 4),
        # two tallest lines are adjacent: narrow but tall beats wide but short
        ([2, 3, 4, 5, 18, 17, 6], 17),
        # strictly increasing: best pair is the middle line with the last one
        (list(range(1, 10**4 + 1)), 25_000_000),
        (list(range(10**4, 0, -1)), 25_000_000),
        # Max size (n = 10^5): an O(n^2) solution will be far too slow here.
        ([10**4] * 10**5, 999_990_000),
        ([10**4] + [0] * (10**5 - 2) + [10**4], 999_990_000),
    ]
    for i, (height, want) in enumerate(testcases):
        got = s.maxArea(height)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
