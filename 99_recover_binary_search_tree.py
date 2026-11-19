
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        first = second = previous = None

        def inorder(node):
            nonlocal first, second, previous
            if node is None:
                return
            inorder(node.left)
            if previous is not None and previous.val > node.val:
                if first is None:
                    first = previous
                second = node
            previous = node
            inorder(node.right)

        inorder(root)
        if first is not None and second is not None:
            first.val, second.val = second.val, first.val
