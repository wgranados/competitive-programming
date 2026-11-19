class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            mstart, mend = merged[-1][0], merged[-1][1]
            if start <= mend and mend < end:
                merged[-1][1] = end
            elif start > mend:
                merged.append(intervals[i])

        return merged


if __name__ == '__main__':
    testcases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[4, 7], [1, 4]], [[1, 7]]),
        ([[1, 4]], [[1, 4]]),
        ([[1, 10], [2, 3], [4, 5]], [[1, 10]]),
        ([[5, 6], [1, 2], [3, 4]], [[1, 2], [3, 4], [5, 6]]),
        ([[1, 3], [1, 3]], [[1, 3]]),
        ([[0, 0], [0, 0]], [[0, 0]]),
        ([[2, 2], [1, 3]], [[1, 3]]),
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[2, 3], [4, 5], [6, 7], [1, 10]], [[1, 10]]),
    ]
    for i, (intervals, want) in enumerate(testcases):
        s = Solution()
        got = s.merge([list(x) for x in intervals])
        # output order is not specified, so compare sorted
        if got is None or sorted(got) != sorted(want):
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
