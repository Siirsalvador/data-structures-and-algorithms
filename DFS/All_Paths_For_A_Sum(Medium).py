class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    recur_paths(root, sum, [], allPaths)
    return allPaths


def recur_paths(root, sum, currentPath, allPaths):
    if root is None:
        return

    currentPath.append(root.val)

    if root.left is None and root.right is None and sum == root.val:
        allPaths.append(list(currentPath))
    else:
        recur_paths(root.left, sum - root.val, currentPath, allPaths)
        recur_paths(root.right, sum - root.val, currentPath, allPaths)

    currentPath.pop(-1)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
