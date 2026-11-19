from typing import Optional
import sys
sys.setrecursionlimit(20_000)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
            
        while curr is not None:
            next_node = curr.next # Save next node
            curr.next = prev # Reverse the pointer
            prev = curr # move prev forward
            curr = next_node # move curr forward
        return prev


    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # reverse everything after head; head.next is now the tail of that list
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


def build(vals):
    head = None
    for val in reversed(vals):
        head = ListNode(val, head)
    return head


def to_list(head, limit=10_000):
    # limit guards against a cycle left behind by a buggy reversal
    vals = []
    while head is not None and len(vals) < limit:
        vals.append(head.val)
        head = head.next
    return vals


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([7, 7, 7], [7, 7, 7]),
        ([-5000, 0, 5000], [5000, 0, -5000]),
        # Max size: a recursive solution needs the raised recursion limit here.
        (list(range(5000)), list(range(4999, -1, -1))),
    ]
    for method in (s.reverseList, s.reverseListRecursive):
        print(method.__name__)
        for i, (vals, want) in enumerate(testcases):
            got = to_list(method(build(vals)))
            if got != want:
                # max-size lists are too long to print in full
                print('Test {}: got != want, {} != {}'.format(i, got[:10], want[:10]))
            else:
                print('Test {}: passed'.format(i))
