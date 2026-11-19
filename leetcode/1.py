class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}
        for index, num in enumerate(nums):
            mapping[num] = index
        for i, num in enumerate(nums):
            compliment = target-num
            if compliment in mapping and mapping[compliment] != i:
                compliment_index = mapping[compliment]
                return [i, compliment_index]


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for i, (nums, target, want) in enumerate(testcases):
        got = s.twoSum(nums, target)
        # answer may be returned in any order
        if sorted(got) != sorted(want):
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
        