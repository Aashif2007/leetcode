# LeetCode provides ListNode and TreeNode.
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node

        return build(0, len(values) - 1)
