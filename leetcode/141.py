from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # Floyd's Cycle-Finding Algorithm
        # If there is a cycle: The fast pointer will eventually loop around and "lap" the slow pointer. They will meet at the exact same node (slow == fast), confirming a cycle exists.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def build(vals, pos):
    # pos is the index the tail's next pointer connects to, or -1 for no cycle
    nodes = [ListNode(val) for val in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        # single node pointing at itself
        ([1], 0, True),
        ([1, 2], -1, False),
        # tail pointing at itself
        ([1, 2], 1, True),
        # duplicate values without a cycle: comparing vals instead of nodes fails here
        ([1, 1, 1, 1], -1, False),
        ([1, 2, 1, 2], -1, False),
        ([-10**5, 0, 10**5], 2, True),
        # Max size (n = 10^4): no cycle, full cycle, tail self-loop, cycle from the middle.
        (list(range(10**4)), -1, False),
        (list(range(10**4)), 0, True),
        (list(range(10**4)), 10**4 - 1, True),
        (list(range(10**4)), 5000, True),
    ]
    for i, (vals, pos, want) in enumerate(testcases):
        got = s.hasCycle(build(vals, pos))
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
