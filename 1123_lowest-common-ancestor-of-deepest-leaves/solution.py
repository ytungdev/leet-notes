from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time : Beats 100.0 %
# Memo : Beats 45.59 %
class Solution1:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0,None)

            depth_l, tree_l = dfs(node.left)
            depth_r, tree_r = dfs(node.right)
            
            if depth_l == depth_r:
                return (depth_l+1, node)
            elif depth_l > depth_r:
                return (depth_l+1, tree_l)
            else:
                return (depth_r+1, tree_r)

        return dfs(root)[1]


# Time : Beats  6.14 %
# Memo : Beats 92.97 %
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find_depth(node, curr_depth):
            if not node:
                return float('-inf')
            if node.left is None and node.right is None:
                return curr_depth
            else:
                max_depth = max(
                    find_depth(node.left, curr_depth+1), 
                    find_depth(node.right, curr_depth+1))
                return max_depth
        def find_lca(node):
            l_depth = find_depth(node.left,1)
            r_depth = find_depth(node.right,1)
            if l_depth == r_depth:
                return node
            elif l_depth >= r_depth:
                return find_lca(node.left)
            else:
                return find_lca(node.right)

        return find_lca(root)