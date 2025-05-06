# 236. Lowest Common Ancestor of a Binary Tree
# Tags: [tree, dfs, recursion, binary-tree, interview-frequent]
# Difficulty: Medium
# Time: O(n) | Space: O(h) where h is height of tree

"""
Input Tree Visualization:
                    3 🌳
                   / \
                  5   1
                 / \ / \
                6  2 0  8
                  / \
                 7   4

Problem: Find the lowest common ancestor (LCA) of two nodes in a binary tree.
The LCA is the deepest node that is an ancestor of both nodes.

Key Insight: DFS + Bottom-up recursion. Return node when found target, 
bubble up results to find where paths intersect.
"""

# 236. Lowest Common Ancestor of a Binary Tree
# Tags: [tree, dfs, recursion, binary-tree, interview-frequent]
# Difficulty: Medium
# Time: O(n) | Space: O(h) where h is height of tree

"""
Input Tree Visualization:
                    3 🌳
                   / \
                  5   1
                 / \ / \
                6  2 0  8
                  / \
                 7   4

Problem: Find the lowest common ancestor (LCA) of two nodes in a binary tree.
The LCA is the deepest node that is an ancestor of both nodes.

Key Insight: DFS + Bottom-up recursion. Return node when found target, 
bubble up results to find where paths intersect.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
"""
Input Tree Visualization:
                    3 🌳
                   / \
                  5   1
                 / \ / \
                6  2 0  8
                  / \
                 7   4
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, level=0):
            if not node:
                prefix = "│   " * level
                print(f"{prefix}┌── ")
                print(f"{prefix}│ 💨 None")
                print(f"{prefix}└── ")
                return None
                
            prefix = "│   " * level
            print(f"{prefix}┌── 🔵 Node: {node.val}")
            
            # Found target node
            if node == p or node == q:
                print(f"{prefix}└── ⭐ Target found: {node.val}")
                return node
                
            # Search children
            print(f"{prefix}├── Searching ←")
            left = dfs(node.left, level + 1)
            
            print(f"{prefix}├── Searching →")
            right = dfs(node.right, level + 1)
            
            # Process results
            if left and right:
                print(f"{prefix}├── 💫 LCA found!")
                return node
                
            result = left or right
            if result:
                direction = "←" if left else "→"
                print(f"{prefix}└── ↑ Return {direction} path: {result.val}")
            else:
                print(f"{prefix}└── ✖ Dead end")
                
            return result

        print("\n┌────────── DFS Path ──────────")
        ans = dfs(root)
        print("└──────────────────────────────")
        return ans

# Test code

# Test code
def build_test_tree():
    """Builds test tree:
                3
               / \
              5   1
             / \ / \
            6  2 0  8
              / \
             7   4
    """
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    return root

if __name__ == "__main__":
    root = build_test_tree()
    p = root.left.right.left # node 5
    q = root.right  # node 1
    Solution().lowestCommonAncestor(root, p, q)

# One Line Lesson:
# LCA can be found by doing DFS and bubbling up results - when both targets 
# are found in different subtrees, their ancestor is the LCA! 🎯

# One Line Lesson:
# LCA can be found by doing DFS and bubbling up results - when both targets 
# are found in different subtrees, their ancestor is the LCA! 🎯
# One Line Lesson:
# LCA can be found by doing DFS and bubbling up results - when both targets 
# are found in different subtrees, their ancestor is the LCA! 🎯