from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         chars = Counter()
         left = right = 0
         res = 0
         while right < len(s):
            r = s[right]
            chars[r] += 1
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
         return res

if __name__ == '__main__':
    s = Solution()
    printable = ''.join(chr(c) for c in range(32, 127))
    testcases = [
        # examples
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        # empty and single character
        ("", 0),
        (" ", 1),
        ("a", 1),
        # no repeats at all
        ("abcdef", 6),
        ("au", 2),
        # duplicate is not adjacent: left pointer must jump past it
        ("dvdf", 3),
        ("abba", 2),
        ("tmmzuxt", 5),
        # longest window is at the end
        ("aab", 2),
        ("aaaabcd", 4),
        # spaces, digits and symbols count as characters
        ("a b c", 3),
        ("12 3!2", 5),
        ("!@#!@#$", 4),
        # case sensitive
        ("aAbBaA", 4),
        # every printable character once (95 distinct)
        (printable, 95),
        # max size (n = 50000), repeating all printable characters
        (printable * (5 * 10**4 // 95 + 1), 95),
        ("a" * 5 * 10**4, 1),
    ]
    for i, (string, want) in enumerate(testcases):
        got = s.lengthOfLongestSubstring(string)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
