class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if char == '}' and p != '{':
                    return False
                if char == ')' and p != '(':
                    return False
                if char == ']' and p != '[':
                    return False
        return True if len(stack) == 0 else False

if __name__ == '__main__':
    import random
    import time

    testcases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("(", False),
        (")", False),
        ("((", False),
        ("))", False),
        ("(()", False),
        ("())", False),
        (")(", False),
        ("}{", False),
        ("{[]}", True),
        ("(([]){})", True),
        ("([}}])", False),
        ("(){}}{", False),
        ("[[[]", False),
    ]
    for i, (s, want) in enumerate(testcases):
        got = Solution().isValid(s)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))