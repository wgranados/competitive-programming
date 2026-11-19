class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        forward = [nums[0]]
        backwards = [nums[-1]]
        for i in range(1, len(nums)):
            forward.append(forward[-1]*nums[i])
            backwards.append(backwards[-1]*nums[len(nums)-1-i])
        res =[]
        for i in range(len(nums)):
            left = forward[i-1] if i > 0 else 1
            right = backwards[len(nums)-2-i] if i < len(nums)-1 else 1
            res.append(left*right)
        return res

if __name__ == '__main__':
    import random
    import time

    testcases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([0, 5], [5, 0]),
        ([0, 0], [0, 0]),
        ([1, 0, 2, 0], [0, 0, 0, 0]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([-1, -2, -3, -4], [-24, -12, -8, -6]),
        ([-1, 2, -3, 4], [-24, 12, -8, 6]),
        ([30, 30, 30, 30, 30, 30], [30**5] * 6),
    ]
    for i, (nums, want) in enumerate(testcases):
        s = Solution()
        got = s.productExceptSelf(list(nums))
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
