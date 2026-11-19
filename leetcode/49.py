class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pairs = []
        for anagram in strs:
            pairs.append((anagram, sorted(anagram)))
        pairs = sorted(pairs, key=lambda v: v[1])
        final_pairs = [[pairs[0][0]]]
        for i in range(1, len(pairs)):
            curr_anagram = pairs[i][1]
            prev_anagram = pairs[i-1][1]
            if curr_anagram == prev_anagram:
                final_pairs[-1].append(pairs[i][0])
            else:
                final_pairs.append([pairs[i][0]])
        return final_pairs


def normalize(groups):
    # order of groups and of strings within a group does not matter,
    # but duplicates do, so sort instead of building a set
    return sorted(sorted(g) for g in groups)


if __name__ == '__main__':
    testcases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["", ""], [["", ""]]),
        (["", "a"], [[""], ["a"]]),
        (["abc", "abc"], [["abc", "abc"]]),
        (["ab", "ba", "abc"], [["ab", "ba"], ["abc"]]),
        (["aab", "abb"], [["aab"], ["abb"]]),
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),
        (["listen", "silent", "enlist", "google", "gogole"], [["listen", "silent", "enlist"], ["google", "gogole"]]),
        (["bdddddddddd", "bbbbbbbbbbc"], [["bdddddddddd"], ["bbbbbbbbbbc"]]),
    ]
    for i, (strs, want) in enumerate(testcases):
        s = Solution()
        got = s.groupAnagrams(list(strs))
        try:
            ok = normalize(got) == normalize(want)
        except TypeError:
            # malformed output (e.g. None, or non-str items in a group)
            ok = False
        if not ok:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))