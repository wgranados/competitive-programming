import queue 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.prev = -float('inf')
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return self.isValidBST(root.right)

if __name__ == '__main__':
    testcases = [
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),
        (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False)
    ]
    for i, (tree, want) in enumerate(testcases):
        s = Solution()
        got = s.isValidBST(tree)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))