# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        pass


if __name__ == '__main__':
    s = Solution()
    testcases = [
        (ListNode(2, ListNode(4, ListNode(3))),
         ListNode(5, ListNode(6, ListNode(4))),
         ListNode(7, ListNode(0, ListNode(8)))),
        (ListNode(0), ListNode(0), ListNode(0)),
        (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
         ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
         ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))))))
    ]
    for i, (l1, l2, want) in enumerate(testcases):
        got = s.addTwoNumbers(l1, l2)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
