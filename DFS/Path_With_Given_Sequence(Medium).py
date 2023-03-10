class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    return find_path_recur(root, sequence, 0)


def find_path_recur(root, sequence, level):
    if not root:
        return False

    if root.val == sequence[level]:
        if root.left is None and root.right is None:
            return True
        return find_path_recur(root.left, sequence, level + 1) or find_path_recur(root.right, sequence, level + 1)

    return False


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
