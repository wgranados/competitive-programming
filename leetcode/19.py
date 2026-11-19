class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        pos = {}
        curr = head
        index = 0
        while curr != None:
            pos[index] = curr
            curr = curr.next
            index +=1
        last_n = index -n 
        last_n_node = pos[last_n]
        if last_n == 0:
            return last_n_node.next
        # Otherwise remove the previous link and then return the head
        prev_node = pos[last_n - 1]
        prev_node.next = last_n_node.next
        return head

    def removeNthFromEndTwoPass(self, head: ListNode | None, n: int) -> ListNode | None:
        # Approach 1, O(1) memory: count the length L, then walk from a dummy
        # node to the (L - n)th node and unlink the node after it.
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        # the dummy node means removing the head needs no special case
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(length - n):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next

    def removeNthFromEndOnePass(self, head: ListNode | None, n: int) -> ListNode | None:
        # Approach 2, O(1) memory: move a fast pointer n + 1 steps ahead of a slow
        # pointer (both starting at a dummy node), advance both until fast falls off
        # the end, then unlink the node after slow.
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        # the gap stays at n + 1, so when fast is None slow sits just before the target
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

def build(vals):
    head = None
    for val in reversed(vals):
        head = ListNode(val, head)
    return head


def to_list(head, limit=1_000):
    # limit guards against a cycle left behind by buggy pointer rewiring
    vals = []
    while head is not None and len(vals) < limit:
        vals.append(head.val)
        head = head.next
    return vals


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        # n == sz removes the head: needs a dummy node or a special case
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        # n == 1 removes the tail
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2, 3], 2, [1, 3]),
        # duplicate values: removing by value instead of by position fails here
        ([7, 7, 7, 7], 2, [7, 7, 7]),
        ([0, 100, 0, 100], 3, [0, 0, 100]),
        # Max size (sz = 30): remove head, middle, and tail.
        (list(range(30)), 30, list(range(1, 30))),
        (list(range(30)), 15, list(range(15)) + list(range(16, 30))),
        (list(range(30)), 1, list(range(29))),
    ]
    for method in (s.removeNthFromEnd, s.removeNthFromEndTwoPass, s.removeNthFromEndOnePass):
        print(method.__name__)
        for i, (vals, n, want) in enumerate(testcases):
            got = to_list(method(build(vals), n))
            if got != want:
                print('Test {}: got != want, {} != {}'.format(i, got, want))
            else:
                print('Test {}: passed'.format(i))
