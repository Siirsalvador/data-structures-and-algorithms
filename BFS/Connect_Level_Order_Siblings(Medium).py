from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    if root:
        store = deque()
        store.append(root)
        target = None
        while store:
            size = len(store)
            for _ in range(size):
                cur = store.popleft()
                print(target)
                if target:
                    return cur.val
                if key == cur.val:
                    print('here')
                    print(cur.val)
                    target = True

    return None


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 9)
    if result:
        print(result.val)

    result = find_successor(root, 12)
    if result:
        print(result.val)


main()
