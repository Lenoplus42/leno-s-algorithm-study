# TreeNode 由 LeetCode 提供；题目保证 p、q 存在于 BST 中，且节点值唯一。
class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                # 分居两侧，或当前节点就是其中一个目标。
                return node
