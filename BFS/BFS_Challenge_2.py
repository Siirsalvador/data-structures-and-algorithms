from __future__ import print_function

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root:
        store = deque()
        store.append(root)
        cur = None
        while store:
            size = len(store)
            for _ in range(size):
                cur = store.popleft()
                if cur.left:
                    store.append(cur.left)
                if cur.right:
                    store.append(cur.right)
            result.append(cur)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
