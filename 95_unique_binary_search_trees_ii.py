# LeetCode provides TreeNode.
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []

        def build(low: int, high: int) -> list[TreeNode | None]:
            if low > high:
                return [None]
            trees = []
            for value in range(low, high + 1):
                for left in build(low, value - 1):
                    for right in build(value + 1, high):
                        root = TreeNode(value)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees

        return build(1, n)
