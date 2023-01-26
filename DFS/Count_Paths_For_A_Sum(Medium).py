class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_recur(root, S, [])


def count_paths_recur(root, S, visited):
    if not root:
        return 0

    visited.append(root.val)
    pathCount, pathSum = 0, 0

    for i in range(len(visited) - 1, -1, -1):
        pathSum += visited[i]
        if pathSum == S:
            pathCount += 1

    pathCount += count_paths_recur(root.left, S, visited)
    pathCount += count_paths_recur(root.right, S, visited)

    del visited[-1]

    return pathCount


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
