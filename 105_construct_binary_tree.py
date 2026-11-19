# LeetCode provides TreeNode.
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        positions = {value: i for i, value in enumerate(inorder)}
        pre_index = 0

        def build(left: int, right: int):
            nonlocal pre_index
            if left > right:
                return None
            value = preorder[pre_index]
            pre_index += 1
            root = TreeNode(value)
            mid = positions[value]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
